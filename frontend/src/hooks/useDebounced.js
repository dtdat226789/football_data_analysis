import { useEffect, useState } from "react";

/**
 * Mirror `value` after it has stopped changing for `delay` ms.
 *
 * Used to keep a keystroke-driven server search from firing one request per
 * character; the input stays controlled and responsive while the request
 * settles.
 */
export function useDebounced(value, delay = 250) {
  const [settled, setSettled] = useState(value);

  useEffect(() => {
    if (delay <= 0) return undefined;
    const timer = setTimeout(() => setSettled(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  // With no delay there is nothing to wait for, so read the live value instead
  // of copying it into state from the effect.
  return delay <= 0 ? value : settled;
}
