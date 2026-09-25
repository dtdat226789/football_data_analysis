import { fireEvent, screen, within } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import { leagueDetail, leagues, meta, teamsResponse } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import Teams from "./Teams.jsx";

vi.mock("../api/client.js", () => {
  const names = [
    "health",
    "meta",
    "listLeagues",
    "league",
    "seasons",
    "standings",
    "matches",
    "match",
    "teams",
    "team",
    "teamMatches",
    "teamForm",
    "teamStandings",
    "teamStats",
    "analysis",
    "analysisModule",
  ];
  const stub = {};
  for (const name of names) stub[name] = vi.fn();
  stub.chartUrl = (league, chart) => `/api/v1/analysis/${league}/charts/${chart}`;
  return { api: stub };
});

const seed = () => {
  api.listLeagues.mockResolvedValue(leagues);
  api.meta.mockResolvedValue(meta);
  api.league.mockResolvedValue(leagueDetail);
  api.teams.mockResolvedValue(teamsResponse);
};

describe("Teams", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders the team registry rows", async () => {
    renderPage(<Teams />);

    expect(await screen.findByRole("heading", { name: "Teams" })).toBeInTheDocument();
    expect(screen.getByText("3 teams in the canonical registry")).toBeInTheDocument();

    const table = within(await screen.findByRole("table"));
    expect(table.getAllByRole("row")).toHaveLength(4);
    expect(table.getByRole("link", { name: "Aston Villa" })).toHaveAttribute(
      "href",
      "/teams/Aston%20Villa",
    );
    expect(table.getByText("chelsea")).toBeInTheDocument();
  });

  it("filters rows by name or slug", async () => {
    renderPage(<Teams />);
    await screen.findByRole("heading", { name: "Teams" });

    const search = screen.getByPlaceholderText("Filter by name or slug…");
    fireEvent.change(search, { target: { value: "chel" } });

    const table = within(await screen.findByRole("table"));
    expect(table.getAllByRole("row")).toHaveLength(2);
    expect(table.getByRole("link", { name: "Chelsea" })).toBeInTheDocument();

    fireEvent.change(search, { target: { value: "" } });
    const reset = within(await screen.findByRole("table"));
    expect(reset.getAllByRole("row")).toHaveLength(4);
  });

  it("shows a message when no team matches the filter", async () => {
    renderPage(<Teams />);
    await screen.findByRole("heading", { name: "Teams" });

    fireEvent.change(screen.getByPlaceholderText("Filter by name or slug…"), {
      target: { value: "zzz" },
    });

    expect(await screen.findByText("No teams match the filter.")).toBeInTheDocument();
  });
});