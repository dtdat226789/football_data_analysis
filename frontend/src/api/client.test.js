import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { withRequestSignal } from "../lib/requestSignal.js";
import { ApiError, api, request } from "./client.js";

function mockFetch(response) {
  // Typed as the real global, so the assertions below that read
  // `fetch.mock` need a cast to reach the mock's own shape.
  globalThis.fetch = vi.fn().mockResolvedValue(response);
}

/** @returns {import("vitest").Mock} */
const mockedFetch = () => /** @type {import("vitest").Mock} */ (globalThis.fetch);

describe("request", () => {
  beforeEach(() => {
    globalThis.fetch = vi.fn();
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("omits undefined, null and empty params but keeps falsy values like 0", async () => {
    mockFetch(new Response(JSON.stringify({ ok: true }), { status: 200 }));

    await request("/x", { a: undefined, b: null, c: "", d: 1, e: 0, f: "true" });

    const url = new URL(mockedFetch().mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/x");
    expect([...url.searchParams.keys()]).toEqual(["d", "e", "f"]);
    expect(url.searchParams.get("d")).toBe("1");
    expect(url.searchParams.get("e")).toBe("0");
  });

  it("throws ApiError with the detail from a JSON error body", async () => {
    mockFetch({
      ok: false,
      status: 404,
      statusText: "Not Found",
      json: async () => ({ detail: "League not found" }),
    });

    const error = await api.league("nope").catch((e) => e);
    expect(error).toBeInstanceOf(ApiError);
    expect(error.status).toBe(404);
    expect(error.message).toBe("League not found");
  });

  it("falls back to statusText when the error body is not JSON", async () => {
    mockFetch({
      ok: false,
      status: 500,
      statusText: "Server Error",
      json: async () => {
        throw new SyntaxError("body is not JSON");
      },
    });

    const error = await api.health().catch((e) => e);
    expect(error).toBeInstanceOf(ApiError);
    expect(error.status).toBe(500);
    expect(error.message).toBe("Server Error");
  });

  it("reports a friendly message when the network cannot be reached", async () => {
    mockedFetch().mockRejectedValue(new TypeError("fetch failed"));

    await expect(api.health()).rejects.toMatchObject({
      status: 0,
      message: "Cannot reach the API server. Is the backend running?",
    });
  });

  it("returns the parsed JSON body on success", async () => {
    mockFetch(new Response(JSON.stringify({ alive: true }), { status: 200 }));

    await expect(api.health()).resolves.toEqual({ alive: true });
  });

  it("requests health under the /api/v1 namespace (matches backend route)", async () => {
    mockFetch(new Response(JSON.stringify({ status: "ok" }), { status: 200 }));

    await api.health();

    const url = new URL(mockedFetch().mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/health");
  });

  it("encodes path parameters so a slug cannot alter the route or query", async () => {
    mockFetch(new Response(JSON.stringify({ ok: true }), { status: 200 }));

    await api.league("a/b?x=1");

    const url = new URL(mockedFetch().mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/leagues/a%2Fb%3Fx%3D1");
    expect(url.search).toBe("");
  });

  it("passes a timeout signal to fetch on every request", async () => {
    mockFetch(new Response(JSON.stringify({ ok: true }), { status: 200 }));

    await api.health();

    expect(mockedFetch().mock.calls[0][1].signal).toBeInstanceOf(AbortSignal);
  });

  it("honours the request signal bound by a loader", async () => {
    mockFetch(new Response(JSON.stringify({ ok: true }), { status: 200 }));
    const controller = new AbortController();

    await withRequestSignal(controller.signal, () => api.health());
    const signal = mockedFetch().mock.calls[0][1].signal;
    expect(signal.aborted).toBe(false);

    controller.abort();
    expect(signal.aborted).toBe(true);
  });

  it("only builds URLs for chart names that are plain PNG files", () => {
    expect(api.chartUrl("premier", "avg_goals.png")).toBe(
      "/api/v1/analysis/premier/charts/avg_goals.png",
    );
    expect(api.chartUrl("premier", "../../secrets")).toBeNull();
    expect(api.chartUrl("premier", "chart.svg")).toBeNull();
  });
});

describe("teamStats", () => {
  it("calls /api/v1/teams/{slug}/stats with league/view params", async () => {
    mockFetch(new Response(JSON.stringify({ team: "spurs" }), { status: 200 }));

    await api.teamStats("spurs", { league: "premier", view: "classic" });

    const url = new URL(mockedFetch().mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/teams/spurs/stats");
    expect(url.searchParams.get("league")).toBe("premier");
    expect(url.searchParams.get("view")).toBe("classic");
  });
});
describe("dashboard client methods", () => {
  it("requests the team KPI sub-resource with filters", async () => {
    mockFetch(new Response(JSON.stringify({ team: "spurs" }), { status: 200 }));

    await api.teamKpi("spurs", { league: "premier", season: "2024-2025", n: 10 });

    const url = new URL(mockedFetch().mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/teams/spurs/kpi");
    expect(url.searchParams.get("season")).toBe("2024-2025");
    expect(url.searchParams.get("n")).toBe("10");
  });

  it("requests club analysis with filters and season list", async () => {
    mockFetch(new Response(JSON.stringify({}), { status: 200 }));

    await api.clubAnalysis({ league: "premier", season: "", team: "arsenal" });
    expect(new URL(mockedFetch().mock.calls[0][0]).pathname).toBe("/api/v1/club-analysis");

    mockFetch(new Response(JSON.stringify({}), { status: 200 }));
    await api.leagueSeasons("premier");
    expect(new URL(mockedFetch().mock.calls[0][0]).pathname).toBe("/api/v1/leagues/premier/seasons");
  });
});

describe("api.matchInsights", () => {
  beforeEach(() => {
    globalThis.fetch = vi.fn();
  });

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("requests the insights sub-resource for the match", async () => {
    mockFetch(new Response(JSON.stringify({ api_id: 1001 }), { status: 200 }));

    await api.matchInsights(1001);

    const url = new URL(mockedFetch().mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/matches/1001/insights");
  });

  it("passes the h2h limit through as a query param", async () => {
    mockFetch(new Response(JSON.stringify({}), { status: 200 }));

    await api.matchInsights(1001, { limit: 5 });

    const url = new URL(mockedFetch().mock.calls[0][0]);
    expect(url.searchParams.get("limit")).toBe("5");
  });
});
