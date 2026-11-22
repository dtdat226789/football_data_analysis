import { fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";

import { I18nProvider } from "./i18n/I18nProvider.jsx";
import { ErrorBox, Loading } from "./components/State.jsx";
import ChartGrid from "./components/ChartGrid.jsx";
import { renderPage } from "./test/render.jsx";

afterEach(() => {
  document.documentElement.lang = "en";
  document.getElementById("root")?.remove();
});

describe("accessibility", () => {
  it("keeps the document language in sync with the selected language", () => {
    render(
      <I18nProvider language="vi">
        <div />
      </I18nProvider>,
    );

    expect(document.documentElement.lang).toBe("vi-VN");
  });

  it("announces loading and error states", () => {
    renderPage(<Loading />);
    expect(screen.getByRole("status")).toHaveAttribute("aria-live", "polite");

    renderPage(<ErrorBox error="Upstream failure" />);
    expect(screen.getByRole("alert")).toHaveTextContent("Upstream failure");
  });

  it("makes the background inert while the chart dialog is open", () => {
    const root = document.createElement("div");
    root.id = "root";
    document.body.appendChild(root);
    renderPage(<ChartGrid league="premier" charts={["avg_goals.png"]} />);

    fireEvent.click(screen.getByRole("button", { name: /View avg goals full screen/ }));
    expect(root).toHaveAttribute("inert");
    expect(screen.getByRole("dialog")).toHaveAttribute("aria-modal", "true");

    fireEvent.keyDown(window, { key: "Escape" });
    expect(root).not.toHaveAttribute("inert");
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });
});
