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
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  // Bumped by `reload`. It joins the dep list and the cache key, so a retry is a
  // genuinely new request rather than the cached failure coming straight back.
  const [attempt, setAttempt] = useState(0);
  const seq = useRef(0);
  const reload = useCallback(() => setAttempt((n) => n + 1), []);

  // The attempt counter has to sit inside the effect's dep list, so the key and
  // the list are built from the same array.
  const tracked = [...deps, attempt];

  useEffect(() => {
    if (typeof loader !== "function") return;
    const id = ++seq.current;
    setLoading(true);
    setError(null);
    cachedLoad(keyFor(loader.toString(), tracked), loader, ttl).then(
      (d) => {
        if (seq.current === id) {
          // A loader may resolve null to mean "a prerequisite is not ready yet"
          // rather than "there is no data" — a route param that has not arrived,
          // or a filter that has not been chosen. That keeps the skeleton up
          // instead of flashing an empty state, and the deps that decide it are
          // the caller's to change.
          if (d === null) {
            setLoading(true);
            setData(null);
            setError(null);
            return;
          }
          setData(d);
          setLoading(false);
        }
      },
      (e) => {
        if (seq.current === id) {
          setError(e.message);
          setLoading(false);
        }
      },
    );
    return () => {
      seq.current += 1;
    };
    // `tracked` is `deps` plus the reload counter, and the effect must re-run on
    // exactly that list. The lint rule cannot check it: the array is built in the
    // hook body rather than written here, so it reads as a non-literal dep list.
    // `loader` and `ttl` are deliberately absent — `loader` is a fresh closure on
    // every render, so listing it would fetch forever; `ttl` is a constant for
    // every call site.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, tracked);

  return { data, loading, error, reload };
}