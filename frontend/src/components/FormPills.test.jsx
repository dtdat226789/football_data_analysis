import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { FormPills } from "./FormPills.jsx";

describe("FormPills", () => {
  it("renders one pill per result with its class and tooltip", () => {
    render(
      <FormPills
        results={[
          { team_result: "W", home_team: "Arsenal", home_score: 2, away_score: 1, away_team: "Chelsea" },
          { team_result: "D", home_team: "Liverpool", home_score: 1, away_score: 1, away_team: "Arsenal" },
        ]}
      />,
    );

    const pills = screen.getAllByText(/^[WDL]$/);
    expect(pills).toHaveLength(2);
    expect(pills[0]).toHaveClass("pill", "W");
    expect(pills[0]).toHaveAttribute("title", "Arsenal 2-1 Chelsea");
    expect(pills[1]).toHaveClass("pill", "D");
  });

  it("renders an em dash when there are no results", () => {
    render(<FormPills results={[]} />);
    expect(screen.getByText("—")).toBeInTheDocument();
  });

  it("renders an em dash when results are missing", () => {
    render(<FormPills />);
    expect(screen.getByText("—")).toBeInTheDocument();
  });
});