import { screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { renderPage } from "../test/render.jsx";
import { TeamLink } from "./TeamLink.jsx";

describe("TeamLink", () => {
  it("renders a router link to the encoded team name", () => {
    renderPage(<TeamLink name="Arsenal FC" />);

    const link = screen.getByRole("link", { name: "Arsenal FC" });
    expect(link).toHaveAttribute("href", "/teams/Arsenal%20FC");
    expect(link).toHaveClass("link");
  });

  it("renders an em dash when there is no team name", () => {
    renderPage(<TeamLink name="" />);

    expect(screen.getByText("—")).toBeInTheDocument();
  });
});