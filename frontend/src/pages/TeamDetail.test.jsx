import { screen, waitFor, within } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { Route } from "react-router-dom";
import { api } from "../test/mockApi.js";
import { renderRoutes } from "../test/render.jsx";
import {
  leagueFixturesPayload,
  matchList,
  teamDetail,
  teamForm,
  teamStanding,
  teamStatsResponse,
} from "../test/fixtures.js";
import TeamDetail from "./TeamDetail.jsx";

vi.mock("../api/client.js", async () => {
  // The stub list is read from the real client rather than written out here.
  // Each test used to carry its own copy of these names, and the copies had
  // already drifted apart — so a new api.foo() call reached an undefined stub in
  // whichever test happened to render that page first.
  const { api: actual } = await vi.importActual("../api/client.js");
  const stub = {};
  for (const name of Object.keys(actual)) stub[name] = vi.fn();
  stub.chartUrl = vi.fn((league, chart) => `/api/v1/analysis/${league}/charts/${chart}`);
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

function renderTeamDetail(route = "/teams/arsenal") {
  return renderRoutes(<Route path="/teams/:slug" element={<TeamDetail />} />, { route });
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
    expect(heading.closest(".page-head")).toHaveTextContent("canonical: Arsenal");
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

    expect(screen.getByText("Upcoming · Premier League")).toBeInTheDocument();
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
    expect(api.teamStats).toHaveBeenLastCalledWith("arsenal", {
      league: "premier",
      view: "classic",
      season: "2024-2025",
    });
  });

  it("renders the aggregated statistics section with charts", async () => {
    renderTeamDetail();

    const section = (await screen.findByRole("heading", { name: /Statistics · Premier League/ })).closest(
      "section",
    );

    expect(await within(section).findByText("27W-4D-7L")).toBeInTheDocument();
    expect(within(section).getByText("91 : 29")).toBeInTheDocument();
    expect(within(section).getByText("2.24 PPG")).toBeInTheDocument();
    expect(within(section).getAllByText("#1").length).toBeGreaterThanOrEqual(1);
    expect(within(section).getAllByText("2023-2024").length).toBeGreaterThanOrEqual(2);

    expect(within(section).getByText("Points per season")).toBeInTheDocument();
    expect(within(section).getByText("83 pts")).toBeInTheDocument();
    expect(within(section).getByText("League position per season (lower is better)")).toBeInTheDocument();
    expect(within(section).getByText("Win % by venue")).toBeInTheDocument();
    expect(within(section).getByText("84.2%")).toBeInTheDocument();
    expect(within(section).getByText("57.9%")).toBeInTheDocument();
  });

  // The stats panel sat under the season selector but ignored it, so every
  // figure was career-wide no matter which season was chosen.
  it("scopes the statistics panel to the selected season", async () => {
    renderTeamDetail();

    await screen.findByRole("heading", { name: /Statistics · Premier League/ });
    await waitFor(() =>
      expect(api.teamStats).toHaveBeenCalledWith(
        "arsenal",
        expect.objectContaining({ league: "premier", season: "2024-2025" }),
      ),
    );

    const section = screen.getByRole("heading", { name: /Statistics · Premier League/ }).closest("section");
    expect(within(section).getByText("Matches · 2024-2025")).toBeInTheDocument();
    expect(
      within(section).getByText(/Summary and venue split cover 2024-2025/),
    ).toBeInTheDocument();
    expect(
      within(section).getByText(/compare every season the team has played in/),
    ).toBeInTheDocument();
  });

  it("shows the best finish's points from that same season", async () => {
    renderTeamDetail();

    const section = (await screen.findByRole("heading", { name: /Statistics · Premier League/ })).closest(
      "section",
    );
    // best is one coherent row: position 1, 2024-2025, 85 points.
    expect(await within(section).findByText("2024-2025 · 85 pts")).toBeInTheDocument();
  });

  // The shared fixture only knows one league, so it cannot catch the fallback
  // effect silently overwriting a ?league= deep link.
  it("honours a ?league= deep link over the first available league", async () => {
    api.team.mockResolvedValue({
      team: teamDetail.team,
      memberships: [
        ...teamDetail.memberships,
        {
          league: "ucl",
          league_name: "Champions League",
          season: "2024-2025",
          start_year: 2024,
          end_year: 2025,
          api_name: "Arsenal",
          api_slug: "arsenal",
        },
      ],
    });

    // leagues[] sorts by league_name, so "Premier League" is not first here.
    renderTeamDetail("/teams/arsenal?league=premier");

    // The league and the season are resolved by two effects in turn — the season
    // rows come from the memberships that only exist once `api.team` resolves —
    // and `teamForm` needs both. Waiting on the select alone left this racing the
    // second effect, which passed most runs and failed when the machine was busy.
    await waitFor(() =>
      expect(screen.getByLabelText("League")).toHaveValue("premier"),
    );
    await waitFor(() =>
      expect(api.teamForm).toHaveBeenCalledWith(
        "arsenal",
        expect.objectContaining({ league: "premier" }),
      ),
    );
  });

  it("falls back to the first league when the deep link names an unknown one", async () => {
    renderTeamDetail("/teams/arsenal?league=not-a-league");

    await waitFor(() =>
      expect(screen.getByLabelText("League")).toHaveValue("premier"),
    );
  });
});