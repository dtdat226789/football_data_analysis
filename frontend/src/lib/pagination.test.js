import { describe, expect, it } from "vitest";
import { pageLabel, pageRange } from "./pagination.js";

describe("pageRange", () => {
  it("reports a one-based range for a first page", () => {
    expect(pageRange(50, 0, 320)).toEqual({ start: 1, end: 50, total: 320 });
  });

  it("reports a mid-page range", () => {
    expect(pageRange(50, 50, 320)).toEqual({ start: 51, end: 100, total: 320 });
  });

  it("clamps a partial last page to the total", () => {
    expect(pageRange(50, 300, 320)).toEqual({ start: 301, end: 320, total: 320 });
  });

  it("returns an empty range when there is nothing to describe", () => {
    expect(pageRange(50, 0, 0)).toEqual({ start: 0, end: 0, total: 0 });
  });

  it("returns null past the last page, where a clamp would repeat the last row", () => {
    // Clamping here would read "150–150 of 150" above an empty table.
    expect(pageRange(50, 150, 150)).toBeNull();
    expect(pageRange(50, 5000, 150)).toBeNull();
  });
});

describe("pageLabel", () => {
  it("renders a readable range", () => {
    expect(pageLabel(50, 0, 320)).toBe("1–50 of 320");
  });

  it("says so when there is nothing on the page", () => {
    expect(pageLabel(50, 0, 0)).toBe("0 results");
  });

  it("says so when the offset is past the end", () => {
    expect(pageLabel(50, 150, 150)).toBe("no rows on this page");
  });

  it("accepts host wording for both empty captions", () => {
    expect(pageLabel(50, 0, 0, { empty: "0 matches" })).toBe("0 matches");
    expect(pageLabel(50, 900, 150, { past: "past the end" })).toBe("past the end");
  });
});
