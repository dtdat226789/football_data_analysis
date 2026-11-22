import { screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import MatchInsights from "./MatchInsights.jsx";
import { matchInsights } from "../test/fixtures.js";
import { renderPage } from "../test/render.jsx";

describe("MatchInsights", () => {
  it("renders the pre-match, model and head-to-head panels", () => {
    renderPage(<MatchInsights insights={matchInsights} homeName="Arsenal" awayName="Chelsea" />);

    expect(screen.getByRole("heading", { name: /Pre-match context/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /Model view/ })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /Head to head/ })).toBeInTheDocument();
    expect(screen.getByText(/Arsenal 1W 1D 0L Chelsea/)).toBeInTheDocument();
  });

  it("does not render when the response has no usable sections", () => {
    const { container } = renderPage(
      <MatchInsights insights={{}} homeName="Arsenal" awayName="Chelsea" />,
    );

    expect(container).toBeEmptyDOMElement();
  });

  it("degrades a malformed response to an empty state instead of throwing", () => {
    const { container } = renderPage(
      <MatchInsights
        insights={{ pre_match: { groups: null }, head_to_head: { matches: "bad" } }}
        homeName="Arsenal"
        awayName="Chelsea"
      />,
    );

    expect(container).toBeEmptyDOMElement();
  });
});
