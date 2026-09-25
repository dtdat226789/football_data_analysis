import { render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { BarList, Donut, StatCard } from "./Charts.jsx";

describe("Charts", () => {
  it("BarList renders values with the maximum bar at full width", () => {
    const { container } = render(
      <BarList
        title="Points"
        data={[
          { label: "2023-2024", value: 60 },
          { label: "2024-2025", value: 90 },
        ]}
      />,
    );

    expect(screen.getByText("Points")).toBeInTheDocument();
    expect(screen.getByText("2023-2024")).toBeInTheDocument();
    expect(screen.getByText("90")).toBeInTheDocument();
    const fills = container.querySelectorAll(".bar-fill");
    expect(fills).toHaveLength(2);
    expect(fills[1].style.width).toBe("100%");
  });

  it("BarList applies a custom format function", () => {
    render(
      <BarList
        data={[{ label: "Home", value: 48.7 }]}
        format={(v) => `${v}%`}
      />,
    );
    expect(screen.getByText("48.7%")).toBeInTheDocument();
  });

  it("Donut renders segment labels and values", () => {
    render(
      <Donut
        title="W / D / L"
        segments={[
          { label: "Won", value: 10, color: "#36d399" },
          { label: "Drawn", value: 5, color: "#fbbf24" },
          { label: "Lost", value: 5, color: "#f87171" },
        ]}
        center="20 matches"
      />,
    );

    expect(screen.getByText("W / D / L")).toBeInTheDocument();
    expect(screen.getByText("Won: 10")).toBeInTheDocument();
    expect(screen.getByText("Drawn: 5")).toBeInTheDocument();
    const legend = screen.getByText("Won: 10").closest("ul");
    expect(within(legend).getByText("Lost: 5")).toBeInTheDocument();
  });

  it("Donut shows only the total center when all values are zero", () => {
    render(
      <Donut
        segments={[
          { label: "Won", value: 0, color: "#36d399" },
          { label: "Lost", value: 0, color: "#f87171" },
        ]}
        center="0"
      />,
    );
    expect(screen.getByText("Won: 0")).toBeInTheDocument();
    expect(screen.getByText("0")).toBeInTheDocument();
  });

  it("StatCard renders label, value and optional sub", () => {
    render(<StatCard label="Points" value="85" sub="2.21 PPG" />);
    expect(screen.getByText("Points")).toBeInTheDocument();
    expect(screen.getByText("85")).toBeInTheDocument();
    expect(screen.getByText("2.21 PPG")).toBeInTheDocument();
  });
});