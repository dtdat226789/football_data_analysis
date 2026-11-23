import { act, fireEvent, screen } from "@testing-library/react";
import { Route } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../test/mockApi.js";
import { clubAnalysis, leagues } from "../test/fixtures.js";
import { clearApiCache } from "../hooks/useApi.js";
import { renderRoutes } from "../test/render.jsx";
import ClubAnalysis from "./ClubAnalysis.jsx";

vi.mock("../api/client.js", async () => {
  const { api: actual } = await vi.importActual("../api/client.js");
  const stub = {};
  for (const name of Object.keys(actual)) stub[name] = vi.fn();
  return { api: stub };
});

const routes = <Route path="/club-analysis" element={<ClubAnalysis />} />;

const seed = () => {
  api.listLeagues.mockResolvedValue(leagues);
  api.clubAnalysis.mockResolvedValue(clubAnalysis);
};

describe("ClubAnalysis", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    clearApiCache();
    seed();
  });

  it("renders the club cards, timeline and league ranking", async () => {
    renderRoutes(routes, { route: "/club-analysis?league=premier" });

    expect(await screen.findByRole("heading", { name: /Club Analysis/ })).toBeInTheDocument();
    expect(screen.getByRole("img", { name: /Goals \/ game by season/ })).toBeInTheDocument();
    expect(screen.getByText("Team goals ranking")).toBeInTheDocument();
    expect(screen.getByText("Club rating")).toBeInTheDocument();
    expect(screen.getByRole("columnheader", { name: "Rating" })).toBeInTheDocument();
    expect(screen.getAllByText("82.6").length).toBeGreaterThan(0);
    expect(screen.getAllByText("ARS").length).toBeGreaterThan(0);
    expect(api.clubAnalysis).toHaveBeenCalledWith({ league: "premier", season: "", team: "" });
  });

  it("passes a changed team filter to the API", async () => {
    renderRoutes(routes, { route: "/club-analysis?league=premier" });
    await screen.findByRole("heading", { name: /Club Analysis/ });

    await act(async () => {
      fireEvent.change(screen.getByLabelText("Team"), { target: { value: "liverpool" } });
    });

    await vi.waitFor(() => {
      expect(api.clubAnalysis).toHaveBeenCalledWith({
        league: "premier",
        season: "",
        team: "liverpool",
      });
    });
  });

  it("surfaces API errors", async () => {
    api.clubAnalysis.mockRejectedValue(new Error("boom"));
    renderRoutes(routes, { route: "/club-analysis" });
    expect(await screen.findByText("boom")).toBeInTheDocument();
  });
});
