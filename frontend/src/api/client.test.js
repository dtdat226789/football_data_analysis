import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { ApiError, api, request } from "./client.js";

function mockFetch(response) {
  globalThis.fetch = vi.fn().mockResolvedValue(response);
}

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

    const url = new URL(globalThis.fetch.mock.calls[0][0]);
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
    globalThis.fetch.mockRejectedValue(new TypeError("fetch failed"));

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

    const url = new URL(globalThis.fetch.mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/health");
  });
});

describe("teamStats", () => {
  it("calls /api/v1/teams/{slug}/stats with league/view params", async () => {
    mockFetch(new Response(JSON.stringify({ team: "spurs" }), { status: 200 }));

    await api.teamStats("spurs", { league: "premier", view: "classic" });

    const url = new URL(globalThis.fetch.mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/teams/spurs/stats");
    expect(url.searchParams.get("league")).toBe("premier");
    expect(url.searchParams.get("view")).toBe("classic");
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

    const url = new URL(globalThis.fetch.mock.calls[0][0]);
    expect(url.pathname).toBe("/api/v1/matches/1001/insights");
  });

  it("passes the h2h limit through as a query param", async () => {
    mockFetch(new Response(JSON.stringify({}), { status: 200 }));

    await api.matchInsights(1001, { limit: 5 });

    const url = new URL(globalThis.fetch.mock.calls[0][0]);
    expect(url.searchParams.get("limit")).toBe("5");
  });
});
