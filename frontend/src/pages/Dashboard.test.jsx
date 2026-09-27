import { screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import { dashboard } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import Dashboard, { regionBuckets } from "./Dashboard.jsx";

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

  it("renders the 'other' region bucket", async () => {
    // Regression: the page hardcoded three RegionSections, so the four leagues
    // the backend buckets as "other" were never rendered at all.
    renderPage(<Dashboard />);

    expect(await screen.findByRole("heading", { name: /Other/ })).toBeInTheDocument();
    expect(
      screen.getAllByRole("link", { name: /A-League/ }).some(
        (a) => a.getAttribute("href") === "/leagues/australia",
      ),
    ).toBe(true);
  });

  it("survives a payload missing the optional collections", async () => {
    // Regression: bare destructuring left these undefined, so .map/.length threw.
    api.dashboard.mockResolvedValue({ meta: { n_leagues: 0 } });
    renderPage(<Dashboard />);

    const head = await screen.findByRole("heading", { name: /Dashboard/ });
    expect(head).toBeInTheDocument();
    expect(head.parentElement.textContent).toMatch(/0 leagues/);
    expect(screen.getByText(/0 recent results/)).toBeInTheDocument();
    expect(screen.getByText(/0 upcoming/)).toBeInTheDocument();
    // every region section still renders, with empty buckets
    for (const name of ["Europe", "Asia", "Americas", "Other"]) {
      expect(screen.getByRole("heading", { name: new RegExp(name) })).toBeInTheDocument();
    }
  });
});

describe("regionBuckets", () => {
  it("returns every known region, empty buckets included", () => {
    const names = regionBuckets({}).map((b) => b.region);
    expect(names).toEqual(["europe", "asia", "america", "other"]);
    expect(regionBuckets({}).every((b) => b.leagues.length === 0)).toBe(true);
  });

  it("keeps known-region order and appends unknown regions", () => {
    const buckets = regionBuckets({ other: [1], atlantis: [2] });
    expect(buckets.map((b) => b.region)).toEqual([
      "europe", "asia", "america", "other", "atlantis",
    ]);
    expect(buckets.find((b) => b.region === "other").leagues).toEqual([1]);
    expect(buckets.find((b) => b.region === "atlantis").leagues).toEqual([2]);
  });

  it("tolerates a missing or malformed payload", () => {
    expect(regionBuckets(undefined).map((b) => b.region)).toHaveLength(4);
    expect(regionBuckets(null).every((b) => Array.isArray(b.leagues))).toBe(true);
    expect(regionBuckets({ europe: "nope" }).find((b) => b.region === "europe").leagues)
      .toEqual([]);
  });
});