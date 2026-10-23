import { fireEvent, screen, waitFor, within } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../test/mockApi.js";
import { leagueDetail, leagues, teamsResponse } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import Teams from "./Teams.jsx";

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
  api.listLeagues.mockResolvedValue(leagues);
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
    expect(table.getByRole("link", { name: "Chelsea" })).toHaveAttribute("href", "/teams/Chelsea");
  });

  it("asks the server for the search term instead of filtering the page", async () => {
    renderPage(<Teams />);
    await screen.findByRole("heading", { name: "Teams" });
    api.teams.mockResolvedValue({ ...teamsResponse, total: 1, teams: [teamsResponse.teams[2]] });

    const search = screen.getByPlaceholderText("Search all teams by name or alias…");
    fireEvent.change(search, { target: { value: "chel" } });

    // The term is debounced, so the request lands a beat after the keystroke.
    await waitFor(() =>
      expect(api.teams).toHaveBeenCalledWith({ limit: 50, offset: 0, q: "chel" }),
    );
    expect(screen.getByRole("link", { name: "Chelsea" })).toBeInTheDocument();
  });

  it("reports when no team matches the search", async () => {
    renderPage(<Teams />);
    await screen.findByRole("heading", { name: "Teams" });
    api.teams.mockResolvedValue({ ...teamsResponse, total: 0, teams: [] });

    fireEvent.change(screen.getByPlaceholderText("Search all teams by name or alias…"), {
      target: { value: "zzz" },
    });

    expect(await screen.findByText("No teams match “zzz”.")).toBeInTheDocument();
  });
});