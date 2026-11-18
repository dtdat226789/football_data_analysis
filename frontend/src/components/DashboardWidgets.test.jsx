import { screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { KpiTile, LineTrend, MiniCompare, RankTable } from "./DashboardWidgets.jsx";
import { renderPage } from "../test/render.jsx";

describe("dashboard widgets", () => {
  it("shows a KPI value with its league rank", () => {
    renderPage(<KpiTile tile={{ key: "goalsPerGame", value: 2.14, rank: 3, rank_total: 20 }} />);
    expect(screen.getByText("Goals / game")).toBeInTheDocument();
    expect(screen.getByText("2.14")).toBeInTheDocument();
    expect(screen.getByText("#3 in league")).toBeInTheDocument();
  });

  it("uses a dash when a KPI has no value or rank", () => {
    renderPage(<KpiTile tile={{ key: "cleanSheetPct", value: null, rank: null, rank_total: 0 }} />);
    expect(screen.getByText("—")).toBeInTheDocument();
    expect(screen.getByText("no league rank")).toBeInTheDocument();
  });

  it("scales comparison bars against the largest value", () => {
    const games = [
      { date: "2025-01-01", opponent: "Alpha", goals_for: 3 },
      { date: "2025-01-08", opponent: "Beta", goals_for: 1 },
    ];
    renderPage(<MiniCompare games={games} metric="goals_for" titleKey="dash.goalsFor" />);
    const fills = /** @type {HTMLElement[]} */ ([...document.querySelectorAll(".dash-bar-fill")]);
    expect(fills.length).toBe(2);
    expect(fills[0].style.width).toBe("100%");
    expect(fills[1].style.width).toBe("33.33333333333333%");
  });

  it("highlights the selected rank row", () => {
    renderPage(
      <RankTable
        rows={[
          { label: "ARS", points: 74, is_selected: true },
          { label: "LIV", points: 84, is_selected: false },
        ]}
        columns={[
          { key: "label", labelKey: "kpi.table.team" },
          { key: "points", labelKey: "table.pts", numeric: true },
        ]}
      />,
    );
    expect(screen.getByRole("columnheader", { name: "Team" })).toBeInTheDocument();
    expect(document.querySelector("tr.is-selected")?.textContent).toContain("ARS");
  });

  it("renders a trend line and an empty state", () => {
    const { unmount } = renderPage(
      <LineTrend data={[{ season: "2023-2024", value: 2 }, { season: "2024-2025", value: 1 }]} label="Goals" />,
    );
    expect(screen.getByRole("img", { name: "Goals by season" })).toBeInTheDocument();
    unmount();
    renderPage(<LineTrend data={[]} label="Goals" />);
    expect(screen.getByText("No season history available.")).toBeInTheDocument();
  });
});
