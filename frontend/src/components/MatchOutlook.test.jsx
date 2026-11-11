import { render, screen } from "@testing-library/react";
import MatchOutlook from "./MatchOutlook.jsx";
import { I18nProvider } from "../i18n/I18nProvider.jsx";

const chipLabels = (container) =>
  [...container.querySelectorAll(".pred-chip")].map((el) => el.textContent.trim());

describe("MatchOutlook", () => {
  it("leads with goal-total probabilities and the model confidence", () => {
    const { container } = render(
      <MatchOutlook
        predictions={{ over_1_5: 0.82, over_2_5: 0.61, confidence: 0.58, data_through: "2026-01-29" }}
      />,
    );
    expect(chipLabels(container)).toEqual(["2+ goals 82%", "3+ goals 61%"]);
    expect(screen.getByText(/Model confidence 58%/)).toBeInTheDocument();
    expect(screen.getByText(/as of 2026-01-29/)).toBeInTheDocument();
  });

  it("reads the dotted keys of a raw calibrated block", () => {
    const { container } = render(
      <MatchOutlook predictions={{ "over_1.5": 0.8, "over_2.5": 0.57 }} />,
    );
    expect(chipLabels(container)).toEqual(["2+ goals 80%", "3+ goals 57%"]);
  });

  it("omits missing goal totals but keeps the confidence line", () => {
    const { container } = render(<MatchOutlook predictions={{ confidence: 0.44 }} />);
    expect(chipLabels(container)).toEqual([]);
    expect(screen.getByText(/Model confidence 44%/)).toBeInTheDocument();
  });

  it("renders nothing when handed nothing at all", () => {
    const { container } = render(<MatchOutlook predictions={null} />);
    expect(container.querySelectorAll(".pred-chip").length).toBe(0);
  });

  it("translates the outlook into Vietnamese", () => {
    const { container } = render(
      <I18nProvider language="vi">
        <MatchOutlook predictions={{ over_1_5: 0.82, over_2_5: 0.61, confidence: 0.58 }} />
      </I18nProvider>,
    );
    expect(chipLabels(container)).toEqual(["2+ bàn thắng 82%", "3+ bàn thắng 61%"]);
    expect(screen.getByText(/Độ tin cậy mô hình 58%/)).toBeInTheDocument();
  });

  it("scales tone with the probability", () => {
    render(<MatchOutlook predictions={{ over_1_5: 0.82, over_2_5: 0.34 }} />);
    const [strong, weak] = [...document.querySelectorAll(".pred-chip")];
    expect(strong.className).toContain("chip-strong");
    expect(weak.className).toContain("chip-weak");
  });
});
