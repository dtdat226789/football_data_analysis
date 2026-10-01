import { render, screen, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import { fixtureDetail, fixtureDetailNoHistory, marketDetail } from "../test/fixtures.js";
import FixtureDetail from "./FixtureDetail.jsx";

vi.mock("../api/client.js", () => {
  const names = [
    "health", "meta", "listLeagues", "league", "seasons", "standings",
    "matches", "match", "matchInsights", "matchesRecent", "dashboard",
    "fixtures", "leagueFixtures", "fixtureDetail", "fixtureMarket",
    "teams", "team", "teamMatches", "teamForm", "teamStandings", "teamStats",
    "analysis", "analysisModule",
  ];
  const stub = {};
  for (const name of names) stub[name] = vi.fn();
  stub.chartUrl = (_l, _c) => `/api/v1/analysis/${_l}/charts/${_c}`;
  return { api: stub };
});

const LEAGUE = "premier";
const TAIL = "2026-02-01-arsenal-vs-chelsea";

// Rendered through the real route pattern, so the splat that carries the
// `date-home-vs-away` id is exercised rather than assumed.
const renderFixture = (route = `/fixture/${LEAGUE}/${TAIL}`) =>
  render(
    <MemoryRouter initialEntries={[route]}>
      <Routes>
        <Route path="/fixture/:league/*" element={<FixtureDetail />} />
      </Routes>
    </MemoryRouter>,
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
      screen.getByText("2026-02-01 16:00 \u00b7 matchday 25 \u00b7 2025-2026 \u00b7 scheduled"),
    ).toBeInTheDocument();
  });

  it("renders the 1/X/2 split including the derived draw probability", async () => {
    renderFixture();

    const panel = (await screen.findByRole("heading", { name: /^Prediction/ })).closest("section");
    const body = within(panel);
    expect(body.getByText("Home win")).toBeInTheDocument();
    expect(body.getByText("Draw")).toBeInTheDocument();
    expect(body.getByText("Away win")).toBeInTheDocument();
    expect(body.getByText("58.0%")).toBeInTheDocument();
    expect(body.getByText("24.0%")).toBeInTheDocument();
    expect(body.getByText("18.0%")).toBeInTheDocument();
  });

  it("renders the model metadata that qualifies the prediction", async () => {
    renderFixture();

    const panel = (await screen.findByRole("heading", { name: /^Prediction/ })).closest("section");
    const body = within(panel);
    expect(body.getByText("dc_v2.0")).toBeInTheDocument();
    // expected goals, the 1/X/2 chips, and the trust metadata
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

  it("lists every goal line with its raw and calibrated read", async () => {
    renderFixture();

    const panel = (await screen.findByRole("heading", { name: "Goal lines" })).closest("section");
    const rows = within(panel).getAllByRole("row");
    // header + 3 lines
    expect(rows).toHaveLength(4);
    expect(within(panel).getByText("Over 1.5")).toBeInTheDocument();
    expect(within(panel).getByText("Over 2.5")).toBeInTheDocument();
    expect(within(panel).getByText("Half time")).toBeInTheDocument();
    // Two full-time lines and one half-time line in the sample.
    expect(within(panel).getAllByText("Full time")).toHaveLength(2);
  });

  it("renders the full derived market menu under the goal lines", async () => {
    renderFixture();

    const panel = (await screen.findByRole("heading", { name: /Markets/ })).closest("section");
    const body = within(panel);
    expect(body.getByText(/21 derived/)).toBeInTheDocument();
    // Every family the engine can produce is labelled for the reader.
    expect(body.getByRole("heading", { name: "Result" })).toBeInTheDocument();
    expect(body.getByRole("heading", { name: "Goals (over/under)" })).toBeInTheDocument();
    expect(body.getByRole("heading", { name: "Asian handicap" })).toBeInTheDocument();
    expect(body.getByRole("heading", { name: "Correct score" })).toBeInTheDocument();
    expect(body.getByRole("heading", { name: "Half time / full time" })).toBeInTheDocument();
    // A quarter line that can refund says so rather than showing one number.
    expect(body.getByText(/27\.0% push/)).toBeInTheDocument();
  });

  it("flags which markets are driving the chips", async () => {
    renderFixture();

    const panel = (await screen.findByRole("heading", { name: /Markets/ })).closest("section");
    const featured = [...panel.querySelectorAll("tbody tr.featured")].map((row) =>
      within(row).getAllByRole("cell")[0].firstChild.textContent.trim()
    );
    expect(featured).toEqual(["O1.5", "U2.5", "Away +0.5", "1/1"]);
  });

  it("distinguishes measured markets from assumed ones", async () => {
    renderFixture();

    const panel = (await screen.findByRole("heading", { name: /Markets/ })).closest("section");
    expect(within(panel).getByText("4 assumed")).toBeInTheDocument();
    // One table per family, so scope to body rows to skip the repeated headers.
    const rows = [...panel.querySelectorAll("tbody tr")];
    const sources = rows.map((tr) => within(tr).getAllByRole("cell")[2].textContent.trim());
    expect(rows).toHaveLength(21);
    expect(sources.filter((s) => s === "model").length).toBe(17);
    expect(sources.filter((s) => s === "assumed").length).toBe(4);
  });

  it("surfaces the dynamic chips the backend selected", async () => {
    renderFixture();

    // The chips follow the model: over 1.5 and the under 2.5 both show, and the
    // old fixed 1/X/2 set is gone.
    const panel = (await screen.findByRole("heading", { name: /^Prediction/ })).closest("section");
    const chips = within(panel)
      .getAllByTitle(/goal distribution|assumed/)
      .map((el) => el.textContent.trim());
    expect(chips).toEqual(["O1.5 80%", "U2.5 41%", "Away +0.5 42%", "1/1 24%"]);
  });

  it("renders crests, form, venue split, rest and table for both sides", async () => {
    renderFixture();

    await screen.findByRole("heading", { name: "Arsenal vs Chelsea" });
    expect(document.querySelector('img[src="https://cdn.example/arsenal.png"]')).toBeInTheDocument();
    expect(document.querySelector('img[src="https://cdn.example/chelsea.png"]')).toBeInTheDocument();

    const sections = screen.getAllByRole("heading", { name: /\(home\)|\(away\)/ });
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
    expect(body.getByText("2026-02-01T16:00:00+00:00")).toBeInTheDocument();
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
    expect(screen.queryByRole("heading", { name: "Goal lines" })).not.toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Pre-match context/ })).not.toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Head to head/ })).not.toBeInTheDocument();
    // ... but the fixture identity and the file-derived kickoff remain
    expect(document.querySelector('img[src="https://cdn.example/arsenal.png"]')).toBeNull();
    expect(
      screen.getByText("2026-02-01 16:00 \u00b7 scheduled"),
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

  it("opens a market's explanation from the featured chip", async () => {
    api.fixtureMarket.mockResolvedValue(marketDetail);
    renderFixture();
    await screen.findByRole("heading", { name: "Arsenal vs Chelsea" });

    await userEvent.click(screen.getByRole("button", { name: /Away \+0\.5 42%/ }));

    expect(await screen.findByRole("dialog")).toBeInTheDocument();
    expect(api.fixtureMarket).toHaveBeenCalledWith(LEAGUE, TAIL, "ft.asian_handicap.-0.5_away");
  });

  it("opens a market's explanation from a table row that is not featured", async () => {
    const detail = { ...marketDetail, market: { ...marketDetail.market, key: "ft.correct_score.2_1", label: "2-1" } };
    api.fixtureMarket.mockResolvedValue(detail);
    renderFixture();
    await screen.findByRole("heading", { name: "Arsenal vs Chelsea" });

    // A correct score never reaches the chip row, but it is still a market.
    await userEvent.click(screen.getByRole("button", { name: "2-1" }));

    expect(await screen.findByRole("dialog")).toBeInTheDocument();
    expect(api.fixtureMarket).toHaveBeenCalledWith(LEAGUE, TAIL, "ft.correct_score.2_1");
  });

  it("does not refetch the fixture to open a market", async () => {
    api.fixtureMarket.mockResolvedValue(marketDetail);
    renderFixture();
    await screen.findByRole("heading", { name: "Arsenal vs Chelsea" });
    expect(api.fixtureDetail).toHaveBeenCalledTimes(1);

    await userEvent.click(screen.getByRole("button", { name: /Away \+0\.5 42%/ }));
    await screen.findByRole("dialog");

    expect(api.fixtureDetail).toHaveBeenCalledTimes(1);
  });

  it("closes the explanation and stops fetching for it", async () => {
    api.fixtureMarket.mockResolvedValue(marketDetail);
    renderFixture();
    await screen.findByRole("heading", { name: "Arsenal vs Chelsea" });

    await userEvent.click(screen.getByRole("button", { name: /Away \+0\.5 42%/ }));
    await screen.findByRole("dialog");
    await userEvent.click(screen.getByRole("button", { name: "Close" }));

    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });
});
