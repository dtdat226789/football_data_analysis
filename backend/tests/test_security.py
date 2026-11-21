"""Security regression tests for the API edge and request guards.

These avoid PostgreSQL: the middleware and the file-backed catalog are enough
to prove that direct-origin requests are rejected, the health probes stay open,
and the hot fixture/report paths reject abusive input shapes.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from apps import deps  # noqa: E402
from apps.main import create_app  # noqa: E402
from db_common import DatabaseNotConfigured, get_conn  # noqa: E402


@pytest.fixture()
def clean_env(monkeypatch):
    for name in (
        "WORKER_SHARED_SECRET",
        "API_RATE_LIMIT_PER_MINUTE",
        "DISABLE_DOCS",
    ):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("ALLOW_INSECURE_API", "1")
    return monkeypatch


def test_worker_secret_is_required_on_api_routes(clean_env):
    clean_env.setenv("WORKER_SHARED_SECRET", "s3cret")
    app = create_app()

    with TestClient(app) as client:
        assert client.get("/api/v1/leagues").status_code == 403
        assert (
            client.get(
                "/api/v1/leagues",
                headers={"x-worker-secret": "wrong"},
            ).status_code
            == 403
        )
        assert (
            client.get(
                "/api/v1/leagues",
                headers={"x-worker-secret": "s3cret"},
            ).status_code
            == 200
        )
        # Probes must remain reachable for the Worker cron and platform checks.
        assert client.get("/health").status_code == 200
        assert client.get("/api/v1/health").status_code == 200


def test_worker_secret_protects_legacy_analysis_routes(clean_env):
    clean_env.setenv("WORKER_SHARED_SECRET", "s3cret")
    app = create_app()

    with TestClient(app) as client:
        assert client.get("/leagues").status_code == 403
        assert (
            client.get("/leagues", headers={"x-worker-secret": "s3cret"}).status_code
            == 200
        )


def test_missing_worker_secret_fails_closed(monkeypatch):
    monkeypatch.delenv("WORKER_SHARED_SECRET", raising=False)
    monkeypatch.delenv("ALLOW_INSECURE_API", raising=False)
    app = create_app()

    with TestClient(app) as client:
        denied = client.get("/api/v1/leagues")
        assert denied.status_code == 503
        assert denied.json()["detail"] == "api authentication is not configured"
        assert client.get("/health").status_code == 200


def test_docs_require_the_worker_secret(clean_env):
    clean_env.setenv("WORKER_SHARED_SECRET", "s3cret")
    app = create_app()

    with TestClient(app) as client:
        for path in ("/docs", "/redoc", "/openapi.json"):
            assert client.get(path).status_code == 403
            assert client.get(path, headers={"x-worker-secret": "s3cret"}).status_code == 200


def test_rate_limit_ignores_spoofed_forwarding_headers(clean_env):
    clean_env.setenv("WORKER_SHARED_SECRET", "s3cret")
    clean_env.setenv("API_RATE_LIMIT_PER_MINUTE", "2")
    app = create_app()

    with TestClient(app) as client:
        headers = {"x-worker-secret": "s3cret"}
        for ip in ("1.1.1.1", "2.2.2.2", "3.3.3.3"):
            spoofed = dict(headers)
            spoofed["cf-connecting-ip"] = ip
            spoofed["x-forwarded-for"] = ip
            response = client.get("/api/v1/leagues", headers=spoofed)
            if ip == "3.3.3.3":
                assert response.status_code == 429
            else:
                assert response.status_code == 200

        # A distinct Worker-injected client IP gets its own bucket.
        trusted = dict(headers, **{"x-worker-client-ip": "9.9.9.9"})
        assert client.get("/api/v1/leagues", headers=trusted).status_code == 200


def test_rate_limit_can_be_enabled(clean_env):
    clean_env.setenv("API_RATE_LIMIT_PER_MINUTE", "2")
    app = create_app()

    with TestClient(app) as client:
        assert client.get("/api/v1/leagues").status_code == 200
        assert client.get("/api/v1/leagues").status_code == 200
        limited = client.get("/api/v1/leagues")
        assert limited.status_code == 429
        assert limited.headers["Retry-After"].isdigit()


def test_production_docs_can_be_disabled(clean_env):
    clean_env.setenv("DISABLE_DOCS", "1")
    app = create_app()

    with TestClient(app) as client:
        assert client.get("/docs").status_code == 404
        assert client.get("/redoc").status_code == 404
        assert client.get("/openapi.json").status_code == 404


def test_input_bounds_are_enforced_before_any_io(clean_env):
    app = create_app()

    with TestClient(app) as client:
        assert client.get("/api/v1/fixtures", params={"min_confidence": 2}).status_code == 422
        assert client.get("/api/v1/fixtures", params={"limit": 0}).status_code == 422
        assert client.get("/api/v1/fixtures", params={"offset": -1}).status_code == 422
        assert client.get("/api/v1/teams", params={"q": "x" * 101}).status_code == 422


def test_readonly_cursor_sets_a_readonly_session(monkeypatch):
    class FakeCursor:
        def close(self):
            pass

    class FakeConn:
        def __init__(self):
            self.session = None
            self.rolled_back = False
            self.closed = False

        def set_session(self, **kwargs):
            self.session = kwargs

        def cursor(self, **_kwargs):
            return FakeCursor()

        def rollback(self):
            self.rolled_back = True

        def close(self):
            self.closed = True

    conn = FakeConn()
    monkeypatch.setattr(deps, "get_conn", lambda: conn)

    with deps.fetched_cursor() as cur:
        assert isinstance(cur, FakeCursor)

    assert conn.session == {"readonly": True, "autocommit": False}
    assert conn.rolled_back is True
    assert conn.closed is True


def test_missing_database_url_raises_handled_error(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(DatabaseNotConfigured):
        get_conn()


def test_missing_database_url_returns_503(clean_env):
    clean_env.delenv("DATABASE_URL", raising=False)
    app = create_app()

    with TestClient(app) as client:
        response = client.get("/api/v1/leagues/premier")
        assert response.status_code == 503
        assert response.json()["detail"] == "database unavailable"
