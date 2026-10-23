import { fireEvent, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "./test/mockApi.js";
import { renderPage } from "./test/render.jsx";
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

vi.mock("./api/client.js", async () => {
  // Stub list read from the real client, so it cannot drift.
  const { api: actual } = await vi.importActual("./api/client.js");
  const stub = {};
  for (const name of Object.keys(actual)) stub[name] = vi.fn();
  stub.chartUrl = vi.fn((league, chart) => `/api/v1/analysis/${league}/charts/${chart}`);
  return { api: stub };
});

const seed = () => {
  api.listLeagues.mockResolvedValue(leagues);
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

const renderApp = (route) => renderPage(<App />, { route });

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