import { useCallback, useMemo } from "react";

import {
  formatDayHeading,
  formatDecimal,
  formatInstantTime,
  formatInstantDay,
  formatInstantHeading,
  formatKickoffDay,
  formatKickoffTime,
  formatLine,
  formatNumber,
  formatPercent,
  formatPlainDay,
  isIsoDay,
  kickoffInstant,
  dayOffset,
  dayKey,
} from "../lib/datetime.js";
import { useI18n } from "./I18nProvider.jsx";

/**
 * Translation and formatting in one hook.
 *
 * Every display concern in the app is one of two things — a sentence, or a
 * number/date that has to follow the reader's language and clock — so a
 * component takes this once instead of assembling `useI18n` plus six datetime
 * imports and passing `locale` and `timeZone` into each by hand. That hand-passing
 * is where the zone would get dropped, and a date formatted in UTC next to one
 * formatted in ICT is exactly the bug this feature exists to remove.
 */
export function useFormatters() {
  const { t, locale, timeZone, language, setLanguage, setTimeZone } = useI18n();

  const kickoffTime = useCallback(
    (date, time) => formatKickoffTime(date, time, { locale, timeZone }),
    [locale, timeZone],
  );

  const kickoffDay = useCallback(
    (date, time) => formatKickoffDay(date, time, { locale, timeZone }),
    [locale, timeZone],
  );

  /** For instants the split `(date, time)` does not fit, e.g. `match_datetime`. */
  const instantTime = useCallback(
    (instant) => formatInstantTime(instant, { locale, timeZone }),
    [locale, timeZone],
  );
  const instantDay = useCallback((instant) => formatInstantDay(instant, { timeZone }), [timeZone]);
  const instantHeading = useCallback(
    (instant) => formatInstantHeading(instant, { locale, timeZone }),
    [locale, timeZone],
  );

  const num = useCallback((value) => formatNumber(value, locale), [locale]);
  const dec = useCallback((value, digits) => formatDecimal(value, digits, locale), [locale]);
  const line = useCallback((value) => formatLine(value, locale), [locale]);
  const pct = useCallback((value, digits = 1) => formatPercent(value, digits, locale), [locale]);
  const pct0 = useCallback((value) => formatPercent(value, 0, locale), [locale]);

  // A calendar day with no clock attached: a played match, a season boundary.
  // Not zone-converted — see `formatPlainDay` for why.
  const plainDay = useCallback((date) => formatPlainDay(date, { locale }), [locale]);
  const dayHeading = useCallback((day) => formatDayHeading(day, { locale }), [locale]);

  /** Days from today in the reader's own zone, or null when the day is unreadable. */
  const offsetFromToday = useCallback((day) => dayOffset(day, timeZone), [timeZone]);

  return useMemo(
    () => ({
      t,
      language,
      setLanguage,
      timeZone,
      setTimeZone,
      locale,
      num,
      dec,
      pct,
      pct0,
      line,
      kickoffTime,
      kickoffDay,
      instantTime,
      instantDay,
      instantHeading,
      plainDay,
      dayHeading,
      offsetFromToday,
      isIsoDay,
      kickoffInstant,
      dayKey,
    }),
    [
      t,
      language,
      setLanguage,
      timeZone,
      setTimeZone,
      locale,
      num,
      dec,
      pct,
      pct0,
      line,
      kickoffTime,
      kickoffDay,
      instantTime,
      instantDay,
      instantHeading,
      plainDay,
      dayHeading,
      offsetFromToday,
    ],
  );
}