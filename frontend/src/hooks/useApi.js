import { useEffect, useRef, useState } from "react";

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
  const seq = useRef(0);

  useEffect(() => {
    if (typeof loader !== "function") return;
    const id = ++seq.current;
    setLoading(true);
    setError(null);
    cachedLoad(keyFor(loader.toString(), deps), loader, ttl).then(
      (d) => {
        if (seq.current === id) {
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
  }, deps);

  return { data, loading, error };
}