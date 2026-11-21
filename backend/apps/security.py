"""Request guards for the public API.

The Cloudflare Worker is the only intended client of the Render origin. When
``WORKER_SHARED_SECRET`` is configured, every API request must carry the same
value in ``X-Worker-Secret``; the Worker injects it and strips any client copy.
This keeps a public Render URL from turning into an unauthenticated API and
file/DB resource sink.

A small, opt-in fixed-window limiter is also available for direct-to-origin
deployments. Cloudflare rate limiting remains the primary edge control; the
backend limiter is a second line of defence and is intentionally disabled
unless ``API_RATE_LIMIT_PER_MINUTE`` is set.

Fail closed: a protected route with no ``WORKER_SHARED_SECRET`` configured is
rejected with 503 unless ``ALLOW_INSECURE_API=1`` is set explicitly for local
development/tests. Never set that flag in production.

The limiter keys on ``X-Worker-Client-IP``, which the Worker derives from
Cloudflare's own view of the client and overwrites on every proxied request.
Client-supplied forwarding headers are never trusted.
"""
from __future__ import annotations

import hmac
import os
import threading
import time
from collections import deque
from typing import Deque

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

SECRET_HEADER = "x-worker-secret"
CLIENT_IP_HEADER = "x-worker-client-ip"
HEALTH_PATHS = frozenset({"/health", "/api/v1/health"})
DOCS_PATHS = ("/docs", "/redoc", "/openapi.json")
WINDOW_SECONDS = 60


def _env_flag(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def _path_is_protected(path: str) -> bool:
    """API, docs and legacy analysis routes, but never the health probes."""
    if path in HEALTH_PATHS:
        return False
    return (
        path == "/api"
        or path.startswith("/api/")
        or path == "/leagues"
        or path.startswith("/leagues/")
        or any(p == path or path.startswith(f"{p}/") for p in DOCS_PATHS)
    )


def _client_key(request: Request) -> str:
    # Only the Worker-injected header is trusted: it is set after the client
    # copy is stripped and the shared-secret check has passed. Forwarding
    # headers from the client are deliberately ignored.
    value = request.headers.get(CLIENT_IP_HEADER, "").strip()
    if value:
        return value.split(",", 1)[0].strip()
    return request.client.host if request.client else "unknown"


class _FixedWindowLimiter:
    """Thread-safe in-process fixed-window limiter.

    Deliberately small: a single Render instance needs only a coarse cap, and
    Cloudflare is responsible for the global limit. Keeping it in-process means
    no extra dependency or shared Redis requirement for this project.
    """

    def __init__(self, limit: int, window_seconds: int = WINDOW_SECONDS):
        self.limit = limit
        self.window_seconds = window_seconds
        self._hits: dict[str, Deque[float]] = {}
        self._lock = threading.Lock()

    def allow(self, key: str, now: float | None = None) -> tuple[bool, int]:
        now = time.monotonic() if now is None else now
        cutoff = now - self.window_seconds
        with self._lock:
            if len(self._hits) > 2048:
                for stale_key, stale_hits in list(self._hits.items()):
                    while stale_hits and stale_hits[0] <= cutoff:
                        stale_hits.popleft()
                    if not stale_hits:
                        self._hits.pop(stale_key, None)
            hits = self._hits.setdefault(key, deque())
            while hits and hits[0] <= cutoff:
                hits.popleft()
            if len(hits) >= self.limit:
                retry_after = max(1, int(self.window_seconds - (now - hits[0])))
                return False, retry_after
            hits.append(now)
            return True, 0


def _configured_limiter() -> _FixedWindowLimiter | None:
    raw = os.getenv("API_RATE_LIMIT_PER_MINUTE", "").strip()
    if not raw:
        return None
    try:
        limit = int(raw)
    except ValueError:
        return None
    return _FixedWindowLimiter(limit) if limit > 0 else None


def install_security(app: FastAPI) -> None:
    """Install the Worker-secret check and optional request limiter."""
    limiter = _configured_limiter()

    @app.middleware("http")
    async def guard(request: Request, call_next):
        if not _path_is_protected(request.url.path):
            return await call_next(request)

        expected = os.getenv("WORKER_SHARED_SECRET", "").strip()
        if not expected:
            if not _env_flag("ALLOW_INSECURE_API"):
                # Misconfiguration must not silently open the origin.
                return JSONResponse(
                    {"detail": "api authentication is not configured"},
                    status_code=503,
                )
        else:
            supplied = request.headers.get(SECRET_HEADER, "")
            if not hmac.compare_digest(
                supplied.encode("utf-8"), expected.encode("utf-8")
            ):
                return JSONResponse(
                    {"detail": "forbidden"},
                    status_code=403,
                )

        if limiter is not None:
            allowed, retry_after = limiter.allow(_client_key(request))
            if not allowed:
                return JSONResponse(
                    {"detail": "too many requests"},
                    status_code=429,
                    headers={"Retry-After": str(retry_after)},
                )

        return await call_next(request)
