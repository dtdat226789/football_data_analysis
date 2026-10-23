import { screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { renderPage } from "../test/render.jsx";
import MatchTable from "./MatchTable.jsx";

const rows = [
  { api_id: 1, match_date: "2025-01-18", home_team: "Arsenal", away_team: "Chelsea", home_score: 2, away_score: 1, league: "premier", league_name: "Premier League" },
  { api_id: 2, match_date: "2025-01-19", home_team: "Barcelona", away_team: "Real Madrid", home_score: 0, away_score: 0, league: "spain1", league_name: "La Liga" },
];

const ready = (matches, extra = {}) => ({ data: { matches, ...extra }, loading: false, error: null });

describe("MatchTable", () => {
  it("renders both rows with scores, team links and a detail link", () => {
    renderPage(<MatchTable state={ready(rows)} showLeague />);

    expect(screen.getAllByRole("row")).toHaveLength(3);
    expect(screen.getByText("2 – 1")).toBeInTheDocument();
    expect(screen.getAllByRole("link", { name: "view" }).map((l) => l.getAttribute("href"))).toEqual([
      "/match/1",
      "/match/2",
    ]);
    expect(within(screen.getByRole("table")).getByText("Premier League")).toBeInTheDocument();
  });

  it("hides the league column for a feed that is already scoped to one league", () => {
    renderPage(<MatchTable state={ready(rows)} />);

    const table = screen.getByRole("table");
    expect(within(table).queryByText("Premier League")).not.toBeInTheDocument();
    expect(within(table).getAllByRole("columnheader")).toHaveLength(5);
  });

  it("says something when there is nothing to show", () => {
    // The copy this replaced rendered a bare tbody, so an uncollected season left
    // a heading above an empty box with no explanation.
    renderPage(
      <MatchTable
        state={ready([])}
        showLeague
        emptyMessage="No finished matches recorded for 2024-2025."
      />,
    );

    const table = screen.getByRole("table");
    const message = within(table).getByText("No finished matches recorded for 2024-2025.");
    // Spans every column rather than sitting in one narrow cell.
    expect(message.closest("td")).toHaveAttribute("colspan", "6");
  });

  it("survives a payload with no matches key at all", () => {
    // A half-built payload used to throw during render here, and with no error
    // boundary above the table that blanked the page rather than the table.
    renderPage(<MatchTable state={{ data: { total: 0 }, loading: false, error: null }} />);

    expect(screen.getByText("No finished matches match the filters.")).toBeInTheDocument();
  });

  it("falls back to the slug when a row carries no league name", () => {
    renderPage(<MatchTable state={ready([{ ...rows[0], league_name: undefined }])} showLeague />);

    expect(screen.getByText("premier")).toBeInTheDocument();
  });

  it("skeletons exactly as many columns as the header will have", () => {
    const { container, unmount } = renderPage(<MatchTable state={{ data: null, loading: true, error: null }} showLeague />);

    // Six for the league-scoped header. Both copies of this table used to draw a
    // skeleton a column short of their own header.
    expect(container.querySelectorAll("table.data thead th")).toHaveLength(6);
    expect(container.querySelectorAll("table.data tbody tr:first-child td")).toHaveLength(6);
    unmount();

    // Five when the league column is gone, derived from the same `showLeague`.
    renderPage(<MatchTable state={ready(rows)} />);
    expect(screen.getAllByRole("columnheader")).toHaveLength(5);
  });

  it("shows the error instead of a skeleton once the request fails", () => {
    renderPage(<MatchTable state={{ data: null, loading: false, error: "boom" }} showLeague />);

    expect(screen.getByText("boom")).toBeInTheDocument();
    expect(document.querySelectorAll("table.data")).toHaveLength(0);
  });

  it("renders nothing before the request has resolved", () => {
    // No header on screen that would sit above an empty body for a beat.
    const { container } = renderPage(<MatchTable state={{ data: null, loading: false, error: null }} showLeague />);
    expect(container).toBeEmptyDOMElement();
  });
});