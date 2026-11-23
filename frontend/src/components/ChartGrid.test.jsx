import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import ChartGrid from "./ChartGrid.jsx";

const reports = {
  goals_analysis: {
    goals_distribution: {
      buckets: [
        { goals: 0, count: 12 },
        { goals: 1, count: 25 },
      ],
    },
  },
};

describe("ChartGrid", () => {
  it("renders a card per chart with a readable caption", () => {
    render(<ChartGrid league="premier" charts={["avg_goals.png", "home_away.png"]} />);

    expect(screen.getByText("avg goals")).toBeInTheDocument();
    expect(screen.getByText("home away")).toBeInTheDocument();
    const imgs = document.querySelectorAll(".chart-grid img");
    expect(imgs).toHaveLength(2);
    expect(imgs[0]).toHaveAttribute("src", "/api/v1/analysis/premier/charts/avg_goals.png");
    expect(imgs[0]).toHaveAttribute("width", "640");
    expect(imgs[0]).toHaveAttribute("height", "320");
  });

  it("ignores chart names that are not plain PNG files", () => {
    render(<ChartGrid league="premier" charts={["../../secret", "avg_goals.png"]} />);

    expect(document.querySelectorAll(".chart-grid img")).toHaveLength(1);
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

  it("renders an interactive chart when the matching report data is available", () => {
    render(
      <ChartGrid
        league="premier"
        charts={["goals_analysis_distribution.png"]}
        reports={reports}
      />,
    );

    expect(
      screen.getByRole("img", { name: /Interactive chart: goals analysis distribution/ }),
    ).toBeInTheDocument();
    expect(document.querySelectorAll(".chart-grid img")).toHaveLength(0);
    expect(screen.getByText("Built from the latest analysis snapshot.")).toBeInTheDocument();
  });

  it("shows and clears a tooltip when a chart mark is focused", () => {
    render(
      <ChartGrid
        league="premier"
        charts={["goals_analysis_distribution.png"]}
        reports={reports}
      />,
    );

    const mark = screen.getByLabelText("0: 12 matches");
    fireEvent.focus(mark);
    expect(screen.getByRole("status")).toHaveTextContent("0: 12 matches");

    fireEvent.blur(mark);
    expect(screen.queryByRole("status")).not.toBeInTheDocument();
  });

  it("opens the image lightbox from an interactive chart card", () => {
    render(
      <ChartGrid
        league="premier"
        charts={["goals_analysis_distribution.png"]}
        reports={reports}
      />,
    );

    fireEvent.click(
      screen.getByRole("button", { name: /View goals analysis distribution full screen/ }),
    );
    expect(screen.getByRole("dialog")).toBeInTheDocument();
  });
});