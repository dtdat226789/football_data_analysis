import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

import ChartLightbox from "./ChartLightbox.jsx";

describe("ChartLightbox", () => {
  it("shows the image and title in a dialog", () => {
    render(<ChartLightbox src="/api/v1/analysis/premier/charts/avg_goals.png" title="avg goals" />);

    expect(screen.getByRole("dialog")).toBeInTheDocument();
    expect(screen.getByAltText("avg goals")).toHaveAttribute(
      "src",
      "/api/v1/analysis/premier/charts/avg_goals.png",
    );
    expect(screen.getByRole("button", { name: "Close" })).toBeInTheDocument();
  });

  it("closes when Escape is pressed", () => {
    const onClose = vi.fn();
    render(<ChartLightbox src="/x.png" title="Chart" onClose={onClose} />);

    fireEvent.keyDown(window, { key: "Escape" });
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it("closes when the backdrop is clicked", () => {
    const onClose = vi.fn();
    const { container } = render(<ChartLightbox src="/x.png" title="Chart" onClose={onClose} />);

    fireEvent.click(container.querySelector(".lightbox-backdrop"));
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it("does not close when the frame (image area) is clicked", () => {
    const onClose = vi.fn();
    const { container } = render(<ChartLightbox src="/x.png" title="Chart" onClose={onClose} />);

    fireEvent.click(container.querySelector(".lightbox-frame"));
    expect(onClose).not.toHaveBeenCalled();
  });
});