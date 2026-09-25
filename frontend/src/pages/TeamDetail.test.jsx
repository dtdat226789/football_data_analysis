import { render, screen, within } from "@testing-library/react";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import {
  leagueFixturesPayload,
  matchList,
  teamDetail,
  teamForm,
  teamStanding,
  teamStatsResponse,
} from "../test/fixtures.js";
import TeamDetail from "./TeamDetail.jsx";

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
  api.team.mockResolvedValue(teamDetail);
  api.teamForm.mockResolvedValue(teamForm);
  api.teamStandings.mockResolvedValue(teamStanding);
  api.teamMatches.mockResolvedValue({ total: 1, matches: [matchList.matches[0]] });
  api.teamStats.mockResolvedValue(teamStatsResponse);
  api.leagueFixtures.mockResolvedValue(leagueFixturesPayload);
};

function renderTeamDetail() {
  return render(
    <MemoryRouter initialEntries={["/teams/arsenal"]}>
      <Routes>
        <Route path="/teams/:slug" element={<TeamDetail />} />
      </Routes>
    </MemoryRouter>,
  );
}

describe("TeamDetail", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders the canonical identity header", async () => {
    renderTeamDetail();

    const heading = (await screen.findAllByRole("heading"))[0];
    expect(heading).toHaveTextContent("Arsenal");
    expect(heading.closest(".page-head")).toHaveTextContent("canonical: Arsenal · slug: arsenal");
  });

  it("renders the standings, form, recent matches, upcoming fixtures and seasons", async () => {
    renderTeamDetail();

    expect(await screen.findByText("Standings · 2024-2025")).toBeInTheDocument();
    expect(screen.getByText("22W-5D-3L")).toBeInTheDocument();
    expect(screen.getByText("70 : 20 (+50)")).toBeInTheDocument();
    expect(screen.getByText("71")).toBeInTheDocument();

    expect(screen.getByText("Recent form")).toBeInTheDocument();
    expect(screen.getAllByText("W").length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText("D").length).toBeGreaterThanOrEqual(1);

    expect(screen.getByText("Recent matches (1)")).toBeInTheDocument();
    expect(screen.getAllByText("2 – 1").length).toBeGreaterThanOrEqual(1);

    expect(screen.getByText("Upcoming · premier")).toBeInTheDocument();
    expect(api.leagueFixtures).toHaveBeenCalledWith("premier");

    const seasonsSection = screen.getByText("Seasons (2)").closest("section");
    expect(within(seasonsSection).getByText("2023-2024")).toBeInTheDocument();
    expect(within(seasonsSection).getByText("2024-2025")).toBeInTheDocument();
  });

  it("requests team data with the current league and season", async () => {
    renderTeamDetail();
    await screen.findByText("Standings · 2024-2025");

    expect(api.team).toHaveBeenCalledWith("arsenal");
    expect(api.teamForm).toHaveBeenLastCalledWith("arsenal", {
      league: "premier",
      season: "2024-2025",
      n: 8,
    });
    expect(api.teamStandings).toHaveBeenLastCalledWith("arsenal", {
      league: "premier",
      season: "2024-2025",
    });
    expect(api.teamMatches).toHaveBeenLastCalledWith("arsenal", {
      league: "premier",
      season: "2024-2025",
      limit: 10,
      offset: 0,
    });
    expect(api.teamStats).toHaveBeenLastCalledWith("arsenal", { league: "premier", view: "classic" });
  });

  it("renders the aggregated statistics section with charts", async () => {
    renderTeamDetail();

    const section = (await screen.findByRole("heading", { name: /Statistics · premier/ })).closest("section");

    expect(await within(section).findByText("53W-9D-14L")).toBeInTheDocument();
    expect(within(section).getByText("179 : 65")).toBeInTheDocument();
    expect(within(section).getByText("2.21 PPG")).toBeInTheDocument();
    expect(within(section).getAllByText("#1").length).toBeGreaterThanOrEqual(1);
    expect(within(section).getAllByText("2023-2024").length).toBeGreaterThanOrEqual(2);

    expect(within(section).getByText("Points per season")).toBeInTheDocument();
    expect(within(section).getByText("83 pts")).toBeInTheDocument();
    expect(within(section).getByText("League position per season (lower is better)")).toBeInTheDocument();
    expect(within(section).getByText("Win % by venue")).toBeInTheDocument();
    expect(within(section).getByText("78.9%")).toBeInTheDocument();
    expect(within(section).getByText("60.5%")).toBeInTheDocument();
  });
});