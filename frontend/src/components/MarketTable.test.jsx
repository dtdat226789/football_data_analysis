import { render, screen, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";
import { qsa } from "../test/dom.js";
import MarketTable from "./MarketTable.jsx";
import { fixtureMarkets, SELECTED_KEYS } from "../test/fixtures.js";

const selected = fixtureMarkets.filter((m) => SELECTED_KEYS.includes(m.key));

const groupNames = (container) =>
  [...container.querySelectorAll(".market-group h4")].map((el) => el.textContent);

/** The market label only — the "featured" flag is a sibling span in the same cell. */
const rowLabels = (container) =>
  [...qsa(container, "tbody tr td:first-child")].map(
    (el) => el.firstChild.textContent.trim()
  );

describe("MarketTable", () => {
  it("groups markets by family in a sensible order", () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    const groups = groupNames(container);
    expect(groups[0]).toBe("Result");
    expect(groups[1]).toBe("Double chance");
    expect(groups).toContain("Goals (over/under)");
    expect(groups).toContain("Asian handicap");
    expect(groups).toContain("Correct score");
    expect(groups).toContain("Half time / full time");
  });

  it("orders lines within a family", async () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    await userEvent.click(screen.getByRole("button", { name: "Full time" }));
    const totals = [...container.querySelectorAll(".market-group")].find(
      (g) => g.querySelector("h4").textContent === "Goals (over/under)"
    );
    expect(rowLabels(totals)).toEqual(["O1.5", "U1.5", "O2.5", "U2.5"]);
  });

  it("puts the tighter half-time line ahead of the full-time ones", () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    const totals = [...container.querySelectorAll(".market-group")].find(
      (g) => g.querySelector("h4").textContent === "Goals (over/under)"
    );
    expect(rowLabels(totals)[0]).toBe("O0.5");
  });

  it("tags every row with its source", () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    const cells = [...qsa(container, "tbody tr")].map((tr) =>
      within(tr).getAllByRole("cell")[2].textContent.trim()
    );
    expect(cells.filter((c) => c === "model").length).toBeGreaterThan(0);
    expect(cells.filter((c) => c === "assumed").length).toBeGreaterThan(0);
  });

  it("counts the assumed markets in the heading", () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    const heading = container.querySelector("h3").textContent;
    expect(heading).toContain("Markets");
    expect(heading).toContain(`${fixtureMarkets.length} derived`);
    expect(heading).toContain(
      `${fixtureMarkets.filter((m) => m.provenance === "modelled").length} assumed`
    );
  });

  it("marks the markets that drive the chips as featured", () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    const featured = [...qsa(container, "tr.featured td:first-child")].map(
      (el) => el.firstChild.textContent.trim()
    );
    expect(featured).toEqual(["O1.5", "U2.5", "Away +0.5", "1/1"]);  });

  it("shows the push probability on a handicap that can refund", () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    const row = [...qsa(container, "tbody tr")].find((tr) =>
      tr.textContent.includes("Home -1")
    );
    expect(within(row).getByText(/27\.0% push/)).toBeInTheDocument();
  });

  it("omits the push note when the line cannot push", () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    const row = [...qsa(container, "tbody tr")].find((tr) =>
      tr.textContent.includes("Home -0.5")
    );
    expect(row.textContent).not.toContain("push");
  });

  it("filters to full time", async () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    await userEvent.click(screen.getByRole("button", { name: "Full time" }));
    const scopes = [...qsa(container, "tbody tr")].map((tr) =>
      within(tr).getAllByRole("cell")[1].textContent.trim()
    );
    expect(scopes.every((s) => s === "Full time")).toBe(true);
    expect(rowLabels(container)).not.toContain("1/1");
  });

  it("filters to half time", async () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    await userEvent.click(screen.getByRole("button", { name: "Half time" }));
    const scopes = [...qsa(container, "tbody tr")].map((tr) =>
      within(tr).getAllByRole("cell")[1].textContent.trim()
    );
    // HT/FT is neither full time nor half time, so it drops out of both.
    expect(scopes.every((s) => s === "Half time")).toBe(true);
    expect(rowLabels(container)).toEqual(["1", "O0.5"]);
  });

  it("filters to assumed markets only", async () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    await userEvent.click(screen.getByRole("button", { name: "Assumed only" }));
    const sources = [...qsa(container, "tbody tr")].map((tr) =>
      within(tr).getAllByRole("cell")[2].textContent.trim()
    );
    expect(sources.every((s) => s === "assumed")).toBe(true);
    expect(rowLabels(container)).toContain("1/1");
  });

  it("shows which filter is active", async () => {
    render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    await userEvent.click(screen.getByRole("button", { name: "Assumed only" }));
    expect(screen.getByRole("button", { name: "Assumed only" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByRole("button", { name: "All" })).toHaveAttribute("aria-pressed", "false");
  });

  it("says so when a filter matches nothing", async () => {
    const onlyFullTime = fixtureMarkets.filter((m) => m.scope === "full_time");
    render(<MarketTable markets={onlyFullTime} selected={[]} />);
    await userEvent.click(screen.getByRole("button", { name: "Half time" }));
    expect(screen.getByText("No markets match this filter.")).toBeInTheDocument();
  });

  it("renders nothing without markets", () => {
    const { container } = render(<MarketTable markets={[]} />);
    expect(container).toBeEmptyDOMElement();
    expect(render(<MarketTable markets={null} />).container).toBeEmptyDOMElement();
    expect(render(<MarketTable />).container).toBeEmptyDOMElement();
  });

  it("tolerates malformed rows and a missing selected list", () => {
    const messy = [...fixtureMarkets, null, { key: "bad" }, { label: "no probability" }];
    const { container } = render(<MarketTable markets={messy} />);
    expect(rowLabels(container).length).toBe(fixtureMarkets.length);
    expect(container.querySelectorAll("tr.featured").length).toBe(0);
  });
});

describe("MarketTable with onSelect", () => {
  it("hands the clicked row back so its explanation can be opened", async () => {
    const onSelect = vi.fn();
    render(<MarketTable markets={fixtureMarkets} selected={selected} onSelect={onSelect} />);

    await userEvent.click(screen.getByRole("button", { name: "Home -1" }));
    expect(onSelect).toHaveBeenCalledTimes(1);
    // The whole row, not just its label, so the caller can key off `key`.
    expect(onSelect).toHaveBeenCalledWith(
      expect.objectContaining({ key: "ft.asian_handicap.-1_home", line: -1, family: "asian_handicap" }),
    );
  });

  it("keeps every row reachable, not just the featured ones", async () => {
    const onSelect = vi.fn();
    const { container } = render(
      <MarketTable markets={fixtureMarkets} selected={selected} onSelect={onSelect} />,
    );
    // A correct score is not a chip, but it is still a market a reader may want
    // explained, so it has to open too.
    await userEvent.click(screen.getByRole("button", { name: "2-1" }));
    expect(onSelect).toHaveBeenCalledWith(expect.objectContaining({ key: "ft.correct_score.2_1" }));
    expect(container.querySelectorAll(".market-open").length).toBe(fixtureMarkets.length);
  });

  it("stays plain text when no handler is passed", () => {
    const { container } = render(<MarketTable markets={fixtureMarkets} selected={selected} />);
    expect(container.querySelectorAll(".market-open").length).toBe(0);
  });
});
