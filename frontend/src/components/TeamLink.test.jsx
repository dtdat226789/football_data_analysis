import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { describe, expect, it } from "vitest";

import { TeamLink } from "./TeamLink.jsx";

describe("TeamLink", () => {
  it("renders a router link to the encoded team name", () => {
    render(
      <MemoryRouter>
        <TeamLink name="Arsenal FC" />
      </MemoryRouter>,
    );

    const link = screen.getByRole("link", { name: "Arsenal FC" });
    expect(link).toHaveAttribute("href", "/teams/Arsenal%20FC");
    expect(link).toHaveClass("link");
  });

  it("renders an em dash when there is no team name", () => {
    render(
      <MemoryRouter>
        <TeamLink name="" />
      </MemoryRouter>,
    );

    expect(screen.getByText("—")).toBeInTheDocument();
  });
});