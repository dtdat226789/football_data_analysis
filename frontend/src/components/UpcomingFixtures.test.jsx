import { screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { clearApiCache } from "../hooks/useApi.js";
import { upcomingFixtures } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import UpcomingFixtures from "./UpcomingFixtures.jsx";

vi.mock("../api/client.js", async () => {
  const { api: actual } = await vi.importActual("../api/client.js");
  const stub = {};
  for (const name of Object.keys(actual)) stub[name] = vi.fn();
  return { api: stub };
});

import { api } from "../test/mockApi.js";

describe("UpcomingFixtures", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    clearApiCache();
    api.fixtures.mockResolvedValue(upcomingFixtures);
  });

  it("renders the grouped fixtures and the filtered total", async () => {
    renderPage(<UpcomingFixtures />);

    expect(await screen.findByText("Arsenal")).toBeInTheDocument();
    expect(screen.getByText("Chelsea")).toBeInTheDocument();
    expect(screen.getByText("2")).toBeInTheDocument();
    expect(api.fixtures).toHaveBeenCalledWith(
      expect.objectContaining({ sort: "date", min_confidence: undefined }),
    );
  });

  it("shows a countdown only for fixtures that have not kicked off", async () => {
    const nowSpy = vi.spyOn(Date, "now").mockReturnValue(Date.parse("2026-02-01T14:00:00Z"));
    try {
      renderPage(<UpcomingFixtures />);
      expect(await screen.findByText("Arsenal")).toBeInTheDocument();

      expect(
        screen.getByRole("timer", { name: "Time until kickoff at 23:00" }),
      ).toHaveTextContent("2h 0m");
    } finally {
      nowSpy.mockRestore();
    }
  });

  it("hides the countdown once the fixture has started", async () => {
    const nowSpy = vi.spyOn(Date, "now").mockReturnValue(Date.parse("2026-02-03T00:00:00Z"));
    try {
      renderPage(<UpcomingFixtures />);
      expect(await screen.findByText("Arsenal")).toBeInTheDocument();

      expect(screen.queryByRole("timer")).not.toBeInTheDocument();
    } finally {
      nowSpy.mockRestore();
    }
  });

  it("accepts a known confidence filter and drops a hand-edited one", async () => {
    renderPage(<UpcomingFixtures />, { route: "/?conf=0.6" });
    await waitFor(() => expect(api.fixtures).toHaveBeenCalled());
    expect(api.fixtures).toHaveBeenCalledWith(
      expect.objectContaining({ min_confidence: "0.6" }),
    );

    clearApiCache();
    renderPage(<UpcomingFixtures />, { route: "/?conf=junk" });
    await waitFor(() => expect(api.fixtures).toHaveBeenCalledTimes(2));
    expect(api.fixtures).toHaveBeenLastCalledWith(
      expect.objectContaining({ min_confidence: undefined }),
    );
  });

  it("shows an empty state when the payload has malformed arrays", async () => {
    api.fixtures.mockResolvedValue({ total: 2, matches: "bad", dates: "bad" });
    renderPage(<UpcomingFixtures />);

    expect(await screen.findByText(/No upcoming fixtures/)).toBeInTheDocument();
  });
});
