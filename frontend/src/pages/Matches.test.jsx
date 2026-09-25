import { fireEvent, screen, waitFor, within } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import { leagues, upcomingFixtures } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import Matches from "./Matches.jsx";

vi.mock("../api/client.js", () => {
  const names = [
    "health", "meta", "listLeagues", "league", "seasons", "standings",
    "matches", "match", "matchesRecent", "dashboard", "fixtures", "leagueFixtures",
    "teams", "team", "teamMatches", "teamForm", "teamStandings", "teamStats",
    "analysis", "analysisModule",
  ];
  const stub = {};
  for (const name of names) stub[name] = vi.fn();
  stub.chartUrl = (_l, _c) => `/api/v1/analysis/${_l}/charts/${_c}`;
  return { api: stub };
});

const recentMatches = {
  count: 2,
  total: 2,
  limit: 50,
  offset: 0,
  matches: [
    {
      api_id: 1001,
      match_date: "2025-01-18",
      home_team: "Arsenal",
      away_team: "Chelsea",
      home_score: 2,
      away_score: 1,
      league: "premier",
    },
    {
      api_id: 1002,
      match_date: "2025-01-19",
      home_team: "Barcelona",
      away_team: "Real Madrid",
      home_score: 0,
      away_score: 0,
      league: "spain1",
    },
  ],
};

const seed = () => {
  api.listLeagues.mockResolvedValue(leagues);
  api.fixtures.mockResolvedValue(upcomingFixtures);
  api.matchesRecent.mockResolvedValue(recentMatches);
};

describe("Matches", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders upcoming top picks with prediction chips and a recent results table", async () => {
    renderPage(<Matches />);

    expect(await screen.findByRole("heading", { name: "Matches" })).toBeInTheDocument();

    const upcoming = await screen.findByRole("heading", { name: /Upcoming/ });
    expect(upcoming.closest("section").querySelector(".badge")).toHaveTextContent("2");
    expect(screen.getAllByText("Arsenal").length).toBeGreaterThanOrEqual(1);
    expect(screen.getByText("58%")).toBeInTheDocument();
    // prediction meta line surfaces model confidence + data through
    expect(screen.getByText(/conf 58%/)).toBeInTheDocument();
    expect(screen.getAllByText(/as of 2026-01-29/).length).toBeGreaterThanOrEqual(1);

    const recent = screen.getByRole("heading", { name: /Recent/ });
    expect(recent.closest("section").querySelector(".badge")).toHaveTextContent("2");
    const table = within(recent.closest("section"));
    expect(table.getAllByRole("row")).toHaveLength(3);
    expect(table.getAllByRole("link", { name: "view" })[0]).toHaveAttribute("href", "/match/1001");
    expect(screen.getAllByText("2 – 1").length).toBeGreaterThanOrEqual(1);
  });

  it("refetches fixtures and results when a league is picked", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    fireEvent.change(screen.getByLabelText("League"), { target: { value: "spain1" } });

    await waitFor(() =>
      expect(api.fixtures).toHaveBeenLastCalledWith({ league: "spain1", sort: "confidence", limit: 50 }),
    );
    await waitFor(() =>
      expect(api.matchesRecent).toHaveBeenLastCalledWith(
        expect.objectContaining({ league: "spain1", offset: 0 }),
      ),
    );
  });

  it("adds and resets a from-date filter on recent results", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    expect(api.matchesRecent).toHaveBeenCalledWith(
      expect.objectContaining({ from_date: undefined, to_date: undefined, offset: 0 }),
    );

    fireEvent.change(screen.getByLabelText("From date"), { target: { value: "2025-01-18" } });
    await waitFor(() =>
      expect(api.matchesRecent).toHaveBeenLastCalledWith(
        expect.objectContaining({ from_date: "2025-01-18", to_date: undefined }),
      ),
    );

    fireEvent.click(screen.getByRole("button", { name: "Reset dates" }));
    await waitFor(() => expect(screen.getByLabelText("From date")).toHaveValue(""));
    expect(screen.queryByRole("button", { name: "Reset dates" })).not.toBeInTheDocument();
  });

  it("applies a 14-day preset to recent results", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    fireEvent.click(screen.getByRole("button", { name: "14d" }));

    await waitFor(() =>
      expect(api.matchesRecent).toHaveBeenLastCalledWith(
        expect.objectContaining({ from_date: expect.stringMatching(/^\d{4}-\d{2}-\d{2}$/), to_date: undefined }),
      ),
    );
    expect(screen.getByRole("button", { name: "Reset dates" })).toBeInTheDocument();
  });

  it("paginates recent results with offset reset on page size change", async () => {
    api.matchesRecent.mockImplementation((params = {}) => {
      const size = params.limit || 50;
      const offset = params.offset || 0;
      const total = 320;
      const all = Array.from({ length: total }, (_, i) => ({
        api_id: 1000 + i,
        match_date: "2025-01-18",
        home_team: `Home ${i}`,
        away_team: `Away ${i}`,
        home_score: 1,
        away_score: 0,
        league: "premier",
      }));
      const matches = all.slice(offset, offset + size);
      return { count: matches.length, total, limit: size, offset, matches };
    });
    renderPage(<Matches />);

    expect(await screen.findByText("1–50 of 320")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "‹ Prev" })).toBeDisabled();
    expect(screen.getByRole("button", { name: "Next ›" })).not.toBeDisabled();

    fireEvent.click(screen.getByRole("button", { name: "Next ›" }));
    expect(await screen.findByText("51–100 of 320")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "‹ Prev" })).not.toBeDisabled();

    fireEvent.change(screen.getByLabelText("Page size"), { target: { value: "20" } });
    await waitFor(() =>
      expect(api.matchesRecent).toHaveBeenLastCalledWith(
        expect.objectContaining({ offset: 0, limit: 20 }),
      ),
    );
  });

  it("shows an empty state when no fixtures exist", async () => {
    api.fixtures.mockResolvedValue({ count: 0, total: 0, matches: [] });
    renderPage(<Matches />);

    await screen.findByRole("heading", { name: /Upcoming/ });
    expect(screen.getByText(/No upcoming fixtures/)).toBeInTheDocument();
  });
});