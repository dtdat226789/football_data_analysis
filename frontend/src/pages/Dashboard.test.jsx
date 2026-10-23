import { screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../test/mockApi.js";
import { dashboard } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import Dashboard, { regionBuckets } from "./Dashboard.jsx";

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
    // Chips follow the markets the backend selected for each fixture.
    const chips = [...document.querySelectorAll(".pred-chip")].map((el) => el.textContent.trim());
    expect(chips).toEqual(["O1.5 80%", "Away +0.5 42%", "U2.5 41%", "1 62%", "BTTS yes 68%"]);

    expect(screen.getByRole("heading", { name: /Recent results/ })).toBeInTheDocument();
    expect(screen.getByText("2–1")).toBeInTheDocument();
  });

  it("names the league on upcoming and recent rows instead of showing the slug", async () => {
    // Upcoming rows come from the fixtures dump, recent rows from the matches
    // feed; both used to print "wsweden" where the name belonged.
    api.dashboard.mockResolvedValue({
      ...dashboard,
      upcoming_matches: [
        { ...dashboard.upcoming_matches[0], league: "wsweden", league_name: "Allsvenskan Women" },
      ],
      recent_matches: [
        { ...dashboard.recent_matches[0], league: "wsweden", league_name: "Allsvenskan Women" },
      ],
    });
    renderPage(<Dashboard />);

    await screen.findByRole("heading", { name: /Recent results/ });
    expect(screen.getAllByText(/Allsvenskan Women/).length).toBeGreaterThanOrEqual(2);
    expect(document.body).not.toHaveTextContent("wsweden");
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