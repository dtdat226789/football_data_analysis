import { describe, expect, it } from "vitest";

import {
  dayKey,
  dayOffset,
  formatDayHeading,
  formatDecimal,
  formatInstantDay,
  formatInstantHeading,
  formatInstantTime,
  formatKickoffDay,
  formatKickoffTime,
  formatLine,
  formatNumber,
  formatPercent,
  formatPlainDay,
  isIsoDay,
  kickoffInstant,
} from "./datetime.js";

// Locales the app actually passes: en maps to en-GB and vi to vi-VN.
const EN = "en-GB";
const VI = "vi-VN";

// The fixture the datetime helpers were written around: Brentford–Chelsea
// kicking off at 19:00 UTC on Friday 18 September 2026.
const UTC = "UTC";
const HANOI = "Asia/Ho_Chi_Minh";
const SINGAPORE = "Asia/Singapore";
const LONDON = "Europe/London";
const BRENTFORD = "2026-09-18T19:00:00Z";
const BRENTFORD_DATE = "2026-09-18";

describe("isIsoDay", () => {
  it("accepts the plain YYYY-MM-DD the API uses", () => {
    expect(isIsoDay("2026-09-18")).toBe(true);
  });

  it("rejects datetimes, partial dates and non-strings", () => {
    expect(isIsoDay("2026-09-18T19:00:00Z")).toBe(false);
    expect(isIsoDay("2026-09")).toBe(false);
    expect(isIsoDay("not a date")).toBe(false);
    expect(isIsoDay(20260918)).toBe(false);
    expect(isIsoDay(null)).toBe(false);
  });
});

describe("kickoffInstant", () => {
  it("locks the split (date, time) to UTC, not the browser's zone", () => {
    const d = kickoffInstant("2026-09-18", "19:00");
    expect(d.getTime()).toBe(new Date(BRENTFORD).getTime());
  });

  it("tolerates a leading hour and a seconds component", () => {
    expect(kickoffInstant("2026-09-18", "7:30:45").getTime()).toBe(
      new Date("2026-09-18T07:30:45Z").getTime(),
    );
  });

  it("returns null when either half is not a usable clock", () => {
    expect(kickoffInstant("2026-09-18", "seven")).toBeNull();
    expect(kickoffInstant("2026-09-18", null)).toBeNull();
    expect(kickoffInstant("yesterday", "19:00")).toBeNull();
  });
});

describe("dayKey", () => {
  it("gives the calendar day the kickoff falls on in the reader's zone", () => {
    expect(dayKey(new Date(BRENTFORD), HANOI)).toBe("2026-09-19");
    expect(dayKey(new Date(BRENTFORD), SINGAPORE)).toBe("2026-09-19");
    expect(dayKey(new Date(BRENTFORD), UTC)).toBe("2026-09-18");
  });

  it("respects DST: 19:00 UTC stays the same day in a UTC+1 London", () => {
    expect(dayKey(new Date(BRENTFORD), LONDON)).toBe("2026-09-18");
  });

  it("counts a near-midnight kickoff on the following day", () => {
    const late = "2026-09-18T21:00:00Z";
    expect(dayKey(new Date(late), HANOI)).toBe("2026-09-19");
    expect(dayKey(new Date(late), UTC)).toBe("2026-09-18");
  });

  it("returns null for an unreadable instant", () => {
    expect(dayKey(new Date("nope"))).toBeNull();
    expect(dayKey(null)).toBeNull();
  });
});

describe("kickoff time formatting", () => {
  it("reads the clock in the reader's zone", () => {
    expect(formatKickoffTime(BRENTFORD_DATE, "19:00", { locale: EN, timeZone: HANOI })).toBe("02:00");
    expect(formatKickoffTime(BRENTFORD_DATE, "19:00", { locale: EN, timeZone: LONDON })).toBe("20:00");
    expect(formatKickoffTime(BRENTFORD_DATE, "19:00", { locale: EN, timeZone: UTC })).toBe("19:00");
  });

  it("keeps the stored clock when the split cannot be parsed", () => {
    expect(formatKickoffTime(BRENTFORD_DATE, "seven", { locale: EN, timeZone: HANOI })).toBe("seven");
    expect(formatKickoffTime(BRENTFORD_DATE, null)).toBe("");
  });

  it("formatInstantTime mirrors it from a full ISO datetime", () => {
    expect(formatInstantTime(BRENTFORD, { locale: EN, timeZone: HANOI })).toBe("02:00");
    expect(formatInstantTime(BRENTFORD, { locale: EN, timeZone: UTC })).toBe("19:00");
    expect(formatInstantTime("not an instant")).toBe("—");
  });
});

describe("kickoff day formatting", () => {
  it("shifts the date along with the clock", () => {
    expect(formatKickoffDay(BRENTFORD_DATE, "19:00", { locale: EN, timeZone: HANOI })).toBe("19/09/2026");
    expect(formatKickoffDay(BRENTFORD_DATE, "19:00", { locale: EN, timeZone: UTC })).toBe("18/09/2026");
  });

  it("formatInstantDay reports the same rollover", () => {
    expect(formatInstantDay(BRENTFORD, { timeZone: HANOI })).toBe("2026-09-19");
    expect(formatInstantDay(BRENTFORD, { timeZone: SINGAPORE })).toBe("2026-09-19");
    expect(formatInstantDay(BRENTFORD, { timeZone: UTC })).toBe("2026-09-18");
  });

  it("formatInstantHeading names the local day of the kickoff", () => {
    expect(formatInstantHeading(BRENTFORD, { locale: EN, timeZone: HANOI })).toBe("Sat 19 Sept");
    expect(formatInstantHeading(BRENTFORD, { locale: EN, timeZone: UTC })).toBe("Fri 18 Sept");
    expect(formatInstantHeading("nope")).toBe("—");
  });

  it("keeps a date with no clock on that date in every zone", () => {
    // Without a kickoff time the midnight anchor cannot roll over, so the same
    // day is returned whether the reader is east or west of the dateline.
    expect(formatKickoffDay("2026-01-15", null, { locale: EN, timeZone: HANOI })).toBe("15/01/2026");
    expect(formatKickoffDay("2026-01-15", null, { locale: EN, timeZone: UTC })).toBe("15/01/2026");
  });
});

describe("plain calendar formatting", () => {
  it("formatPlainDay never shifts with the zone", () => {
    // A played match is a calendar date, not an instant, so a negative-offset
    // zone must not move it onto the previous day.
    expect(formatPlainDay("2026-01-15", { locale: EN })).toBe("15/01/2026");
    expect(formatPlainDay("2026-01-15", { locale: VI })).toBe("15/01/2026");
    expect(formatPlainDay("not a date")).toBe("not a date");
  });

  it("formatDayHeading renders a day bucket in the reader's language", () => {
    expect(formatDayHeading("2026-02-02", { locale: EN })).toBe("Mon 2 Feb");
    expect(formatDayHeading("2026-02-02", { locale: VI })).toBe("Thứ 2, 2 thg 2");
    expect(formatDayHeading("2026-09-19", { locale: EN })).toBe("Sat 19 Sept");
  });
});

describe("dayOffset", () => {
  it("counts whole calendar days from today in the reader's zone", () => {
    const now = new Date("2026-09-18T12:00:00Z").getTime();
    expect(dayOffset("2026-09-18", HANOI, now)).toBe(0);
    expect(dayOffset("2026-09-19", HANOI, now)).toBe(1);
    expect(dayOffset("2026-09-17", HANOI, now)).toBe(-1);
  });

  it("is null for an unreadable day", () => {
    expect(dayOffset("yesterday")).toBeNull();
  });
});

describe("locale-aware number formatting", () => {
  it("uses the language's grouping and decimal separators", () => {
    expect(formatNumber(1234.5, "en-GB")).toBe("1,234.5");
    expect(formatNumber(1234.5, "vi-VN")).toBe("1.234,5");
    expect(formatDecimal(0.94, 2, "en-GB")).toBe("0.94");
    expect(formatDecimal(66.7, 1, "vi-VN")).toBe("66,7");
    expect(formatNumber("nope", "en-GB")).toBe("nope");
  });

  it("formatPercent keeps the locale's decimal mark", () => {
    expect(formatPercent(0.667, 1, "en-GB")).toBe("66.7%");
    expect(formatPercent(0.667, 1, "vi-VN")).toBe("66,7%");
    expect(formatPercent(0.27, 0, "en-GB")).toBe("27%");
  });

  it("formatLine trims trailing zeros and keeps the decimal mark", () => {
    expect(formatLine(1.5, "en-GB")).toBe("1.5");
    expect(formatLine(1.5, "vi-VN")).toBe("1,5");
    expect(formatLine(2, "en-GB")).toBe("2");
    expect(formatLine(0.25, "en-GB")).toBe("0.25");
    expect(formatLine(-0.5, "vi-VN")).toBe("-0,5");
    expect(formatLine("nope", "en-GB")).toBe("nope");
  });
});