import { describe, expect, it } from "vitest";
import { timeToKickoff } from "./countdown.js";

const KICKOFF = Date.parse("2026-09-18T19:00:00Z");
const before = (ms) => KICKOFF - ms;

describe("timeToKickoff", () => {
  it("splits a long wait into days and hours", () => {
    expect(timeToKickoff("2026-09-18", "19:00", before(26 * 3600_000 + 61_000))).toEqual({
      started: false,
      totalSeconds: 93661,
      days: 1,
      hours: 2,
      minutes: 1,
      seconds: 1,
    });
  });

  it("splits a short wait into hours and minutes", () => {
    expect(timeToKickoff("2026-09-18", "19:00", before(90 * 60_000))).toEqual({
      started: false,
      totalSeconds: 5400,
      days: 0,
      hours: 1,
      minutes: 30,
      seconds: 0,
    });
  });

  it("keeps a sub-hour wait in seconds", () => {
    expect(timeToKickoff("2026-09-18", "19:00", before(3599_000))).toEqual({
      started: false,
      totalSeconds: 3599,
      days: 0,
      hours: 0,
      minutes: 59,
      seconds: 59,
    });
  });

  it("rounds a partial second up so the chip never shows all zeroes before kickoff", () => {
    expect(timeToKickoff("2026-09-18", "19:00", before(400))).toEqual({
      started: false,
      totalSeconds: 1,
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 1,
    });
  });

  it("marks the kickoff and everything after it as started", () => {
    const started = {
      started: true,
      totalSeconds: 0,
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0,
    };
    expect(timeToKickoff("2026-09-18", "19:00", KICKOFF)).toEqual(started);
    expect(timeToKickoff("2026-09-18", "19:00", KICKOFF + 5 * 60_000)).toEqual(started);
  });

  it("uses kickoffInstant parsing, including un-padded clocks and Date inputs", () => {
    expect(
      timeToKickoff("2026-09-18", "7:05", new Date("2026-09-18T06:05:00Z")),
    ).toMatchObject({ hours: 1, minutes: 0, started: false });
  });

  it("is null for an unreadable kickoff or clock", () => {
    expect(timeToKickoff("yesterday", "19:00", before(60_000))).toBeNull();
    expect(timeToKickoff("2026-09-18", "noon", before(60_000))).toBeNull();
    expect(timeToKickoff("2026-09-18", undefined, before(60_000))).toBeNull();
    expect(timeToKickoff("2026-09-18", "19:00", Number.NaN)).toBeNull();
  });
});
