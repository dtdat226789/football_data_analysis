import { useCallback } from "react";
import { useSearchParams } from "react-router-dom";

/** A plain `YYYY-MM-DD` — the only date shape the API and `<input type="date">` speak. */
const ISO_DAY = /^\d{4}-\d{2}-\d{2}$/;

export function isIsoDay(value) {
  return ISO_DAY.test(value ?? "");
}

/** A plain run of digits — `1e400` and `50px` are not integers, whatever `parseInt` thinks. */
const UNSIGNED_INT = /^\d+$/;

/**
 * A non-negative integer search param, or `fallback` when it is not one.
 *
 * `?offset=abc` used to be coerced with `Number(...)` into `NaN`, which the API
 * client stringified into `"NaN"` and FastAPI answered with a 422 — and because
 * `NaN + size >= total` is false, the pager was then disabled in one direction
 * for the rest of the session. A value that is not a plain non-negative integer
 * is treated as absent, so a hand-edited or truncated URL degrades to page one
 * instead of breaking the control that read it.
 */
export function intParam(params, key, fallback = 0) {
  const raw = params.get(key);
  if (raw === null || !UNSIGNED_INT.test(raw)) return fallback;
  const value = Number(raw);
  return Number.isSafeInteger(value) ? value : fallback;
}

/**
 * The query value for an offset: page one is the absence of an offset, so it is
 * dropped rather than written as `?offset=0`.
 */
export function pageOffset(offset) {
  return Number.isInteger(offset) && offset > 0 ? offset : "";
}

/**
 * One patch implementation for every filter that lives in the query string.
 *
 * Each list used to carry its own copy and they disagreed on a single rule:
 * three deleted an empty value while the upcoming list wrote `uoffset=0`. Two
 * different URLs then meant the same state, so a shared link or a back step
 * landed somewhere the reader did not expect — on this page "go to page 1"
 * emitted `/matches` for the recent table and `/matches?uoffset=0` for the
 * upcoming one. Empty now means "remove the param" everywhere, and `pageOffset`
 * is how a caller says "rewind to page one".
 *
 * @returns {[URLSearchParams, (updates: Record<string, string | number | null | undefined>) => void]}
 *   The current params and a stable patch function for them.
 */
export function useParamsPatch() {
  const [searchParams, setSearchParams] = useSearchParams();
  const patch = useCallback(
    (updates) => {
      const next = new URLSearchParams(searchParams);
      for (const [key, value] of Object.entries(updates)) {
        if (value === "" || value === null || value === undefined) next.delete(key);
        else next.set(key, String(value));
      }
      setSearchParams(next);
    },
    [searchParams, setSearchParams],
  );
  return [searchParams, patch];
}