import { act, fireEvent, screen } from "@testing-library/react";
import { Route } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../test/mockApi.js";
import { leagueDetail, leagues, teamKpi } from "../test/fixtures.js";
import { clearApiCache } from "../hooks/useApi.js";
import { renderRoutes } from "../test/render.jsx";
import TeamKpi from "./TeamKpi.jsx";

vi.mock("../api/client.js", async () => {
  const { api: actual } = await vi.importActual("../api/client.js");
  const stub = {};
  for (const name of Object.keys(actual)) stub[name] = vi.fn();
  return { api: stub };
});

const routes = <Route path="/teams/:slug/kpi" element={<TeamKpi />} />;
const route = "/teams/arsenal/kpi?league=premier";

const seed = () => {
  api.listLeagues.mockResolvedValue(leagues);
  api.leagueSeasons.mockResolvedValue(leagueDetail);
  api.teamKpi.mockResolvedValue(teamKpi);
};

describe("TeamKpi", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    clearApiCache();
    seed();
  });

  it("renders the KPI groups, recent games and table", async () => {
    renderRoutes(routes, { route });

    expect(await screen.findByRole("heading", { name: /Arsenal/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "Creativity" })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "Defence" })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "Last 5 games" })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "League table" })).toBeInTheDocument();
    expect(screen.getByText("79.21")).toBeInTheDocument();
    expect(screen.getByRole("columnheader", { name: "Rating" })).toBeInTheDocument();
    expect(screen.getAllByText("82.6").length).toBeGreaterThan(0);
    expect(api.teamKpi).toHaveBeenCalledWith("arsenal", { league: "premier", season: "", n: 5 });
  });

  it("changes the season and games window through URL state", async () => {
    renderRoutes(routes, { route });
    await screen.findByRole("heading", { name: "Creativity" });

    await act(async () => {
      fireEvent.change(screen.getByLabelText("Season"), { target: { value: "2023-2024" } });
    });
    await vi.waitFor(() => {
      expect(api.teamKpi).toHaveBeenCalledWith("arsenal", {
        league: "premier",
        season: "2023-2024",
        n: 5,
      });
    });

    await act(async () => {
      fireEvent.change(screen.getByLabelText("Games"), { target: { value: "10" } });
    });
    await vi.waitFor(() => {
      expect(api.teamKpi).toHaveBeenCalledWith("arsenal", {
        league: "premier",
        season: "2023-2024",
        n: 10,
      });
    });
  });

  it("shows an error from the API", async () => {
    api.teamKpi.mockRejectedValue(new Error("failed"));
    renderRoutes(routes, { route });
    expect(await screen.findByText("failed")).toBeInTheDocument();
  });
});
