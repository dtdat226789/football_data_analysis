import { useCallback, useEffect, useRef, useState } from "react";

import { useI18n } from "../i18n/I18nProvider.jsx";
import { withRequestSignal } from "../lib/requestSignal.js";

const DEFAULT_TTL = 5 * 60 * 1000;
const MAX_CACHE_ENTRIES = 100;

const cache = new Map();

function trimCache() {
  if (cache.size <= MAX_CACHE_ENTRIES) return;
  const resolved = [...cache.entries()]
    .filter(([, entry]) => !entry.promise)
    .sort((a, b) => a[1].at - b[1].at);
  for (const [key] of resolved) {
    if (cache.size <= MAX_CACHE_ENTRIES) break;
    cache.delete(key);
  }
  while (cache.size > MAX_CACHE_ENTRIES) {
    cache.delete(cache.keys().next().value);
  }
}

async function cachedLoad(key, loader, ttl, signal) {
  const hit = cache.get(key);
  if (hit) {
    if (hit.promise) return hit.promise;
    if (Date.now() - hit.at < ttl) return hit.value;
  }
  let pending;
  try {
    pending = withRequestSignal(signal, () => Promise.resolve(loader()));
  } catch (error) {
    return Promise.reject(error);
  }
  const promise = pending.then(
    (value) => {
      if (value === null) {
        cache.delete(key);
      } else {
        cache.set(key, { value, at: Date.now() });
        trimCache();
      }
      return value;
    },
    (error) => {
      cache.delete(key);
      throw error;
    },
  );
  cache.set(key, { promise });
  return promise;
}

function keyFor(source, deps) {
  let serialized;
  try {
    serialized = JSON.stringify(deps.map((d) => (typeof d === "function" ? `fn:${d.length}` : d)));
  } catch {
    serialized = `len:${deps.length}`;
  }
  return `${source}\u0001${serialized}`;
}

export function clearApiCache() {
  cache.clear();
}

export function apiCacheSize() {
  return cache.size;
}

const ERROR_STATUSES = new Set([0, 400, 403, 404, 422, 429, 499, 500, 502, 503, 504]);

function errorText(t, status, message) {
  if (status !== null && ERROR_STATUSES.has(status)) {
    const key = `api.error.${status}`;
    const translated = t(key);
    if (translated !== key) return translated;
  }
  return message || t("common.error");
}

export function useApi(loader, deps = [], { ttl = DEFAULT_TTL } = {}) {
  const { t } = useI18n();
  const [attempt, setAttempt] = useState(0);
  const seq = useRef(0);
  const reload = useCallback(() => setAttempt((n) => n + 1), []);

  const tracked = [...deps, attempt];
  const key = typeof loader === "function" ? keyFor(loader.toString(), tracked) : null;

  const [result, setResult] = useState({
    key: null,
    data: null,
    loading: true,
    error: null,
    status: null,
  });

  useEffect(() => {
    if (key === null) return undefined;
    const id = ++seq.current;
    const controller = new AbortController();
    cachedLoad(key, loader, ttl, controller.signal).then(
      (d) => {
        if (seq.current !== id) return;
        if (d === null) {
          setResult({ key, data: null, loading: true, error: null, status: null });
          return;
        }
        setResult({ key, data: d, loading: false, error: null, status: null });
      },
      (e) => {
        if (seq.current === id) {
          const status = e?.status ?? null;
          setResult({
            key,
            data: null,
            loading: false,
            error: errorText(t, status, e?.message),
            status,
          });
        }
      },
    );
    return () => {
      seq.current += 1;
      controller.abort();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [key]);

  if (typeof loader !== "function") {
    return { data: null, loading: true, error: null, status: null, reload };
  }

  const settled = result.key === key;
  return {
    data: result.data,
    error: settled ? result.error : null,
    status: settled ? result.status : null,
    loading: !settled || result.loading,
    reload,
  };
}
