import { render, screen, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../api/client.js";
import {
  fixtureMarkets,
  marketDetail,
  marketDetailHalfToFull,
  marketDetailQuarter,
} from "../test/fixtures.js";
import MarketDetailModal from "./MarketDetailModal.jsx";

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

const market = (key) => fixtureMarkets.find((m) => m.key === key);

const renderModal = (row, payload = marketDetail) => {
  api.fixtureMarket.mockResolvedValue(payload);
  return render(
    <MarketDetailModal
      league={LEAGUE}
      matchId={TAIL}
      market={row}
      onClose={vi.fn()}
    />,
  );
};

const settlementRow = (name) =>
  screen.getByText(name).closest(".settle-row");

describe("MarketDetailModal", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("asks for the clicked market only", async () => {
    renderModal(market("ft.asian_handicap.-1_home"));

    await screen.findByRole("dialog");
    expect(api.fixtureMarket).toHaveBeenCalledWith(LEAGUE, TAIL, "ft.asian_handicap.-1_home");
  });

  it("shows how the market settles across win, push and lose", async () => {
    renderModal(market("ft.asian_handicap.-1_home"));

    await screen.findByRole("dialog");
    expect(within(settlementRow("Wins")).getByText("31.0%")).toBeInTheDocument();
    expect(within(settlementRow("Pushes")).getByText("27.0%")).toBeInTheDocument();
    expect(within(settlementRow("Loses")).getByText("42.0%")).toBeInTheDocument();
  });

  it("lists the scorelines that pay the market", async () => {
    renderModal(market("ft.asian_handicap.-1_home"));

    await screen.findByText("2-0");
    const table = screen.getByText("2-0").closest("table");
    expect(within(table).getByText("pushes")).toBeInTheDocument();
    expect(screen.getByText(/4 of 81 grid cells/)).toBeInTheDocument();
  });

  it("spells out a quarter line's half-stake split", async () => {
    // The row clicked and the payload served have to agree, or the title would
    // come from one and the cells from the other.
    const quarter = { ...marketDetailQuarter.market };
    api.fixtureMarket.mockResolvedValue(marketDetailQuarter);
    render(
      <MarketDetailModal
        league={LEAGUE}
        matchId={TAIL}
        market={quarter}
        onClose={vi.fn()}
      />,
    );

    // A quarter line is the whole point of the half-stake label: without it a
    // reader would assume "Home -0.25" either wins or loses on a draw.
    expect(await screen.findByText("pushes half, loses half")).toBeInTheDocument();
    expect(screen.getByText("Home -0.25 · Full time")).toBeInTheDocument();
  });

  it("shows the two 1X2 splits behind a half-time / full-time market", async () => {
    renderModal(market("ht_ft.home.home"), marketDetailHalfToFull);

    await screen.findByText("Where it comes from");
    const table = screen.getByText("Half time").closest("table");
    // The HT row is the one carrying the assumed split, so it is badged.
    expect(within(table).getByText("41.0%")).toBeInTheDocument();
    expect(within(table).getByText("58.0%")).toBeInTheDocument();
    // A product of splits, not a set of scorelines.
    expect(screen.queryByText(/grid cells/)).not.toBeInTheDocument();
  });

  it("badges a market whose half-time split was assumed", async () => {
    renderModal(market("ht_ft.home.home"), marketDetailHalfToFull);

    await screen.findByText("assumed");
  });

  it("closes on the backdrop, the close button and Escape", async () => {
    const onClose = vi.fn();
    api.fixtureMarket.mockResolvedValue(marketDetail);
    render(
      <MarketDetailModal
        league={LEAGUE}
        matchId={TAIL}
        market={market("ft.asian_handicap.-1_home")}
        onClose={onClose}
      />,
    );
    const dialog = await screen.findByRole("dialog");

    await userEvent.click(screen.getByRole("button", { name: "Close" }));
    expect(onClose).toHaveBeenCalledTimes(1);

    await userEvent.click(dialog);
    expect(onClose).toHaveBeenCalledTimes(2);

    await userEvent.keyboard("{Escape}");
    expect(onClose).toHaveBeenCalledTimes(3);
  });

  it("says so when a market has no explanation rather than rendering nothing", async () => {
    renderModal(market("ft.result.home"), { ...marketDetail, market: null });

    expect(
      await screen.findByText("This market has no explanation to show."),
    ).toBeInTheDocument();
  });

  it("reports a failed lookup instead of leaving an empty dialog", async () => {
    api.fixtureMarket.mockRejectedValue(new Error("market 'ft.result.home' not found"));
    render(
      <MarketDetailModal
        league={LEAGUE}
        matchId={TAIL}
        market={market("ft.result.home")}
        onClose={vi.fn()}
      />,
    );

    expect(await screen.findByText(/not found/)).toBeInTheDocument();
  });

  it("renders nothing without a market to explain", () => {
    const { container } = render(
      <MarketDetailModal league={LEAGUE} matchId={TAIL} market={null} onClose={vi.fn()} />,
    );
    expect(container).toBeEmptyDOMElement();
    expect(api.fixtureMarket).not.toHaveBeenCalled();
  });
});
