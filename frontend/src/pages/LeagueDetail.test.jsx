import { fireEvent, screen, waitFor } from "@testing-library/react";
import { Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import {
  analysisBundle,
  leagueDetail,
  leagueFixturesPayload,
  matchList,
  standingsClassic,
} from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import LeagueDetail from "./LeagueDetail.jsx";

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

const seed = () => {
  api.league.mockResolvedValue(leagueDetail);
  api.standings.mockResolvedValue(standingsClassic);
  api.matches.mockResolvedValue(matchList);
  api.leagueFixtures.mockResolvedValue(leagueFixturesPayload);
  api.analysis.mockResolvedValue(analysisBundle);
};

const renderDetail = (route = "/leagues/premier") =>
  renderPage(
    <Routes>
      <Route path="/leagues/:slug" element={<LeagueDetail />} />
    </Routes>,
    { route },
  );

describe("LeagueDetail", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders the header and the standings tab by default with the latest season", async () => {
    renderDetail();

    expect(await screen.findByRole("heading", { name: "Premier League" })).toBeInTheDocument();
    expect(screen.getByText(/round-robin/)).toBeInTheDocument();

    // The table shell mounts before its rows resolve, so wait for the content.
    await screen.findAllByText("Arsenal");
    expect(api.standings).toHaveBeenCalledWith("premier", { season: "2024-2025", view: "classic" });
  });

  it("honours a season supplied in the URL", async () => {
    renderDetail("/leagues/premier?season=2023-2024");

    await screen.findByRole("table");
    expect(api.standings).toHaveBeenLastCalledWith("premier", { season: "2023-2024", view: "classic" });
    expect(screen.getByLabelText("Season")).toHaveValue("2023-2024");
  });

  it("switches the standings view and updates the URL", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Luck" }));

    await waitFor(() =>
      expect(api.standings).toHaveBeenLastCalledWith("premier", { season: "2024-2025", view: "luck" }),
    );
  });

  it("switches to the analysis tab", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Analysis" }));

    expect(await screen.findByText("Home advantage is strong")).toBeInTheDocument();
    expect(screen.getByText("380")).toBeInTheDocument();
    expect(screen.getByText("2.80")).toBeInTheDocument();
  });

  it("shows upcoming fixtures with predictions and recent results on the matches tab", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Matches" }));

    expect(await screen.findByRole("heading", { name: /Upcoming · 2024-2025/ })).toBeInTheDocument();
    expect(screen.getAllByText("Arsenal").length).toBeGreaterThanOrEqual(1);
    expect(screen.getByText("58%")).toBeInTheDocument();
    expect(api.leagueFixtures).toHaveBeenCalledWith("premier");

    expect(screen.getByRole("heading", { name: /Recent · 2024-2025/ })).toBeInTheDocument();
    expect(screen.getAllByRole("link", { name: "view" }).length).toBeGreaterThanOrEqual(1);
  });

  it("lists seasons from the details payload", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Seasons" }));

    expect(await screen.findByText("in_progress")).toBeInTheDocument();
    expect(screen.getAllByText("2023-2024").length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText("2025-2026").length).toBeGreaterThanOrEqual(1);
  });
});