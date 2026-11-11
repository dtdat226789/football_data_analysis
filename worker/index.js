const RETRY_STATUSES = new Set([502, 503, 504]);
const RETRY_BUDGET_MS = 25_000;
const RETRY_DELAY_MS = 3_000;

async function fetchWithRetry(target, init) {
  const start = Date.now();
  let response;

  for (;;) {
    response = await fetch(target, init);
    if (!RETRY_STATUSES.has(response.status)) {
      return response;
    }
    if (Date.now() - start + RETRY_DELAY_MS >= RETRY_BUDGET_MS) {
      return response;
    }
    await new Promise((resolve) => setTimeout(resolve, RETRY_DELAY_MS));
  }
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const isApi =
      url.pathname === "/health" ||
      url.pathname === "/api" ||
      url.pathname.startsWith("/api/");

    if (!isApi) {
      return env.ASSETS.fetch(request);
    }

    const target = new URL(url.pathname + url.search, env.BACKEND_URL);
    const headers = new Headers(request.headers);
    headers.delete("host");

    return fetchWithRetry(target, {
      method: request.method,
      headers,
      redirect: "follow",
    });
  },

  async scheduled(controller, env, ctx) {
    ctx.waitUntil(
      fetch(new URL("/health", env.BACKEND_URL), { method: "GET" }).catch(
        () => {},
      ),
    );
  },
};
