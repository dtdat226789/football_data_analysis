import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import ErrorBoundary from "./ErrorBoundary.jsx";

function Boom({ fail = true }) {
  if (fail) throw new Error("render failed");
  return null;
}

describe("ErrorBoundary", () => {
  it("shows a translated fallback instead of a blank page", () => {
    const silence = (event) => event.preventDefault();
    window.addEventListener("error", silence);
    try {
      render(
        <ErrorBoundary>
          <Boom />
        </ErrorBoundary>,
        { onRecoverableError: () => {} },
      );

      expect(screen.getByRole("alert")).toHaveTextContent("This section could not be displayed");
      expect(screen.getByRole("button", { name: "Reload this page" })).toBeInTheDocument();
    } finally {
      window.removeEventListener("error", silence);
    }
  });
});
