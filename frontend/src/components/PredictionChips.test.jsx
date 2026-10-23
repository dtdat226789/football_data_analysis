import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";
import PredictionChips from "./PredictionChips.jsx";
import { I18nProvider } from "../i18n/I18nProvider.jsx";

const chipLabels = (container) =>
  [...container.querySelectorAll(".pred-chip")].map((el) => el.textContent.trim());

describe("PredictionChips", () => {
  it("renders the fixed set when the payload carries no selected markets", () => {
    // An older backend payload: no `selected` key at all.
    const { container } = render(
      <PredictionChips predictions={{ home: 0.58, away: 0.18, btts_yes: 0.55, over_1_5: 0.82, over_2_5: 0.61 }} />
    );
    expect(chipLabels(container)).toEqual(["1 58%", "X —", "2 18%", "BTTS 55%", "O1.5 82%", "O2.5 61%"]);
  });

  it("falls back when selected is present but empty", () => {
    const { container } = render(
      <PredictionChips predictions={{ home: 0.58, away: 0.18, selected: [] }} />
    );
    expect(chipLabels(container)).toContain("1 58%");
  });

  it("renders the derived markets the backend selected", () => {
    const { container } = render(
      <PredictionChips
        predictions={{
          home: 0.58,
          away: 0.18,
          selected: [
            { key: "ft.totals.over_1.5", label: "O1.5", scope: "full_time", probability: 0.8, provenance: "model" },
            { key: "ft.totals.under_2.5", label: "U2.5", scope: "full_time", probability: 0.41, provenance: "model" },
          ],
        }}
      />
    );
    expect(chipLabels(container)).toEqual(["O1.5 80%", "U2.5 41%"]);
  });

  it("follows the model rather than a fixed list", () => {
    // A low-scoring fixture: the under line surfaces, over 1.5 does not, and the
    // draw the old fixed set showed as "—" is simply absent.
    const { container } = render(
      <PredictionChips
        predictions={{
          home: 0.4,
          away: 0.3,
          selected: [
            { key: "ft.totals.under_2.5", label: "U2.5", scope: "full_time", probability: 0.74, provenance: "model" },
          ],
        }}
      />
    );
    expect(chipLabels(container)).toEqual(["U2.5 74%"]);
  });

  it("shows a real draw when the model rates one", () => {
    const { container } = render(
      <PredictionChips
        predictions={{
          selected: [{ key: "ft.result.draw", label: "X", scope: "full_time", probability: 0.61, provenance: "model" }],
        }}
      />
    );
    expect(chipLabels(container)).toEqual(["X 61%"]);
  });

  it("marks assumed markets differently from measured ones", () => {
    render(
      <PredictionChips
        predictions={{
          selected: [
            { key: "a", label: "U2.5", scope: "full_time", probability: 0.74, provenance: "model" },
            { key: "b", label: "HT U0.5", scope: "half_time", probability: 0.7, provenance: "modelled" },
          ],
        }}
      />
    );
    const [measured, assumed] = [...document.querySelectorAll(".pred-chip")];
    expect(measured.className).not.toContain("chip-assumed");
    expect(assumed.className).toContain("chip-assumed");
  });

  it("expands the derived chip labels into Vietnamese phrases", () => {
    const { container } = render(
      <I18nProvider language="vi">
        <PredictionChips
          predictions={{
            selected: [
              { key: "ft.result.home", family: "result", label: "1", scope: "full_time", line: null, selection: "home", probability: 0.68, provenance: "model" },
              { key: "ft.totals.over_1.5", family: "totals", label: "O1.5", scope: "full_time", line: 1.5, selection: "over", probability: 0.8, provenance: "model" },
              { key: "ft.totals.under_2.5", family: "totals", label: "U2.5", scope: "full_time", line: 2.5, selection: "under", probability: 0.41, provenance: "model" },
              { key: "ft.btts.yes", family: "btts", label: "BTTS yes", scope: "full_time", line: null, selection: "yes", probability: 0.68, provenance: "model" },
              { key: "ft.asian_handicap.-0.5_away", family: "asian_handicap", label: "Away +0.5", scope: "full_time", line: -0.5, selection: "away", probability: 0.42, provenance: "model" },
              { key: "ht_ft.home.home", family: "ht_ft", label: "1/1", scope: "half_to_full", line: null, selection: "home_home", probability: 0.24, provenance: "modelled" },
            ],
          }}
        />
      </I18nProvider>,
    );
    expect(chipLabels(container)).toEqual([
      "Chủ nhà thắng 68%",
      "Trên 1,5 bàn thắng 80%",
      "Dưới 2,5 bàn thắng 41%",
      "Cả hai đội ghi bàn 68%",
      "Khách +0,5 42%",
      "1 / 1 24%",
    ]);
  });

  it("translates the legacy fixed set too", () => {
    const { container } = render(
      <I18nProvider language="vi">
        <PredictionChips predictions={{ home: 0.58, away: 0.18, btts_yes: 0.55, over_1_5: 0.82, over_2_5: 0.61 }} />
      </I18nProvider>,
    );
    expect(chipLabels(container)).toEqual([
      "Chủ nhà thắng 58%",
      "Hoà —",
      "Khách thắng 18%",
      "Cả hai đội ghi bàn 55%",
      "Trên 1,5 bàn thắng 82%",
      "Trên 2,5 bàn thắng 61%",
    ]);
  });

  it("explains in the tooltip where a number came from", () => {
    render(
      <PredictionChips
        predictions={{
          selected: [
            { key: "a", label: "O1.5", scope: "full_time", probability: 0.8, provenance: "model" },
            { key: "b", label: "1/1", scope: "half_to_full", probability: 0.62, provenance: "modelled" },
            { key: "c", label: "Home -1", scope: "full_time", probability: 0.66, provenance: "model", push: 0.27 },
          ],
        }}
      />
    );
    const [measured, assumed, pushed] = [...document.querySelectorAll(".pred-chip")];
    expect(measured.getAttribute("title")).toContain("from the model's goal distribution");
    expect(assumed.getAttribute("title")).toContain("half time / full time");
    expect(assumed.getAttribute("title")).toContain("assumed");
    expect(pushed.getAttribute("title")).toContain("27% push");
  });

  it("scales tone within the decisive band", () => {
    render(
      <PredictionChips
        predictions={{
          selected: [
            { key: "a", label: "A", scope: "full_time", probability: 0.8, provenance: "model" },
            { key: "b", label: "B", scope: "full_time", probability: 0.62, provenance: "model" },
          ],
        }}
      />
    );
    const [strong, mid] = [...document.querySelectorAll(".pred-chip")];
    expect(strong.className).toContain("chip-strong");
    expect(mid.className).toContain("chip-mid");
  });

  it("ignores malformed selected entries", () => {
    const { container } = render(
      <PredictionChips
        predictions={{
          selected: [null, { label: "bad" }, { label: "ok", scope: "full_time", probability: 0.7, provenance: "model" }],
        }}
      />
    );
    expect(chipLabels(container)).toEqual(["ok 70%"]);
  });

  it("renders the confidence and as-of meta line", () => {
    render(<PredictionChips predictions={{ selected: [] }} confidence={0.61} dataThrough="2026-01-29" />);
    expect(screen.getByText(/conf 61%/)).toBeInTheDocument();
    expect(screen.getByText(/as of 2026-01-29/)).toBeInTheDocument();
  });

  it("survives being handed nothing at all", () => {
    const { container } = render(<PredictionChips predictions={null} />);
    expect(container.querySelectorAll(".pred-chip").length).toBe(6);
  });
});

describe("PredictionChips with onSelect", () => {
  const derived = {
    selected: [
      { key: "ft.totals.over_1.5", label: "O1.5", scope: "full_time", probability: 0.8, provenance: "model" },
      { key: "ht.result.home", label: "1", scope: "half_time", probability: 0.62, provenance: "modelled" },
    ],
  };

  it("hands the clicked market back", async () => {
    const onSelect = vi.fn();
    render(<PredictionChips predictions={derived} onSelect={onSelect} />);

    await userEvent.click(screen.getByRole("button", { name: /O1\.5 80%/ }));
    expect(onSelect).toHaveBeenCalledWith(expect.objectContaining({ key: "ft.totals.over_1.5" }));
  });

  it("leaves the legacy fixed chips inert, since they are not markets", () => {
    const onSelect = vi.fn();
    render(<PredictionChips predictions={{ home: 0.58, away: 0.18 }} onSelect={onSelect} />);
    // "1"/"2" are readable off the summary, not a market key the backend can
    // explain, so offering to open one would only produce an error.
    expect(screen.queryAllByRole("button")).toHaveLength(0);
  });

  it("stays plain spans when no handler is passed", () => {
    render(<PredictionChips predictions={derived} />);
    expect(screen.queryAllByRole("button")).toHaveLength(0);
  });
});
