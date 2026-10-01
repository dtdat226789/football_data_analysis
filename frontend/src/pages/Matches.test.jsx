import { fireEvent, screen, waitFor, within } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import { leagues, upcomingFixtures } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import Matches from "./Matches.jsx";

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

const recentMatches = {
  count: 2,
  total: 2,
  limit: 50,
  offset: 0,
  matches: [
    {
      api_id: 1001,
      match_date: "2025-01-18",
      home_team: "Arsenal",
      away_team: "Chelsea",
      home_score: 2,
      away_score: 1,
      league: "premier",
      league_name: "Premier League",
    },
    {
      api_id: 1002,
      match_date: "2025-01-19",
      home_team: "Barcelona",
      away_team: "Real Madrid",
      home_score: 0,
      away_score: 0,
      league: "spain1",
      league_name: "La Liga",
    },
  ],
};

const seed = () => {
  api.listLeagues.mockResolvedValue(leagues);
  api.fixtures.mockResolvedValue(upcomingFixtures);
  api.matchesRecent.mockResolvedValue(recentMatches);
};

/** Chip labels and values sit in sibling nodes, so match on the joined text. */
const chipTexts = () =>
  [...document.querySelectorAll(".pred-chip")].map((el) => el.textContent.trim());

describe("Matches", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders upcoming fixtures with prediction chips and a recent results table", async () => {
    renderPage(<Matches />);

    expect(await screen.findByRole("heading", { name: "Matches" })).toBeInTheDocument();

    const upcoming = await screen.findByRole("heading", { name: /Upcoming/ });
    expect(upcoming.closest("section").querySelector(".badge")).toHaveTextContent("2");
    expect(screen.getAllByText("Arsenal").length).toBeGreaterThanOrEqual(1);
    // Chips come from the markets the backend selected, so the Arsenal row leads
    // with its decisive goal line rather than a fixed 1/X/2 read.
    expect(chipTexts()).toContain("O1.5 80%");
    // prediction meta line surfaces model confidence + data through
    expect(screen.getByText(/conf 58%/)).toBeInTheDocument();
    expect(screen.getAllByText(/as of 2026-01-29/).length).toBeGreaterThanOrEqual(1);

    const recent = screen.getByRole("heading", { name: /Recent/ });
    expect(recent.closest("section").querySelector(".badge")).toHaveTextContent("2");
    const table = within(recent.closest("section"));
    expect(table.getAllByRole("row")).toHaveLength(3);
    expect(table.getAllByRole("link", { name: "view" })[0]).toHaveAttribute("href", "/match/1001");
    expect(screen.getAllByText("2 – 1").length).toBeGreaterThanOrEqual(1);
  });

  it("groups upcoming fixtures under a heading per day", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    const days = [...document.querySelectorAll(".fixture-day")].map((el) => [
      el.querySelector(".fixture-day-head").textContent,
      el.querySelectorAll(".event").length,
    ]);
    // Each fixture is alone on its day, so each heading reports "1 shown".
    expect(days).toHaveLength(2);
    for (const [head, count] of days) {
      expect(head).toMatch(/\d+ shown/);
      expect(head).toMatch(/[A-Z][a-z]{2} \d{1,2} [A-Z][a-z]{2}/);
      expect(count).toBe(1);
    }
    // Arsenal's fixture sits under the earlier day, before Madrid's.
    expect(days[0][0]).toMatch(/Feb/);
    expect(document.querySelector(".fixture-day .event .teams").textContent).toContain("Arsenal");
  });

  it("says which slice of a paged upcoming list is on screen", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    // 2 of 2 rows fit, so the heading claims the list is complete rather than
    // implying there is more below.
    expect(screen.getByText("all 2")).toBeInTheDocument();
  });

  it("builds each fixture's chip row from the markets the backend selected", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    const chips = chipTexts();
    // Arsenal: four derived markets, including one half-time line marked assumed.
    expect(chips).toEqual(["O1.5 80%", "Away +0.5 42%", "U2.5 41%", "1 62%", "BTTS yes 68%"]);
    // The old fixed set is gone: no "BTTS 55%", and no 1/X/2 it was built from.
    expect(chips).not.toContain("BTTS 55%");
    expect(chips.some((c) => c.startsWith("X "))).toBe(false);
    // The half-time chip is flagged as assumed rather than presented as measured.
    const assumed = [...document.querySelectorAll(".pred-chip.chip-assumed")];
    expect(assumed).toHaveLength(1);
    expect(assumed[0].textContent).toBe("1 62%");
    expect(assumed[0].getAttribute("title")).toContain("assumed");
  });

  it("links every upcoming fixture to its detail page using the slug tail", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    const upcoming = screen.getByRole("heading", { name: /Upcoming/ }).closest("section");
    const links = within(upcoming).getAllByRole("link", { name: "detail" });
    expect(links.map((l) => l.getAttribute("href"))).toEqual([
      "/fixture/premier/2026-02-01-arsenal-vs-chelsea",
      "/fixture/spain1/2026-02-02-barcelona-vs-madrid",
    ]);
  });

  it("refetches fixtures and results when a league is picked", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    fireEvent.change(screen.getByLabelText("League"), { target: { value: "spain1" } });

    await waitFor(() =>
      expect(api.fixtures).toHaveBeenLastCalledWith({
        league: "spain1",
        sort: "confidence",
        limit: 50,
        offset: 0,
        from_date: undefined,
        to_date: undefined,
        min_confidence: undefined,
      }),
    );
    await waitFor(() =>
      expect(api.matchesRecent).toHaveBeenLastCalledWith(
        expect.objectContaining({ league: "spain1", offset: 0 }),
      ),
    );
  });

  it("filters upcoming fixtures by model confidence", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    fireEvent.click(screen.getByRole("button", { name: "60%+" }));

    await waitFor(() =>
      expect(api.fixtures).toHaveBeenLastCalledWith(
        expect.objectContaining({ min_confidence: "0.6", offset: 0 }),
      ),
    );
    // A confidence filter has no meaningful confidence ordering, so the server
    // switches to date order and the list is read as a schedule.
    expect(api.fixtures).toHaveBeenLastCalledWith(
      expect.objectContaining({ sort: "date" }),
    );
  });

  it("applies the shared date window to upcoming fixtures too", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    fireEvent.change(screen.getByLabelText("From date"), { target: { value: "2026-02-02" } });

    await waitFor(() =>
      expect(api.fixtures).toHaveBeenLastCalledWith(
        expect.objectContaining({ from_date: "2026-02-02", sort: "date" }),
      ),
    );
    expect(api.fixtures).toHaveBeenLastCalledWith(
      expect.objectContaining({ to_date: undefined }),
    );
  });

  it("jumps to a single day and rewinds to the first page", async () => {
    renderPage(<Matches />, { route: "/matches?uoffset=50" });
    await screen.findByRole("heading", { name: /Upcoming/ });

    // Day chips carry their true counts, so a reader can see a 126-match
    // Saturday is a day rather than an endless list.
    const day = screen.getByRole("button", { name: /Sun 1 Feb 1/ });
    fireEvent.click(day);

    await waitFor(() =>
      expect(api.fixtures).toHaveBeenLastCalledWith(
        // Selecting a day rewinds the offset, so you land on that day and not on
        // page 2 of it.
        expect.objectContaining({ offset: 0, sort: "date" }),
      ),
    );
    expect(day).toHaveAttribute("aria-pressed", "true");

    // Clicking the active day clears it again.
    fireEvent.click(day);
    await waitFor(() =>
      expect(api.fixtures).toHaveBeenLastCalledWith(
        expect.objectContaining({ sort: "confidence" }),
      ),
    );
  });

  it("paginates upcoming fixtures independently of recent results", async () => {
    const total = 120;
    api.fixtures.mockImplementation((params = {}) => {
      const size = params.limit || 50;
      const offset = params.offset || 0;
      const all = Array.from({ length: total }, (_, i) => {
        // Three days of fixtures, so paging genuinely straddles a day boundary.
        const day = `2026-02-0${1 + Math.floor(i / 40)}`;
        return {
          slug: `england/premier-league/${day}-home-${i}-vs-away-${i}`,
          league: "premier",
          home_team: `Home ${i}`,
          away_team: `Away ${i}`,
          match_date: day,
          time: "15:00",
          status: "scheduled",
          predictions: {
            home: 0.5, away: 0.25, confidence: 0.5, data_through: "2026-01-29",
            selected: [],
          },
        };
      });
      const matches = all.slice(offset, offset + size);
      return {
        count: matches.length,
        total,
        returned: matches.length,
        limit: size,
        offset,
        has_more: offset + matches.length < total,
        dates: ["2026-02-01", "2026-02-02", "2026-02-03"],
        day_counts: { "2026-02-01": 40, "2026-02-02": 40, "2026-02-03": 40 },
        matches,
      };
    });

    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    const section = () => screen.getByRole("heading", { name: /Upcoming/ }).closest("section");

    // Page one of three: the first day is complete, the second is cut at 10.
    expect(within(section()).getAllByText("1–50 of 120").length).toBeGreaterThan(0);
    const heads = [...section().querySelectorAll(".fixture-day-head")].map((h) => h.textContent);
    expect(heads[0]).toMatch(/40 shown(?! of)/);
    expect(heads[1]).toMatch(/10 shown of 40/);
    // A split day is not left to look complete.
    expect(within(section()).getAllByRole("button", { name: "see this day" })).toHaveLength(1);

    // Upcoming paging must not disturb the recent list's own offset.
    fireEvent.click(within(section()).getByRole("button", { name: "Next ›" }));
    await waitFor(() =>
      expect(api.fixtures).toHaveBeenLastCalledWith(expect.objectContaining({ offset: 50 })),
    );
    expect(api.matchesRecent).toHaveBeenLastCalledWith(expect.objectContaining({ offset: 0 }));
  });

  it("adds and resets a from-date filter on recent results", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    expect(api.matchesRecent).toHaveBeenCalledWith(
      expect.objectContaining({ from_date: undefined, to_date: undefined, offset: 0 }),
    );

    fireEvent.change(screen.getByLabelText("From date"), { target: { value: "2025-01-18" } });
    await waitFor(() =>
      expect(api.matchesRecent).toHaveBeenLastCalledWith(
        expect.objectContaining({ from_date: "2025-01-18", to_date: undefined }),
      ),
    );

    fireEvent.click(screen.getByRole("button", { name: "Reset dates" }));
    await waitFor(() => expect(screen.getByLabelText("From date")).toHaveValue(""));
    expect(screen.queryByRole("button", { name: "Reset dates" })).not.toBeInTheDocument();
  });

  it("applies a 14-day preset to recent results", async () => {
    renderPage(<Matches />);
    await screen.findByRole("heading", { name: /Upcoming/ });

    fireEvent.click(screen.getByRole("button", { name: "14d" }));

    await waitFor(() =>
      expect(api.matchesRecent).toHaveBeenLastCalledWith(
        expect.objectContaining({ from_date: expect.stringMatching(/^\d{4}-\d{2}-\d{2}$/), to_date: undefined }),
      ),
    );
    expect(screen.getByRole("button", { name: "Reset dates" })).toBeInTheDocument();
  });

  it("paginates recent results with offset reset on page size change", async () => {
    api.matchesRecent.mockImplementation((params = {}) => {
      const size = params.limit || 50;
      const offset = params.offset || 0;
      const total = 320;
      const all = Array.from({ length: total }, (_, i) => ({
        api_id: 1000 + i,
        match_date: "2025-01-18",
        home_team: `Home ${i}`,
        away_team: `Away ${i}`,
        home_score: 1,
        away_score: 0,
        league: "premier",
      }));
      const matches = all.slice(offset, offset + size);
      return { count: matches.length, total, limit: size, offset, matches };
    });
    renderPage(<Matches />);

    expect(await screen.findByText("1–50 of 320")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "‹ Prev" })).toBeDisabled();
    expect(screen.getByRole("button", { name: "Next ›" })).not.toBeDisabled();

    fireEvent.click(screen.getByRole("button", { name: "Next ›" }));
    expect(await screen.findByText("51–100 of 320")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "‹ Prev" })).not.toBeDisabled();

    fireEvent.change(screen.getByLabelText("Page size"), { target: { value: "20" } });
    await waitFor(() =>
      expect(api.matchesRecent).toHaveBeenLastCalledWith(
        expect.objectContaining({ offset: 0, limit: 20 }),
      ),
    );
  });

  it("shows an empty state when no fixtures exist", async () => {
    api.fixtures.mockResolvedValue({ count: 0, total: 0, matches: [] });
    renderPage(<Matches />);

    await screen.findByRole("heading", { name: /Upcoming/ });
    expect(screen.getByText(/No upcoming fixtures/)).toBeInTheDocument();
  });

  it("labels leagues by name everywhere, never by slug", async () => {
    // "wsweden" is a routing key, not something a reader should have to decode.
    api.listLeagues.mockResolvedValue([
      ...leagues,
      { slug: "wsweden", name: "Allsvenskan Women", country: "Sweden", teams: 14 },
    ]);
    api.matchesRecent.mockResolvedValue({
      ...recentMatches,
      matches: [{ ...recentMatches.matches[0], league: "wsweden", league_name: "Allsvenskan Women" }],
    });
    renderPage(<Matches />, { route: "/matches?league=wsweden" });

    // Subtitle resolves the slug from the league list it already fetched.
    expect(await screen.findByText(/Allsvenskan Women · upcoming fixtures/)).toBeInTheDocument();
    // Table cell uses the name the row already carries.
    const table = screen.getByRole("table");
    expect(within(table).getByText("Allsvenskan Women")).toBeInTheDocument();
    expect(table).not.toHaveTextContent("wsweden");
  });

  it("falls back to the slug when a row carries no league name", async () => {
    api.matchesRecent.mockResolvedValue({
      ...recentMatches,
      matches: [{ ...recentMatches.matches[0], league_name: undefined }],
    });
    renderPage(<Matches />);

    const table = await screen.findByRole("table");
    expect(within(table).getByText("premier")).toBeInTheDocument();
  });
});