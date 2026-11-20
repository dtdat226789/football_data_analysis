import { describe, expect, it } from "vitest";
import { safeHttpsUrl } from "./safeUrl.js";

describe("safeHttpsUrl", () => {
  it("keeps ordinary HTTPS links", () => {
    expect(safeHttpsUrl("https://football-charts.com/match")).toBe(
      "https://football-charts.com/match",
    );
  });

  it("rejects executable and downgrade schemes", () => {
    expect(safeHttpsUrl("javascript:alert(1)")).toBeNull();
    expect(safeHttpsUrl("data:text/html,<script>alert(1)</script>")).toBeNull();
    expect(safeHttpsUrl("http://football-charts.com/match")).toBeNull();
  });

  it("rejects malformed and empty values", () => {
    expect(safeHttpsUrl("")).toBeNull();
    expect(safeHttpsUrl("not a URL")).toBeNull();
    expect(safeHttpsUrl(null)).toBeNull();
  });
});
