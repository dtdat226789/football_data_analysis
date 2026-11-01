import { useCallback, useEffect, useRef, useState } from "react";

const DEFAULT_TTL = 5 * 60 * 1000; // ms

/** key (loader source) -> { promise } while in flight, or { value, at } once resolved. */
const cache = new Map();

async function cachedLoad(key, loader, ttl) {
  const hit = cache.get(key);
  if (hit) {
    if (hit.promise) return hit.promise;
    if (Date.now() - hit.at < ttl) return hit.value;
  }
  const promise = Promise.resolve()
    .then(loader)
    .then(
      (value) => {
        if (value === null) {
          cache.delete(key);
        } else {
          cache.set(key, { value, at: Date.now() });
        }
        return value;
      },
      (err) => {
        cache.delete(key);
        throw err;
      },
    );
  cache.set(key, { promise });
  return promise;
}

/** Stable cache key: loader source + serialized deps (deps vary per params). */
function keyFor(source, deps) {
  let serialized;
  try {
    serialized = JSON.stringify(deps.map((d) => (typeof d === "function" ? `fn:${d.length}` : d)));
  } catch {
    serialized = `len:${deps.length}`;
  }
  return `${source}\u0001${serialized}`;
}

/** Drop all cached responses (used between tests and after upgrades). */
export function clearApiCache() {
  cache.clear();
}

/**
 * Async hook with an in-memory promise cache keyed by the loader source and
 * its deps. Identical loader calls within the TTL share a single fetch and
 * resolve instantly on remounts or when returning to previously seen params.
 */
export function useApi(loader, deps = [], { ttl = DEFAULT_TTL } = {}) {
  // Bumped by `reload`. It joins the dep list and the cache key, so a retry is a
  // genuinely new request rather than the cached failure coming straight back.
  const [attempt, setAttempt] = useState(0);
  const seq = useRef(0);
  const reload = useCallback(() => setAttempt((n) => n + 1), []);

  // The attempt counter has to sit inside the request key, so the key and the
  // deps it serializes come from the same array.
  const tracked = [...deps, attempt];
  const key = typeof loader === "function" ? keyFor(loader.toString(), tracked) : null;

  // One result per request key. Comparing it with the current key during render
  // is how the hook knows a request is still pending: a key that has not settled
  // yet reads as loading before the effect even fires. Its data is kept so a
  // refetch does not unmount the caller's filters, matching what the old
  // `setLoading(true)`-in-an-effect implementation did.
  const [result, setResult] = useState({ key: null, data: null, loading: true, error: null });

  useEffect(() => {
    if (key === null) return;
    const id = ++seq.current;
    cachedLoad(key, loader, ttl).then(
      (d) => {
        if (seq.current !== id) return;
        // A loader may resolve null to mean "a prerequisite is not ready yet"
        // rather than "there is no data" — a route param that has not arrived,
        // or a filter that has not been chosen. That keeps the skeleton up
        // instead of flashing an empty state, and the deps that decide it are
        // the caller's to change.
        if (d === null) {
          setResult({ key, data: null, loading: true, error: null });
          return;
        }
        setResult({ key, data: d, loading: false, error: null });
      },
      (e) => {
        if (seq.current === id) {
          setResult({ key, data: null, loading: false, error: e.message });
        }
      },
    );
    return () => {
      seq.current += 1;
    };
    // `key` is the loader source plus its serialized deps, so it changes exactly
    // when the request should. `loader` and `ttl` are deliberately absent —
    // `loader` is a fresh closure on every render, so listing it would fetch
    // forever; `ttl` is a constant for every call site.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [key]);

  if (typeof loader !== "function") {
    return { data: null, loading: true, error: null, reload };
  }

  const settled = result.key === key;
  return {
    data: result.data,
    error: settled ? result.error : null,
    loading: !settled || result.loading,
    reload,
  };
}