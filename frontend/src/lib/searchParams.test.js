import { describe, expect, it } from "vitest";

import { intParam, isIsoDay, pageOffset } from "./searchParams.js";

describe("isIsoDay", () => {
  it("accepts a plain calendar day and rejects everything else", () => {
    expect(isIsoDay("2026-02-01")).toBe(true);
    expect(isIsoDay("")).toBe(false);
    expect(isIsoDay(null)).toBe(false);
    expect(isIsoDay(undefined)).toBe(false);
    expect(isIsoDay("2026-2-1")).toBe(false);
    expect(isIsoDay("2026-02-01T16:00")).toBe(false);
    expect(isIsoDay("yesterday")).toBe(false);
  });
});

describe("intParam", () => {
  const params = (query) => new URLSearchParams(query);

  it("reads a plain non-negative integer", () => {
    expect(intParam(params("offset=50"), "offset")).toBe(50);
    expect(intParam(params("offset=0"), "offset")).toBe(0);
  });

  it("falls back rather than yielding NaN", () => {
    // NaN used to be stringified into the query and rejected by FastAPI with a
    // 422, which is a worse answer than page one for a mistyped bookmark.
    for (const raw of ["abc", "", "  ", "-5", "+5", "1e400", "NaN", "Infinity", "99999999999999999999"]) {
      expect(intParam(params(`offset=${raw}`), "offset")).toBe(0);
    }
    expect(intParam(params(""), "offset")).toBe(0);
    expect(intParam(params("offset=abc"), "offset", 7)).toBe(7);
  });

  it("does not salvage the leading digits of a padded value", () => {
    // `parseInt("50px")` is 50, which would page a list the link never asked for.
    expect(intParam(params("offset=50px"), "offset")).toBe(0);
    expect(intParam(params("offset=0.5"), "offset")).toBe(0);
  });
});

describe("pageOffset", () => {
  it("drops page one rather than writing a zero offset", () => {
    // Page one is the absence of an offset, so `?offset=0` is noise in a shared
    // link and in the browser history.
    expect(pageOffset(0)).toBe("");
    expect(pageOffset(-50)).toBe("");
    expect(pageOffset(NaN)).toBe("");
    expect(pageOffset(50)).toBe(50);
  });
});