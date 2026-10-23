import { fireEvent, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../test/mockApi.js";
import { leagues } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import Leagues from "./Leagues.jsx";

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
};

describe("Leagues", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders leagues grouped by region with analysis badges", async () => {
    renderPage(<Leagues />);

    expect(await screen.findByRole("heading", { name: "Leagues" })).toBeInTheDocument();
    const europe = screen.getByRole("heading", { name: /Europe/ });
    expect(europe.closest("section").textContent).toContain("La Liga");
    expect(screen.getByRole("heading", { name: /Asia/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /Americas/ })).toBeInTheDocument();

    const premier = screen.getByRole("link", { name: /Premier League/ });
    expect(premier).toHaveAttribute("href", "/leagues/premier");
    expect(screen.getAllByText("analysis").length).toBe(2);
  });

  it("filters leagues by name or country", async () => {
    renderPage(<Leagues />);
    await screen.findByRole("heading", { name: "Leagues" });

    fireEvent.change(screen.getByLabelText("Search"), { target: { value: "Japan" } });

    expect(screen.queryByRole("link", { name: /Premier League/ })).not.toBeInTheDocument();
    expect(screen.getByRole("link", { name: /J-League/ })).toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /Europe/ })).not.toBeInTheDocument();
  });

  it("shows a message when the search matches nothing", async () => {
    renderPage(<Leagues />);
    await screen.findByRole("heading", { name: "Leagues" });

    fireEvent.change(screen.getByLabelText("Search"), { target: { value: "zzz" } });

    expect(screen.getByText(/No leagues match/)).toBeInTheDocument();
  });
});