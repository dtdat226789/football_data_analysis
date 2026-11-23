import { act, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { renderPage } from "../test/render.jsx";
import Countdown from "./Countdown.jsx";

const KICKOFF = Date.parse("2026-09-18T19:00:00Z");

describe("Countdown", () => {
  beforeEach(() => {
    window.localStorage.setItem("fd.timezone", "UTC");
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
    window.localStorage.clear();
  });

  it("shows hours and minutes above an hour and ticks once a second", () => {
    vi.setSystemTime(new Date(KICKOFF - 90 * 60_000));
    renderPage(<Countdown date="2026-09-18" time="19:00" />);

    const chip = screen.getByRole("timer", { name: "Time until kickoff at 19:00" });
    expect(chip).toHaveTextContent("1h 30m");
    expect(chip).toHaveClass("tabular");

    act(() => {
      vi.advanceTimersByTime(3100);
    });
    expect(chip).toHaveTextContent("1h 29m");
  });

  it("shows days and hours for a longer wait", () => {
    vi.setSystemTime(new Date(KICKOFF - (26 * 3600_000 + 61_000)));
    renderPage(<Countdown date="2026-09-18" time="19:00" />);

    expect(screen.getByRole("timer")).toHaveTextContent("1d 2h");
  });

  it("switches to HH:MM:SS below an hour", () => {
    vi.setSystemTime(new Date(KICKOFF - 65_000));
    renderPage(<Countdown date="2026-09-18" time="19:00" />);

    expect(screen.getByRole("timer")).toHaveTextContent("00:01:05");
  });

  it("hides once the match has started without announcing ticks", () => {
    vi.setSystemTime(new Date(KICKOFF - 65_000));
    const { unmount } = renderPage(<Countdown date="2026-09-18" time="19:00" />);
    expect(screen.getByRole("timer")).not.toHaveAttribute("aria-live");
    unmount();

    vi.setSystemTime(new Date(KICKOFF));
    renderPage(<Countdown date="2026-09-18" time="19:00" />);
    expect(screen.queryByRole("timer")).not.toBeInTheDocument();
  });

  it("shares one ticker across every row", () => {
    vi.setSystemTime(new Date(KICKOFF - 65_000));
    const setIntervalSpy = vi.spyOn(globalThis, "setInterval");
    renderPage(
      <>
        <Countdown date="2026-09-18" time="19:00" />
        <Countdown date="2026-09-19" time="19:00" />
      </>,
    );

    expect(setIntervalSpy).toHaveBeenCalledTimes(1);
    expect(screen.getAllByRole("timer")).toHaveLength(2);
    setIntervalSpy.mockRestore();
  });
});
