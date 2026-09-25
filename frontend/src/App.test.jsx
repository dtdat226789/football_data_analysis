import { fireEvent, render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "./api/client.js";
import App from "./App.jsx";
import {
  dashboard,
  leagueDetail,
  leagueFixturesPayload,
  leagues,
  matchDetail,
  matchList,
  recentMatches,
  standingsClassic,
  teamDetail,
  teamForm,
  teamStanding,
  teamsResponse,
  upcomingFixtures,
} from "./test/fixtures.js";

vi.mock("./api/client.js", () => {
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
  api.listLeagues.mockResolvedValue(leagues);
  api.meta.mockResolvedValue({ default_league: "premier" });
  api.league.mockResolvedValue(leagueDetail);
  api.standings.mockResolvedValue(standingsClassic);
  api.matches.mockResolvedValue(matchList);
  api.matchesRecent.mockResolvedValue(recentMatches);
  api.match.mockResolvedValue(matchDetail);
  api.dashboard.mockResolvedValue(dashboard);
  api.fixtures.mockResolvedValue(upcomingFixtures);
  api.leagueFixtures.mockResolvedValue(leagueFixturesPayload);
  api.teams.mockResolvedValue(teamsResponse);
  api.team.mockResolvedValue(teamDetail);
  api.teamForm.mockResolvedValue(teamForm);
  api.teamStandings.mockResolvedValue(teamStanding);
  api.teamMatches.mockResolvedValue({ total: 1, matches: [matchList.matches[0]] });
  api.teamStats.mockResolvedValue({
    seasons: [],
    totals: { played: 0, won: 0, drawn: 0, lost: 0, goals_for: 0, goals_against: 0, points: 0, ppg: 0, goal_difference: 0 },
    home_away: {},
  });
};

function renderApp(route) {
  return render(
    <MemoryRouter initialEntries={[route]}>
      <App />
    </MemoryRouter>,
  );
}

describe("App routing", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it.each([
    ["/", /Dashboard/],
    ["/leagues", /Leagues/],
    ["/leagues/premier", /Premier League/],
    ["/teams", /Teams/],
    ["/teams/arsenal", /Arsenal/],
    ["/matches", /Matches/],
    ["/match/1001", /Arsenal/],
  ])("renders the %s page", async (route, heading) => {
    renderApp(route);
    expect(await screen.findByRole("heading", { name: heading })).toBeInTheDocument();
  });

  it("redirects unknown routes to the dashboard", async () => {
    renderApp("/does-not-exist");
    expect(await screen.findByRole("heading", { name: /Dashboard/ })).toBeInTheDocument();
  });

  it("navigates between pages via the topbar", async () => {
    renderApp("/");
    await screen.findByRole("heading", { name: /Dashboard/ });

    fireEvent.click(screen.getByRole("link", { name: "Matches" }));

    expect(await screen.findByRole("heading", { name: /Matches/ })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Leagues" })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Teams" })).toBeInTheDocument();
    expect(screen.queryByRole("link", { name: "Standings" })).not.toBeInTheDocument();
  });
});