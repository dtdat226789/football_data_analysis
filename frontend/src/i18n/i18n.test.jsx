import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it } from "vitest";

import { I18nProvider } from "./I18nProvider.jsx";
import SettingsControls from "./SettingsControls.jsx";
import { useFormatters } from "./useFormatters.js";
import { renderPage } from "../test/render.jsx";

/**
 * A page-shaped slice that reads every display concern through the real
 * provider: a sentence, a kickoff's day+clock (which the zone moves), and the
 * locale-aware number/percent punctuation.
 */
function Probe() {
  const { t, kickoffDay, kickoffTime, num, pct } = useFormatters();
  return (
    <section>
      <p data-testid="loading">{t("common.loading")}</p>
      <p data-testid="kickoff">
        {kickoffDay("2026-09-18", "19:00")} {kickoffTime("2026-09-18", "19:00")}
      </p>
      <p data-testid="number">{num(1234.5)}</p>
      <p data-testid="percent">{pct(0.667)}</p>
      <p data-testid="missing">{t("settings.__never_a_key__")}</p>
    </section>
  );
}

function renderDefault() {
  return renderPage(
    <>
      <SettingsControls />
      <Probe />
    </>,
  );
}

describe("i18n provider and settings", () => {
  beforeEach(() => {
    window.localStorage.clear();
  });

  it("defaults to English and Hanoi (UTC+7)", async () => {
    renderDefault();

    expect(screen.getByTestId("loading")).toHaveTextContent("Loading…");
    // friday 19:00 UTC is saturday 02:00 in Hanoi
    expect(screen.getByTestId("kickoff")).toHaveTextContent("19/09/2026 02:00");
    expect(screen.getByTestId("number")).toHaveTextContent("1,234.5");
    expect(screen.getByTestId("percent")).toHaveTextContent("66.7%");
    expect(screen.getByLabelText("Language")).toBeInTheDocument();
    expect(screen.getByLabelText("Time zone")).toBeInTheDocument();
  });

  it("switches the whole page to Vietnamese, punctuation included", async () => {
    renderDefault();

    await userEvent.selectOptions(screen.getByLabelText("Language"), "vi");

    expect(screen.getByTestId("loading")).toHaveTextContent("Đang tải…");
    expect(screen.getByTestId("kickoff")).toHaveTextContent("19/09/2026 02:00");
    expect(screen.getByTestId("number")).toHaveTextContent("1.234,5");
    expect(screen.getByTestId("percent")).toHaveTextContent("66,7%");
    expect(screen.getByLabelText("Ngôn ngữ")).toBeInTheDocument();
    expect(screen.getByLabelText("Múi giờ")).toBeInTheDocument();
  });

  it("moves the kickoff clock and day when the zone changes", async () => {
    renderDefault();

    // UTC keeps the kickoff on its own day.
    await userEvent.selectOptions(screen.getByLabelText("Time zone"), "UTC");
    expect(screen.getByTestId("kickoff")).toHaveTextContent("18/09/2026 19:00");
    expect(screen.getByTestId("loading")).toHaveTextContent("Loading…");

    // Back to Hanoi, the fixture rolls onto Saturday morning again.
    await userEvent.selectOptions(screen.getByLabelText("Time zone"), "Asia/Ho_Chi_Minh");
    expect(screen.getByTestId("kickoff")).toHaveTextContent("19/09/2026 02:00");
  });

  it("persists the language and zone across a remount", async () => {
    const { unmount } = renderDefault();

    await userEvent.selectOptions(screen.getByLabelText("Language"), "vi");
    await userEvent.selectOptions(screen.getByLabelText("Múi giờ"), "Asia/Singapore");
    unmount();

    // A fresh provider reads the stored choices instead of the browser defaults.
    renderDefault();
    expect(screen.getByTestId("loading")).toHaveTextContent("Đang tải…");
    // Friday 19:00 UTC is Saturday 03:00 in UTC+8 Singapore.
    expect(screen.getByTestId("kickoff")).toHaveTextContent("19/09/2026 03:00");
  });

  it("honours language and zone forced through props", () => {
    render(
      <I18nProvider language="vi" timeZone="UTC">
        <Probe />
      </I18nProvider>,
    );

    expect(screen.getByTestId("loading")).toHaveTextContent("Đang tải…");
    expect(screen.getByTestId("kickoff")).toHaveTextContent("18/09/2026 19:00");
  });

  it("falls back to the key itself when no catalogue has it", async () => {
    renderDefault();

    expect(screen.getByTestId("missing")).toHaveTextContent("settings.__never_a_key__");

    await userEvent.selectOptions(screen.getByLabelText("Language"), "vi");
    expect(screen.getByTestId("missing")).toHaveTextContent("settings.__never_a_key__");
  });

  it("lists the Viet-named settings and the short zone pick list", async () => {
    renderDefault();

    const zone = /** @type {HTMLSelectElement} */ (screen.getByLabelText("Time zone"));
    expect(zone).toHaveValue("Asia/Ho_Chi_Minh");
    const zones = [...zone.options].map((o) => o.value);
    expect(zones).toEqual([
      "Asia/Ho_Chi_Minh",
      "Asia/Singapore",
      "Asia/Tokyo",
      "Europe/London",
      "UTC",
    ]);

    const language = /** @type {HTMLSelectElement} */ (screen.getByLabelText("Language"));
    expect([...language.options].map((o) => o.textContent)).toEqual(["English", "Tiếng Việt"]);
  });
});