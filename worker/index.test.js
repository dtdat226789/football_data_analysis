import assert from "node:assert/strict";
import { afterEach, test } from "node:test";

import worker, { clientIp, fetchWithRetry } from "./index.js";

const originalFetch = globalThis.fetch;
const originalError = console.error;

afterEach(() => {
  globalThis.fetch = originalFetch;
  console.error = originalError;
});

function makeRequest(path, options = {}) {
  return {
    method: options.method || "GET",
    url: `https://football.example${path}`,
    headers: new Headers(options.headers || {}),
    cf: options.cf,
  };
}

function makeEnv(overrides = {}) {
  return {
    BACKEND_URL: "https://origin.example",
    BACKEND_SHARED_SECRET: "s3cret",
    API_RATE_LIMITER: { limit: async () => ({ success: true }) },
    ...overrides,
  };
}

test("clientIp prefers Cloudflare's value over a caller header", () => {
  const request = makeRequest("/api/v1/leagues", {
    headers: { "cf-connecting-ip": "1.2.3.4" },
    cf: { clientIp: "9.8.7.6" },
  });
  assert.equal(clientIp(request), "9.8.7.6");
  assert.equal(clientIp(makeRequest("/", { headers: { "cf-connecting-ip": "1.2.3.4" } })), "1.2.3.4");
});

test("fetchWithRetry retries network errors and then succeeds", async () => {
  let calls = 0;
  globalThis.fetch = async () => {
    calls += 1;
    if (calls < 3) throw new TypeError("network down");
    return new Response("ok", { status: 200 });
  };
  const response = await fetchWithRetry("https://origin.example/health", {});
  assert.equal(response.status, 200);
  assert.equal(calls, 3);
});

test("fetchWithRetry gives each retry a fresh timeout signal", async () => {
  const controller = new AbortController();
  let calls = 0;
  let secondSignal;
  globalThis.fetch = async (_target, init) => {
    calls += 1;
    if (calls === 1) {
      throw new DOMException("timed out", "TimeoutError");
    }
    secondSignal = init.signal;
    return new Response("ok", { status: 200 });
  };
  const response = await fetchWithRetry("https://origin.example/health", {
    signal: controller.signal,
  });
  assert.equal(response.status, 200);
  assert.equal(calls, 2);
  assert.notEqual(secondSignal, controller.signal);
  assert.equal(secondSignal.aborted, false);
});

test("fetchWithRetry retries gateway statuses", async () => {
  let calls = 0;
  globalThis.fetch = async () => {
    calls += 1;
    return new Response("", { status: calls < 2 ? 503 : 200 });
  };
  const response = await fetchWithRetry("https://origin.example/api/v1/leagues", {});
  assert.equal(response.status, 200);
  assert.equal(calls, 2);
});

test("fetchWithRetry gives up after three network failures", async () => {
  let calls = 0;
  globalThis.fetch = async () => {
    calls += 1;
    throw new TypeError("still down");
  };
  await assert.rejects(fetchWithRetry("https://origin.example/health", {}), TypeError);
  assert.equal(calls, 3);
});

test("fetch returns 502 when the origin is unreachable", async () => {
  console.error = () => {};
  globalThis.fetch = async () => {
    throw new TypeError("connection refused");
  };
  const response = await worker.fetch(makeRequest("/api/v1/leagues"), makeEnv());
  assert.equal(response.status, 502);
});

test("fetch fails closed when the rate-limit binding is missing", async () => {
  const response = await worker.fetch(
    makeRequest("/api/v1/leagues"),
    makeEnv({ API_RATE_LIMITER: undefined }),
  );
  assert.equal(response.status, 503);
});

test("local harness can opt out of the missing rate-limit binding", async () => {
  globalThis.fetch = async () => new Response("[]", { status: 200 });
  const response = await worker.fetch(
    makeRequest("/api/v1/leagues"),
    makeEnv({ API_RATE_LIMITER: undefined, ALLOW_NO_RATE_LIMITER: "1" }),
  );
  assert.equal(response.status, 200);
});

test("fetch returns 429 when the edge limiter denies the request", async () => {
  let limitedKey;
  const env = makeEnv({
    API_RATE_LIMITER: {
      limit: async ({ key }) => {
        limitedKey = key;
        return { success: false };
      },
    },
  });
  const response = await worker.fetch(
    makeRequest("/api/v1/leagues", { cf: { clientIp: "5.6.7.8" } }),
    env,
  );
  assert.equal(response.status, 429);
  assert.equal(response.headers.get("retry-after"), "60");
  assert.equal(limitedKey, "5.6.7.8");
});

test("fetch overwrites the backend client-IP header and injects the secret", async () => {
  let forwarded;
  globalThis.fetch = async (_target, init) => {
    forwarded = init.headers;
    return new Response("[]", { status: 200 });
  };
  const response = await worker.fetch(
    makeRequest("/api/v1/leagues", {
      headers: {
        "cf-connecting-ip": "1.1.1.1",
        "x-worker-client-ip": "2.2.2.2",
        "x-worker-secret": "client-guess",
        cookie: "session=stolen",
      },
      cf: { clientIp: "9.9.9.9" },
    }),
    makeEnv(),
  );
  assert.equal(response.status, 200);
  assert.equal(forwarded.get("x-worker-client-ip"), "9.9.9.9");
  assert.equal(forwarded.get("x-worker-secret"), "s3cret");
  assert.equal(forwarded.get("cookie"), null);
});

test("scheduled health check rejects non-2xx responses", async () => {
  globalThis.fetch = async () => new Response("down", { status: 503 });
  await assert.rejects(worker.scheduled({}, makeEnv()), /HTTP 503/);
});

test("scheduled health check accepts a healthy response", async () => {
  globalThis.fetch = async () => new Response("ok", { status: 200 });
  await assert.doesNotReject(worker.scheduled({}, makeEnv()));
});
