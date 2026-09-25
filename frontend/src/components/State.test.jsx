import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { Empty, ErrorBox, Loading } from "./State.jsx";

describe("State components", () => {
  it("Loading shows the default label", () => {
    render(<Loading />);
    expect(screen.getByText("Loading…")).toBeInTheDocument();
  });

  it("Loading shows a custom label", () => {
    render(<Loading label="booting" />);
    expect(screen.getByText("booting")).toBeInTheDocument();
  });

  it("ErrorBox shows the provided message", () => {
    render(<ErrorBox error="kaboom" />);
    expect(screen.getByText("kaboom")).toBeInTheDocument();
  });

  it("ErrorBox falls back to a default message", () => {
    render(<ErrorBox />);
    expect(screen.getByText("Something went wrong.")).toBeInTheDocument();
  });

  it("Empty renders its children", () => {
    render(
      <Empty>
        <span>nothing here</span>
      </Empty>,
    );
    expect(screen.getByText("nothing here")).toBeInTheDocument();
  });
});