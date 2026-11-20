const RETRY_STATUSES = new Set([502, 503, 504]);
const RETRY_BUDGET_MS = 6_000;
const RETRY_DELAY_MS = 500;
const MAX_ATTEMPTS = 3;
const REQUEST_TIMEOUT_MS = 20_000;
const ALLOWED_METHODS = new Set(["GET", "HEAD"]);

const SECURITY_HEADERS = {
  "Content-Security-Policy":
    "default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; " +
    "form-action 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; " +
    "img-src 'self' data: https:; connect-src 'self'; font-src 'self'; manifest-src 'self'",
  "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "DENY",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
};

function harden(response) {
  const headers = new Headers(response.headers);
  for (const [name, value] of Object.entries(SECURITY_HEADERS)) {
    headers.set(name, value);
  }
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}

function methodNotAllowed() {
  return harden(
    new Response("Method Not Allowed", {
      status: 405,
      headers: { Allow: "GET, HEAD" },
    }),
  );
}

function rateLimited() {
  return harden(
    new Response("Too Many Requests", {
      status: 429,
      headers: { "Retry-After": "60" },
    }),
  );
}

async function fetchWithRetry(target, init) {
  const start = Date.now();
  let response;

  for (let attempt = 0; attempt < MAX_ATTEMPTS; attempt += 1) {
    response = await fetch(target, init);
    if (!RETRY_STATUSES.has(response.status)) {
      return response;
    }
    if (
      attempt === MAX_ATTEMPTS - 1 ||
      Date.now() - start + RETRY_DELAY_MS >= RETRY_BUDGET_MS
    ) {
      return response;
    }
    await new Promise((resolve) => setTimeout(resolve, RETRY_DELAY_MS));
  }

  return response;
}

/**
 * Keep redirects on the Worker origin instead of leaking the request (and the
 * backend secret) to a cross-origin Location. FastAPI's trailing-slash
 * redirects are the common case, so the path is preserved for the browser.
 */
function rewriteRedirect(response, target) {
  if (![301, 302, 303, 307, 308].includes(response.status)) {
    return response;
  }
  const location = response.headers.get("location");
  if (!location) {
    return response;
  }
  const redirected = new URL(location, target);
  if (redirected.origin !== target.origin) {
    return harden(new Response("Bad Gateway", { status: 502 }));
  }
  const headers = new Headers(response.headers);
  headers.set("location", `${redirected.pathname}${redirected.search}`);
  return harden(
    new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers,
    }),
  );
}

export default {
  async fetch(request, env) {
    if (!ALLOWED_METHODS.has(request.method)) {
      return methodNotAllowed();
    }

    const url = new URL(request.url);
    const isApi =
      url.pathname === "/health" ||
      url.pathname === "/api" ||
      url.pathname.startsWith("/api/");

    // Edge limit for /api/* only: static assets and SPA navigation are free.
    // The binding is configured in wrangler.jsonc; skip the check if a local
    // harness supplies no binding so the worker stays testable in isolation.
    if (isApi && env.API_RATE_LIMITER) {
      const key = request.headers.get("cf-connecting-ip") || "unknown";
      const { success } = await env.API_RATE_LIMITER.limit({ key });
      if (!success) {
        return rateLimited();
      }
    }

    if (!isApi) {
      return harden(await env.ASSETS.fetch(request));
    }

    const target = new URL(url.pathname + url.search, env.BACKEND_URL);
    const headers = new Headers(request.headers);
    headers.delete("host");
    headers.delete("cookie");
    headers.delete("authorization");
    // Never trust a client-supplied secret; inject the configured one after
    // stripping the header so a direct request cannot pass itself off as the
    // Worker.
    headers.delete("x-worker-secret");
    if (env.BACKEND_SHARED_SECRET) {
      headers.set("x-worker-secret", env.BACKEND_SHARED_SECRET);
    }

    const response = await fetchWithRetry(target, {
      method: request.method,
      headers,
      redirect: "manual",
      signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
    });

    return rewriteRedirect(harden(response), target);
  },

  async scheduled(controller, env, ctx) {
    ctx.waitUntil(
      fetch(new URL("/health", env.BACKEND_URL), {
        method: "GET",
        redirect: "manual",
        signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
      }).catch(() => {}),
    );
  },
};
