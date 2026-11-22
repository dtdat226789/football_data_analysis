import { renderHook, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { ApiError } from "../api/client.js";
import { currentRequestSignal } from "../lib/requestSignal.js";
import { apiCacheSize, clearApiCache, useApi } from "./useApi.js";

describe("useApi", () => {
  beforeEach(() => {
    clearApiCache();
  });

  it("transitions from loading to data", async () => {
    const { result } = renderHook(() => useApi(() => Promise.resolve(42), []));

    expect(result.current.loading).toBe(true);
    await waitFor(() => expect(result.current.loading).toBe(false));
    expect(result.current.data).toBe(42);
    expect(result.current.error).toBeNull();
  });

  it("captures rejected loaders as an error message string", async () => {
    const { result } = renderHook(() => useApi(() => Promise.reject(new Error("boom")), []));

    await waitFor(() => expect(result.current.loading).toBe(false));
    expect(result.current.data).toBeNull();
    expect(result.current.error).toBe("boom");
  });

  it("stays loading when the loader resolves to null (prerequisites not ready)", async () => {
    const { result } = renderHook(() => useApi(() => Promise.resolve(null), []));

    await new Promise((resolve) => setTimeout(resolve, 0));
    expect(result.current.loading).toBe(true);
    expect(result.current.data).toBeNull();
    expect(result.current.error).toBeNull();
  });

  it("leaves loading when deps flip to an unresolved prerequisite", async () => {
    const loader = vi.fn((ready) => (ready ? Promise.resolve("data") : Promise.resolve(null)));
    const { result, rerender } = renderHook(
      ({ ready }) => useApi(() => loader(ready), [ready]),
      { initialProps: { ready: true } },
    );

    await waitFor(() => expect(result.current.loading).toBe(false));
    expect(result.current.data).toBe("data");

    rerender({ ready: false });
    await new Promise((resolve) => setTimeout(resolve, 0));
    expect(result.current.loading).toBe(true);
    expect(result.current.data).toBeNull();
  });

  it("re-runs the loader when deps change", async () => {
    const loader = vi.fn((dep) => Promise.resolve(dep));
    const { result, rerender } = renderHook(
      ({ dep }) => useApi(() => loader(dep), [dep]),
      { initialProps: { dep: "a" } },
    );

    await waitFor(() => expect(result.current.data).toBe("a"));
    rerender({ dep: "b" });
    await waitFor(() => expect(result.current.data).toBe("b"));
    expect(loader).toHaveBeenCalledTimes(2);
  });

  it("ignores a stale response arriving after the deps already changed", async () => {
    let resolveFirst;
    const first = new Promise((resolve) => {
      resolveFirst = resolve;
    });
    const loader = vi.fn((dep) => (dep === "a" ? first : Promise.resolve(dep)));

    const { result, rerender } = renderHook(
      ({ dep }) => useApi(() => loader(dep), [dep]),
      { initialProps: { dep: "a" } },
    );

    await waitFor(() => expect(loader).toHaveBeenCalledTimes(1));
    rerender({ dep: "b" });
    await waitFor(() => expect(result.current.data).toBe("b"));

    resolveFirst("a");
    await new Promise((resolve) => setTimeout(resolve, 0));
    expect(result.current.data).toBe("b");
  });

  it("reports the status and a translated message for an API failure", async () => {
    const { result } = renderHook(() =>
      useApi(() => Promise.reject(new ApiError(404, "raw backend detail")), []),
    );

    await waitFor(() => expect(result.current.loading).toBe(false));
    expect(result.current.status).toBe(404);
    expect(result.current.error).toBe("That page or record could not be found.");
    expect(result.current.error).not.toContain("raw backend detail");
  });

  it("gives the loader an abort signal and aborts it on unmount", async () => {
    let seen;
    const { unmount } = renderHook(() =>
      useApi(() => {
        seen = currentRequestSignal();
        return new Promise(() => {});
      }, []),
    );

    expect(seen).toBeInstanceOf(AbortSignal);
    expect(seen.aborted).toBe(false);
    unmount();
    expect(seen.aborted).toBe(true);
  });

  it("bounds the response cache", async () => {
    const hooks = [];
    for (let i = 0; i < 110; i += 1) {
      hooks.push(
        renderHook(({ value }) => useApi(() => Promise.resolve(value), [value]), {
          initialProps: { value: i },
        }),
      );
    }

    await waitFor(() => expect(hooks[109].result.current.data).toBe(109));
    expect(apiCacheSize()).toBeLessThanOrEqual(100);
  });
});