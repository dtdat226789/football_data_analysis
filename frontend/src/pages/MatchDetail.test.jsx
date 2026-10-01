import { render, screen } from "@testing-library/react";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import { matchDetail, matchInsights } from "../test/fixtures.js";
import MatchDetail from "./MatchDetail.jsx";

vi.mock("../api/client.js", () => {
  const names = [
    "health", "meta", "listLeagues", "league", "seasons", "standings",
    "matches", "match", "matchInsights", "matchesRecent", "dashboard", "fixtures", "leagueFixtures",
    "teams", "team", "teamMatches", "teamForm", "teamStandings", "teamStats",
    "analysis", "analysisModule",
  ];
  const stub = {};
  for (const name of names) stub[name] = vi.fn();
  stub.chartUrl = (_l, _c) => `/api/v1/analysis/${_l}/charts/${_c}`;
  return { api: stub };
});

const seed = () => {
  api.match.mockResolvedValue(matchDetail);
  api.matchInsights.mockResolvedValue(matchInsights);
};

function renderMatch(route = "/match/1001") {
  return render(
    <MemoryRouter initialEntries={[route]}>
      <Routes>
        <Route path="/match/:id" element={<MatchDetail />} />
      </Routes>
    </MemoryRouter>,
  );
}

describe("MatchDetail", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders the scoreline, facts and links", async () => {
    renderMatch();

    expect(await screen.findByRole("heading", { name: /Arsenal/ })).toBeInTheDocument();
    expect(screen.getByText("2 – 1")).toBeInTheDocument();
    // half-time; head-to-head rows can also contain a "1 - 0" scoreline
    expect(screen.getAllByText("1 – 0").length).toBeGreaterThanOrEqual(1);
    expect(screen.getByRole("link", { name: "Premier League" })).toHaveAttribute(
      "href",
      "/leagues/premier",
    );
    expect(screen.getAllByText("2024-2025").length).toBeGreaterThanOrEqual(1);
    expect(screen.getByText("20'")).toBeInTheDocument();
    expect(screen.getAllByText("1001").length).toBeGreaterThanOrEqual(1);
    expect(screen.getByRole("heading", { name: "Raw record" })).toBeInTheDocument();
    expect(api.match).toHaveBeenCalledWith("1001");
  });

  it("shows an error box for unknown matches", async () => {
    api.match.mockRejectedValue(new Error("match 999999 not found"));
    renderMatch("/match/999999");

    expect(await screen.findByText(/match 999999 not found/)).toBeInTheDocument();
  });
});
describe("MatchDetail insights", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders pre-match context grouped under its labels", async () => {
    renderMatch();

    expect(await screen.findByRole("heading", { name: /Pre-match context/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "Form (last 5)" })).toBeInTheDocument();
    expect(screen.getByText("Home win rate (home games)")).toBeInTheDocument();
    expect(screen.getByText("0.70")).toBeInTheDocument();
    expect(api.matchInsights).toHaveBeenCalledWith("1001");
  });

  it("badges in-sample predictions as optimistic", async () => {
    renderMatch();

    expect(await screen.findByText("in-sample")).toBeInTheDocument();
    expect(screen.getByText(/the model was fitted on them/)).toBeInTheDocument();
    // Correctness of the stored prediction is shown, not hidden.
    expect(screen.getByText("correct")).toBeInTheDocument();
  });

  it("badges holdout rows as out-of-sample and omits the warning", async () => {
    api.matchInsights.mockResolvedValue({
      ...matchInsights,
      model: { ...matchInsights.model, in_sample: false, season: "2025-2026" },
    });
    renderMatch();

    expect(await screen.findByText("out-of-sample")).toBeInTheDocument();
    expect(screen.queryByText(/the model was fitted on them/)).not.toBeInTheDocument();
  });

  it("renders head-to-head summary and prior meetings as links", async () => {
    renderMatch();

    expect(await screen.findByRole("heading", { name: /Head to head/ })).toBeInTheDocument();
    expect(screen.getByText(/Arsenal 1W 1D 0L Chelsea/)).toBeInTheDocument();
    const link = screen.getByRole("link", { name: "Chelsea vs Arsenal" });
    // The route is /match/:id; /matches/:id resolved to the dashboard.
    expect(link).toHaveAttribute("href", "/match/900");
  });

  it("still renders the match when insights are unavailable", async () => {
    // A missing artifact must not take down the page.
    api.matchInsights.mockRejectedValue(new Error("insights unavailable"));
    renderMatch();

    expect(await screen.findByRole("heading", { name: /Arsenal/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "Raw record" })).toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Pre-match context/ })).not.toBeInTheDocument();
  });

  it("hides the panel entirely when every section is empty", async () => {
    api.matchInsights.mockResolvedValue({
      api_id: 1001,
      pre_match: null,
      model: null,
      head_to_head: { limit: 10, summary: null, matches: [] },
    });
    renderMatch();

    await screen.findByRole("heading", { name: /Arsenal/ });
    expect(screen.queryByRole("heading", { name: /Pre-match context/ })).not.toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Model view/ })).not.toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Head to head/ })).not.toBeInTheDocument();
  });

  it("shows a first-ever meeting without a summary line", async () => {
    api.matchInsights.mockResolvedValue({
      ...matchInsights,
      head_to_head: { limit: 10, summary: null, matches: [] },
    });
    renderMatch();

    expect(await screen.findByText("No previous meetings on record.")).toBeInTheDocument();
  });

  it("marks a wrong prediction as wrong", async () => {
    api.matchInsights.mockResolvedValue({
      ...matchInsights,
      model: { ...matchInsights.model, actual_match_result: "AWAY_WIN" },
    });
    renderMatch();

    expect(await screen.findByText("wrong")).toBeInTheDocument();
  });
});

describe("MatchDetail head-to-head truncation", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("says the table shows only the most recent of a longer history", async () => {
    api.matchInsights.mockResolvedValue({
      ...matchInsights,
      head_to_head: {
        ...matchInsights.head_to_head,
        truncated: true,
        summary: { ...matchInsights.head_to_head.summary, played: 24 },
        matches: matchInsights.head_to_head.matches.slice(0, 1),
      },
    });
    renderMatch();

    expect(await screen.findByText("24 previous")).toBeInTheDocument();
    expect(screen.getByText("Showing the 1 most recent of 24.")).toBeInTheDocument();
  });

  it("omits the truncation note when the history is complete", async () => {
    api.matchInsights.mockResolvedValue({
      ...matchInsights,
      head_to_head: { ...matchInsights.head_to_head, truncated: false },
    });
    renderMatch();

    expect(await screen.findByText("2 previous")).toBeInTheDocument();
    expect(screen.queryByText(/most recent of/)).not.toBeInTheDocument();
  });
});

describe("MatchDetail probability bars", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("gives each probability bar a non-zero height", async () => {
    // .bar-track carries no height in CSS, so an omitted inline height renders
    // an invisible bar. Regression guard.
    const { container } = renderMatch();
    await screen.findByRole("heading", { name: /Model view/ });
    const tracks = container.querySelectorAll(".bar-track");
    expect(tracks.length).toBeGreaterThan(0);
    for (const track of tracks) {
      expect(track.style.height).toMatch(/^\d+px$/);
      expect(parseInt(track.style.height, 10)).toBeGreaterThan(0);
    }
  });
});
