import { useEffect, useRef, useState } from "react";

export function useApi(loader, deps = []) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const seq = useRef(0);

  useEffect(() => {
    if (typeof loader !== "function") return;
    const id = ++seq.current;
    setLoading(true);
    setError(null);
    Promise.resolve(loader())
      .then((d) => {
        if (seq.current === id) {
          setData(d);
          setLoading(false);
        }
      })
      .catch((e) => {
        if (seq.current === id) {
          setError(e.message);
          setLoading(false);
        }
      });
    return () => {
      seq.current += 1;
    };
  }, deps);

  return { data, loading, error };
}