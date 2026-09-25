import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import ChartGrid from "./ChartGrid.jsx";

describe("ChartGrid", () => {
  it("renders a card per chart with a readable caption", () => {
    render(<ChartGrid league="premier" charts={["avg_goals.png", "home_away.png"]} />);

    expect(screen.getByText("avg goals")).toBeInTheDocument();
    expect(screen.getByText("home away")).toBeInTheDocument();
    const imgs = document.querySelectorAll(".chart-grid img");
    expect(imgs).toHaveLength(2);
    expect(imgs[0]).toHaveAttribute("src", "/api/v1/analysis/premier/charts/avg_goals.png");
  });

  it("opens a full-screen lightbox when a chart is selected", () => {
    render(<ChartGrid league="premier" charts={["avg_goals.png"]} />);

    fireEvent.click(screen.getByRole("button", { name: /View avg goals full screen/ }));

    expect(screen.getByRole("dialog")).toBeInTheDocument();
    expect(screen.getByAltText("avg goals")).toBeInTheDocument();
  });

  it("closes the lightbox on Escape", () => {
    render(<ChartGrid league="premier" charts={["avg_goals.png"]} />);

    fireEvent.click(screen.getByRole("button", { name: /View avg goals full screen/ }));
    expect(screen.getByRole("dialog")).toBeInTheDocument();

    fireEvent.keyDown(window, { key: "Escape" });
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });
});