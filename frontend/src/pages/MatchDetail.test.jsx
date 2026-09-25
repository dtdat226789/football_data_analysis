import { render, screen } from "@testing-library/react";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import { matchDetail } from "../test/fixtures.js";
import MatchDetail from "./MatchDetail.jsx";

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
  api.match.mockResolvedValue(matchDetail);
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
    expect(screen.getByText("1 – 0")).toBeInTheDocument(); // half-time
    expect(screen.getByRole("link", { name: "premier" })).toHaveAttribute("href", "/leagues/premier");
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