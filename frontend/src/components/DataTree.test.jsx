import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import Tree from "./DataTree.jsx";

describe("DataTree", () => {
  it("renders integers and strings as-is, floats to 2 decimals", () => {
    render(<Tree value={42} />);
    expect(screen.getByText("42")).toBeInTheDocument();

    const { rerender } = render(<Tree value={3.14159} />);
    expect(screen.getByText("3.14")).toBeInTheDocument();

    rerender(<Tree value={"text"} />);
    expect(screen.getByText("text")).toBeInTheDocument();
  });

  it("renders booleans as yes/no badges", () => {
    render(<Tree value={{ on: true, off: false }} />);
    expect(screen.getByText("yes")).toBeInTheDocument();
    expect(screen.getByText("no")).toBeInTheDocument();
  });

  it("renders null/undefined/missing as an em dash", () => {
    render(<Tree value={null} />);
    expect(screen.getByText("—")).toBeInTheDocument();
  });

  it("renders a plain object as key/value table rows", () => {
    render(<Tree value={{ team: "Arsenal", points: 71 }} />);

    expect(screen.getByText("team")).toBeInTheDocument();
    expect(screen.getByText("Arsenal")).toBeInTheDocument();
    expect(screen.getByText("points")).toBeInTheDocument();
    expect(screen.getByText("71")).toBeInTheDocument();
  });

  it("renders an array of objects as a table with a header row", () => {
    render(
      <Tree
        value={[
          { team: "Arsenal", played: 38 },
          { team: "Chelsea", played: 38 },
        ]}
      />,
    );

    const headers = ["team", "played"];
    for (const header of headers) {
      expect(screen.getByRole("columnheader", { name: header })).toBeInTheDocument();
    }
    expect(screen.getByText("Arsenal")).toBeInTheDocument();
    expect(screen.getByText("Chelsea")).toBeInTheDocument();
  });

  it("shows a placeholder for a missing cell in an object array", () => {
    render(<Tree value={[{ a: 1 }, { a: 2, b: "y" }]} />);

    expect(screen.getByRole("columnheader", { name: "b" })).toBeInTheDocument();
    expect(screen.getAllByText("—").length).toBeGreaterThanOrEqual(1);
  });

  it("renders an empty array as none", () => {
    render(<Tree value={[]} />);
    expect(screen.getByText("none")).toBeInTheDocument();
  });
});