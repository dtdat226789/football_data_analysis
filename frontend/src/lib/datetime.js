/**
 * Match times are stored in UTC and read as such.
 *
 * The upstream feed's `match_datetime` carries an explicit `Z`
 * (`2026-09-18T19:00:00Z` is Brentford–Chelsea at 20:00 BST on a Friday), and
 * `matches.kickoff_time` is a Postgres `TIME` holding that same UTC wall clock.
 * Nothing in the pipeline ever converts it, so every rendering site used to
 * print UTC and label it as if it were local.
 *
 * Everything here is a pure function of (date, time, zone) so the conversion
 * can be tested without a provider or a browser clock.
 */

/** Vietnam. UTC+7 all year, so there is no DST edge to get wrong. */
export const DEFAULT_TIME_ZONE = "Asia/Ho_Chi_Minh";

/**
 * The zones offered in the picker. Kept short on purpose: this is a
 * "show me my local kickoff" control, not a timezone database.
 */
export const TIME_ZONES = [
  { id: "Asia/Ho_Chi_Minh", label: "Hanoi (ICT, UTC+7)" },
  { id: "Asia/Singapore", label: "Singapore (UTC+8)" },
  { id: "Asia/Tokyo", label: "Tokyo (UTC+9)" },
  { id: "Europe/London", label: "London (UTC+0/+1)" },
  { id: "UTC", label: "UTC" },
];

const ISO_DAY = /^\d{4}-\d{2}-\d{2}$/;
const CLOCK = /^(\d{1,2}):(\d{2})(?::(\d{2}))?/;

/** @returns {boolean} True for a plain `YYYY-MM-DD`, the shape every API date has. */
export function isIsoDay(value) {
  return typeof value === "string" && ISO_DAY.test(value);
}

/**
 * The instant a fixture kicks off, or null when the inputs are not one.
 *
 * `new Date("2026-09-18T19:00:00Z")` rather than a local-midnight parse: the
 * stored clock is UTC, so it has to be pinned to UTC or the browser's own
 * offset would be applied twice — once here and once by `timeZone`.
 */
export function kickoffInstant(date, time) {
  if (!isIsoDay(date) || typeof time !== "string") return null;
  const m = CLOCK.exec(time.trim());
  if (!m) return null;
  const [, hh, mm, ss] = m;
  const iso = `${date}T${hh.padStart(2, "0")}:${mm}:${ss || "00"}Z`;
  const d = new Date(iso);
  return Number.isNaN(d.getTime()) ? null : d;
}

/**
 * The calendar day an instant falls on in `timeZone`, as `YYYY-MM-DD`.
 *
 * `en-CA` is the locale whose short format is ISO-ordered, which is what makes
 * this usable as a grouping key: a 23:00 UTC kickoff is `2026-09-19` in Hanoi
 * and stays `2026-09-18` in London, so the same fixture lands under a different
 * day heading depending on the reader's zone.
 */
export function dayKey(instant, timeZone = DEFAULT_TIME_ZONE) {
  if (!(instant instanceof Date) || Number.isNaN(instant.getTime())) return null;
  try {
    return new Intl.DateTimeFormat("en-CA", {
      timeZone,
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }).format(instant);
  } catch {
    return null;
  }
}

/** `2026-09-18T19:00:00Z` → `2026-09-18 19:00` in `timeZone`. Null-safe. */
export function formatKickoffTime(date, time, { locale = "en", timeZone = DEFAULT_TIME_ZONE } = {}) {
  const instant = kickoffInstant(date, time);
  if (!instant) return typeof time === "string" ? time : "";
  try {
    return new Intl.DateTimeFormat(locale, {
      timeZone,
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    }).format(instant);
  } catch {
    return time;
  }
}

/**
 * The clock half of an instant in `timeZone`, mirroring `formatKickoffTime` but
 * taking an instant (a `Date` or an ISO datetime with a zone suffix) instead of
 * the split `(date, time)` the fixtures API returns.
 */
export function formatInstantTime(instant, { locale = "en", timeZone = DEFAULT_TIME_ZONE } = {}) {
  const d = instant instanceof Date ? instant : new Date(instant);
  if (!instant || Number.isNaN(d.getTime())) return "—";
  try {
    return new Intl.DateTimeFormat(locale, {
      timeZone,
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    }).format(d);
  } catch {
    return "—";
  }
}

/** The calendar day an instant falls on in `timeZone`, as `YYYY-MM-DD`. */
export function formatInstantDay(instant, { timeZone = DEFAULT_TIME_ZONE } = {}) {
  return dayKey(instant instanceof Date ? instant : new Date(instant), timeZone);
}

/** "Sat 19 Sep" for an instant, in the reader's zone. */
export function formatInstantHeading(instant, { locale = "en", timeZone = DEFAULT_TIME_ZONE } = {}) {
  const d = instant instanceof Date ? instant : new Date(instant);
  const key = dayKey(d, timeZone);
  if (!key) return "—";
  const [y, m, day] = key.split("-").map(Number);
  try {
    return new Intl.DateTimeFormat(locale, {
      weekday: "short",
      day: "numeric",
      month: "short",
      timeZone: "UTC",
    }).format(new Date(Date.UTC(y, m - 1, day)));
  } catch {
    return key;
  }
}

/** The date half only, in `timeZone`. Used where a row shows a date and no clock. */
export function formatKickoffDay(date, time, { locale = "en", timeZone = DEFAULT_TIME_ZONE } = {}) {
  const instant = kickoffInstant(date, time);
  const anchor = instant ?? (isIsoDay(date) ? new Date(`${date}T00:00:00Z`) : null);
  if (!anchor) return isIsoDay(date) ? date : "";
  try {
    return new Intl.DateTimeFormat(locale, {
      timeZone,
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }).format(anchor);
  } catch {
    return date;
  }
}

/**
 * A finished match, or a day bucket with no kickoff attached.
 *
 * Deliberately does *not* convert. These are calendar days with no time
 * component — the row says "18 Sep 2026" and nothing on screen claims a
 * kickoff hour — so pinning them to midnight UTC and shifting them into a
 * negative-offset zone would move a played match onto the previous day for a
 * reason no reader could reconstruct.
 */
export function formatPlainDay(date, { locale = "en" } = {}) {
  if (!isIsoDay(date)) return typeof date === "string" ? date : "";
  const [y, m, d] = date.split("-").map(Number);
  try {
    return new Intl.DateTimeFormat(locale, {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      timeZone: "UTC",
    }).format(new Date(Date.UTC(y, m - 1, d)));
  } catch {
    return date;
  }
}

/** "Sat 19 Sep" / "Th 9, 19 thg 9" for a day bucket heading. */
export function formatDayHeading(isoDay, { locale = "en" } = {}) {
  if (!isIsoDay(isoDay)) return typeof isoDay === "string" ? isoDay : "";
  const [y, m, d] = isoDay.split("-").map(Number);
  try {
    return new Intl.DateTimeFormat(locale, {
      weekday: "short",
      day: "numeric",
      month: "short",
      timeZone: "UTC",
    }).format(new Date(Date.UTC(y, m - 1, d)));
  } catch {
    return isoDay;
  }
}

/**
 * How far `isoDay` sits from today in the reader's own zone.
 *
 * Read at noon on the target day rather than midnight so a reader east of
 * Greenwich and one west of it both get the same answer, and returned as an
 * offset in days so the caller can pick its own wording and language.
 *
 * @returns {number | null} 0 for today, 1 for tomorrow, negative for past.
 */
export function dayOffset(isoDay, timeZone = DEFAULT_TIME_ZONE, now = Date.now()) {
  if (!isIsoDay(isoDay)) return null;
  const todayKey = dayKey(new Date(now), timeZone);
  if (!todayKey) return null;
  const [y1, m1, d1] = isoDay.split("-").map(Number);
  const [y2, m2, d2] = todayKey.split("-").map(Number);
  const a = Date.UTC(y1, m1 - 1, d1);
  const b = Date.UTC(y2, m2 - 1, d2);
  if (Number.isNaN(a) || Number.isNaN(b)) return null;
  return Math.round((a - b) / 86400000);
}

/** Locale-aware grouping separator: `1,234` in English, `1.234` in Vietnamese. */
export function formatNumber(value, locale = "en") {
  if (typeof value !== "number" || !Number.isFinite(value)) return value == null ? "—" : String(value);
  try {
    return new Intl.NumberFormat(locale).format(value);
  } catch {
    return String(value);
  }
}

/** Fixed-decimal formatting that also follows the locale's separator. */
export function formatDecimal(value, digits, locale = "en") {
  if (typeof value !== "number" || !Number.isFinite(value)) return value == null ? "—" : String(value);
  try {
    return new Intl.NumberFormat(locale, {
      minimumFractionDigits: digits,
      maximumFractionDigits: digits,
    }).format(value);
  } catch {
    return value.toFixed(digits);
  }
}

/**
 * A betting line, e.g. `1.5`, `0.25`: locale decimal mark, trailing zeros
 * trimmed so `1` does not render as `1.00`.
 */
export function formatLine(value, locale = "en") {
  if (typeof value !== "number" || !Number.isFinite(value)) return value == null ? "—" : String(value);
  try {
    return new Intl.NumberFormat(locale, {
      minimumFractionDigits: 0,
      maximumFractionDigits: 2,
    }).format(value);
  } catch {
    return String(value);
  }
}

/** Percentage from a 0..1 ratio. Vietnamese uses `,` as the decimal mark. */
export function formatPercent(value, digits = 1, locale = "en") {
  if (typeof value !== "number" || !Number.isFinite(value)) return "—";
  return `${formatDecimal(value * 100, digits, locale)}%`;
}