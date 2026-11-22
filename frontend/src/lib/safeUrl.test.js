import { describe, expect, it } from "vitest";
import { isValidChartName, safeHttpsUrl, safeImageUrl } from "./safeUrl.js";

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

describe("safeImageUrl", () => {
  it("allows same-origin paths and HTTPS logos", () => {
    expect(safeImageUrl("/logos/arsenal.png")).toBe("/logos/arsenal.png");
    expect(safeImageUrl("https://cdn.example.com/logo.png")).toBe(
      "https://cdn.example.com/logo.png",
    );
  });

  it("rejects executable schemes and protocol-relative paths", () => {
    expect(safeImageUrl("javascript:alert(1)")).toBeNull();
    expect(safeImageUrl("//evil.example.com/x.png")).toBeNull();
    expect(safeImageUrl("data:image/svg+xml,<svg/>")).toBeNull();
    expect(safeImageUrl(null)).toBeNull();
  });
});

describe("isValidChartName", () => {
  it("accepts only a plain PNG filename", () => {
    expect(isValidChartName("avg_goals.png")).toBe(true);
    expect(isValidChartName("../secret.png")).toBe(false);
    expect(isValidChartName("chart.svg")).toBe(false);
  });
});
