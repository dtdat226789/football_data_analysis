import { fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { api } from "../test/mockApi.js";
import {
  analysisBundle,
  leagueDetail,
  matchList,
  standingsClassic,
  upcomingFixtures,
} from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";
import { I18nProvider } from "../i18n/I18nProvider.jsx";
import { ROUTER_FUTURE } from "../routerFuture.js";
import LeagueDetail from "./LeagueDetail.jsx";

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
  api.league.mockResolvedValue(leagueDetail);
  api.standings.mockResolvedValue(standingsClassic);
  api.matches.mockResolvedValue(matchList);
  api.fixtures.mockResolvedValue(upcomingFixtures);
  api.analysis.mockResolvedValue(analysisBundle);
};

const renderDetail = (route = "/leagues/premier") =>
  renderPage(
    <Routes>
      <Route path="/leagues/:slug" element={<LeagueDetail />} />
    </Routes>,
    { route },
  );

describe("LeagueDetail", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    seed();
  });

  it("renders the header and the standings tab by default with the latest season", async () => {
    renderDetail();

    expect(await screen.findByRole("heading", { name: "Premier League" })).toBeInTheDocument();
    expect(screen.getByText(/round-robin/)).toBeInTheDocument();

    // The table shell mounts before its rows resolve, so wait for the content.
    await screen.findAllByText("Arsenal");
    expect(api.standings).toHaveBeenCalledWith("premier", { season: "2024-2025", view: "classic" });
  });

  it("honours a season supplied in the URL", async () => {
    renderDetail("/leagues/premier?season=2023-2024");

    await screen.findByRole("table");
    expect(api.standings).toHaveBeenLastCalledWith("premier", { season: "2023-2024", view: "classic" });
    expect(screen.getByLabelText("Season")).toHaveValue("2023-2024");
  });

  it("switches the standings view and updates the URL", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Luck" }));

    await waitFor(() =>
      expect(api.standings).toHaveBeenLastCalledWith("premier", { season: "2024-2025", view: "luck" }),
    );
  });

  it("switches to the analysis tab", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Analysis" }));

    expect(await screen.findByText("Home advantage is strong")).toBeInTheDocument();
    expect(screen.getByText("380")).toBeInTheDocument();
    expect(screen.getByText("2.80")).toBeInTheDocument();
  });

  it("translates the analysis tab findings and chart captions into Vietnamese", async () => {
    api.analysis.mockResolvedValue({
      ...analysisBundle,
      charts: ["matches_analysis_ht_ft_matrix.png", "avg_goals.png"],
      reports: {
        ...analysisBundle.reports,
        findings: {
          key_findings: [
            { id: "F1", finding: "Outcome split across all seasons", detail: "2330 matches: home wins 43.0%.", importance: "medium" },
            { id: "F2", finding: "Data-quality warnings (3)", detail: "3 rows skipped.", importance: "medium" },
            { id: "F3", finding: "Home advantage is strong", detail: "62% of points scored at home." },
          ],
        },
      },
    });
    render(
      <I18nProvider language="vi">
        <MemoryRouter initialEntries={["/leagues/premier"]} future={ROUTER_FUTURE}>
          <Routes>
            <Route path="/leagues/:slug" element={<LeagueDetail />} />
          </Routes>
        </MemoryRouter>
      </I18nProvider>,
    );

    fireEvent.click(await screen.findByRole("button", { name: "Phân tích" }));

    expect(await screen.findByText("Phân bố kết quả qua các mùa giải")).toBeInTheDocument();
    expect(screen.getByText("Cảnh báo chất lượng dữ liệu (3)")).toBeInTheDocument();
    // An unknown finding keeps its original text rather than vanishing.
    expect(screen.getByText("Home advantage is strong")).toBeInTheDocument();
    // Known chart stems translate; unmapped ones fall back to the readable stem.
    expect(screen.getByText("Ma trận hiệp một / hiệp hai")).toBeInTheDocument();
    expect(screen.getByText("avg goals")).toBeInTheDocument();
  });

  it("shows upcoming fixtures with predictions and recent results on the matches tab", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Matches" }));

    expect(await screen.findByRole("heading", { name: /Upcoming/ })).toBeInTheDocument();
    expect(screen.getAllByText("Arsenal").length).toBeGreaterThanOrEqual(1);

    // The merged feed, not the raw per-league payload: the matches page reads the
    // markets the backend selected, and this tab has to read the same ones.
    expect(api.fixtures).toHaveBeenCalledWith(expect.objectContaining({ league: "premier" }));
    expect(api.leagueFixtures).not.toHaveBeenCalled();

    expect(screen.getByRole("heading", { name: /Recent · 2024-2025/ })).toBeInTheDocument();
    expect(screen.getAllByRole("link", { name: "view" }).length).toBeGreaterThanOrEqual(1);
  });

  it("gives a fixture the same chips on the league tab as on the matches page", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Matches" }));

    // The old tab fed `model_predictions.dc_v2.calibrated` into the legacy fixed
    // chip set, so this one fixture wore a different row of predictions here than
    // it did on /matches. Both pages now build chips from `selected` markets.
    const chips = await waitFor(() => {
      const found = [...document.querySelectorAll(".pred-chip")].map((el) => el.textContent.trim());
      expect(found).toContain("O1.5 80%");
      return found;
    });
    expect(chips).not.toContain("BTTS 55%");

    // And the fixture links through to its own page, which the old tab never did.
    expect(within(screen.getByRole("heading", { name: /Upcoming/ }).closest("section")).getAllByRole("link", { name: "detail" }).length)
      .toBeGreaterThanOrEqual(1);
  });

  it("says so when a season has no finished matches", async () => {
    api.matches.mockResolvedValue({ total: 0, matches: [] });
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Matches" }));

    // The table used to render bare under its heading, with nothing in the body.
    expect(await screen.findByText("No finished matches recorded for 2024-2025.")).toBeInTheDocument();
  });

  it("lists seasons from the details payload", async () => {
    renderDetail();

    fireEvent.click(await screen.findByRole("button", { name: "Seasons" }));

    expect(await screen.findByText("in_progress")).toBeInTheDocument();
    expect(screen.getAllByText("2023-2024").length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText("2025-2026").length).toBeGreaterThanOrEqual(1);
  });
});