import { screen, within } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { Route } from "react-router-dom";
import { api } from "../test/mockApi.js";
import { renderRoutes } from "../test/render.jsx";
import { fixtureDetail, fixtureDetailNoHistory } from "../test/fixtures.js";
import FixtureDetail from "./FixtureDetail.jsx";

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

const LEAGUE = "premier";
const TAIL = "2026-02-01-arsenal-vs-chelsea";

// Rendered through the real route pattern, so the splat that carries the
// `date-home-vs-away` id is exercised rather than assumed.
const renderFixture = (route = `/fixture/${LEAGUE}/${TAIL}`) =>
  renderRoutes(
    <Route path="/fixture/:league/*" element={<FixtureDetail />} />,
    { route },
  );

const seed = (payload = fixtureDetail) => {
  api.fixtureDetail.mockResolvedValue(payload);
};

describe("FixtureDetail", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("requests the fixture by league and slug tail", async () => {
    renderFixture();

    await screen.findByRole("heading", { name: "Arsenal vs Chelsea" });
    expect(api.fixtureDetail).toHaveBeenCalledWith(LEAGUE, TAIL);
  });

  it("shows the headline, matchday, season and status", async () => {
    renderFixture();

    await screen.findByRole("heading", { name: "Arsenal vs Chelsea" });
    expect(
      screen.getByText("01/02/2026 23:00 \u00b7 matchday 25 \u00b7 2025-2026 \u00b7 scheduled"),
    ).toBeInTheDocument();
  });

  it("renders the goal outlook with model confidence and data freshness", async () => {
    renderFixture();

    const panel = (await screen.findByRole("heading", { name: /^Prediction/ })).closest("section");
    const body = within(panel);
    // The model's own goal distribution, in plain language.
    expect(body.getByText("2+ goals")).toBeInTheDocument();
    expect(body.getByText("3+ goals")).toBeInTheDocument();
    expect(body.getByText("82%")).toBeInTheDocument();
    expect(body.getByText("61%")).toBeInTheDocument();
    expect(body.getByText(/Model confidence/)).toBeInTheDocument();
  });

  it("renders the model metadata that qualifies the prediction", async () => {
    renderFixture();

    const panel = (await screen.findByRole("heading", { name: /^Prediction/ })).closest("section");
    const body = within(panel);
    expect(body.getByText("dc_v2.0")).toBeInTheDocument();
    // expected goals, the goal outlook, and the trust metadata
    expect(body.getByText(/1\.82 – 0\.94/)).toBeInTheDocument();
    expect(body.getByText(/HT total 0\.98/)).toBeInTheDocument();
    expect(body.getByText("0.0019")).toBeInTheDocument();
    expect(body.getByText(/sigma 0\.5/)).toBeInTheDocument();
    expect(body.getByText("home att 0.42 / def 0.31")).toBeInTheDocument();
    expect(body.getByText("home 34.6")).toBeInTheDocument();
    expect(body.getByText("away 15.6")).toBeInTheDocument();
    expect(body.getByText(/leans: fail/)).toBeInTheDocument();
    expect(body.getByText(/probabilities: pass/)).toBeInTheDocument();
    // "as of" chip meta and the Data through row both name the cut-off.
    expect(body.getAllByText(/2026-01-29/).length).toBe(2);
  });

  it("renders crests, form, venue split, rest and table for both sides", async () => {
    renderFixture();

    await screen.findByRole("heading", { name: "Arsenal vs Chelsea" });
    expect(document.querySelector('img[src="https://cdn.example/arsenal.png"]')).toBeInTheDocument();
    expect(document.querySelector('img[src="https://cdn.example/chelsea.png"]')).toBeInTheDocument();

    const sections = screen.getAllByRole("heading", { name: /Home|Away/ });
    const homeCard = sections[0].closest("section");
    const body = within(homeCard);
    // form pills from the last five results
    expect(body.getByTitle(/Arsenal 2-1 Liverpool/)).toBeInTheDocument();
    expect(body.getByText(/8W 2D 2L/)).toBeInTheDocument();
    expect(body.getByText(/win rate 66\.7%/)).toBeInTheDocument();
    expect(body.getByText("4 days")).toBeInTheDocument();
    expect(body.getByText(/2 · 57 pts · \+31 · 24 played/)).toBeInTheDocument();
  });

  it("reuses the pre-match and head-to-head panels from a finished match", async () => {
    renderFixture();

    expect(await screen.findByRole("heading", { name: /Pre-match context/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /Head to head/ })).toBeInTheDocument();
    expect(screen.getByText(/Arsenal 1W 1D 0L Chelsea/)).toBeInTheDocument();
    const link = screen.getByRole("link", { name: "Chelsea vs Arsenal" });
    expect(link).toHaveAttribute("href", "/match/900");
  });

  it("shows kickoff metadata and links to the source", async () => {
    renderFixture();

    const card = (await screen.findByRole("heading", { name: "Fixture record" })).closest("section");
    const body = within(card);
    expect(body.getByText("Sun 1 Feb \u00b7 23:00")).toBeInTheDocument();
    expect(body.getByText("Matchday 25")).toBeInTheDocument();
    expect(body.getByText("regular_season")).toBeInTheDocument();
    const source = body.getByRole("link", { name: "football-charts.com" });
    expect(source).toHaveAttribute(
      "href",
      "https://football-charts.com/england/premier-league/2026-02-01-arsenal-vs-chelsea",
    );
    expect(body.getByRole("link", { name: "Premier League" })).toHaveAttribute(
      "href",
      "/leagues/premier",
    );
  });

  it("renders without history or a collected detail payload", async () => {
    seed(fixtureDetailNoHistory);

    renderFixture();

    expect(await screen.findByRole("heading", { name: "Arsenal vs Chelsea" })).toBeInTheDocument();
    // no prediction block and no collected payload to render
    expect(screen.queryByRole("heading", { name: /^Prediction/ })).not.toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Pre-match context/ })).not.toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Head to head/ })).not.toBeInTheDocument();
    // ... but the fixture identity and the file-derived kickoff remain
    expect(document.querySelector('img[src="https://cdn.example/arsenal.png"]')).toBeNull();
    expect(
      screen.getByText("01/02/2026 23:00 \u00b7 scheduled"),
    ).toBeInTheDocument();
    const card = screen.getByRole("heading", { name: "Fixture record" }).closest("section");
    const body = within(card);
    expect(body.getByText("16:00")).toBeInTheDocument();
    // Derived sections report "unknown", they do not invent a matchday.
    const matchdayRow = body.getByText("Matchday").closest("tr");
    expect(within(matchdayRow).getByText("\u2014")).toBeInTheDocument();
  });

  it("surfaces an error from the endpoint", async () => {
    api.fixtureDetail.mockRejectedValue(new Error("fixture not found"));

    renderFixture();

    expect(await screen.findByText(/fixture not found/)).toBeInTheDocument();
  });
});
