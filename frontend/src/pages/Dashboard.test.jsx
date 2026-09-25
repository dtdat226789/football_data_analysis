import { screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import { dashboard } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import Dashboard from "./Dashboard.jsx";

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
  api.dashboard.mockResolvedValue(dashboard);
};

describe("Dashboard", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders top leagues from the aggregate", async () => {
    renderPage(<Dashboard />);

    expect(await screen.findByRole("heading", { name: /Dashboard/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /Top leagues/ })).toBeInTheDocument();

    const link = screen.getAllByRole("link", { name: /Premier League/ }).find((a) => a.getAttribute("href") === "/leagues/premier");
    expect(link).toBeInTheDocument();
    expect(screen.getByText("2,330 matches")).toBeInTheDocument();
  });

  it("shows upcoming top picks with prediction chips and recent results", async () => {
    renderPage(<Dashboard />);

    expect(await screen.findByRole("heading", { name: /Upcoming · top picks/ })).toBeInTheDocument();
    expect(screen.getAllByText("Arsenal").length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText("Chelsea").length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText("58%").length).toBeGreaterThanOrEqual(1);

    expect(screen.getByRole("heading", { name: /Recent results/ })).toBeInTheDocument();
    expect(screen.getByText("2–1")).toBeInTheDocument();
  });

  it("renders top clubs (current leaders)", async () => {
    renderPage(<Dashboard />);

    expect(await screen.findByRole("heading", { name: /Top clubs · current leaders/ })).toBeInTheDocument();
    expect(screen.getByText(/85 pts/)).toBeInTheDocument();
    expect(screen.getAllByText("Barcelona").length).toBeGreaterThanOrEqual(1);
  });

  it("groups leagues by region", async () => {
    renderPage(<Dashboard />);

    expect(await screen.findByRole("heading", { name: /Europe/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /Asia/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /Americas/ })).toBeInTheDocument();
    expect(
      screen.getAllByRole("link", { name: /J-League/ }).length,
    ).toBeGreaterThanOrEqual(1);
  });
});