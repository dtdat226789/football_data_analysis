import { createContext, useCallback, useContext, useEffect, useMemo, useState } from "react";

import { DEFAULT_TIME_ZONE, TIME_ZONES } from "../lib/datetime.js";
import { en } from "./en.js";
import { vi } from "./vi.js";

/**
 * Language and time zone.
 *
 * Two things the whole app has to agree on, kept in one place because they are
 * the same kind of setting: a reader's language and a reader's wall clock.
 *
 * Both are persisted to `localStorage` so a reload does not throw the choice
 * away, and both fall back to something sensible on a first visit — the
 * language from the browser, the zone from Vietnam, which is the audience this
 * was asked for rather than whatever machine happens to open the page.
 */

const CATALOGUES = { en, vi };

export const LANGUAGES = [
  { id: "en", label: "English" },
  { id: "vi", label: "Tiếng Việt" },
];

export const DEFAULT_LANGUAGE = "en";

const LOCALE_TAG = { en: "en-GB", vi: "vi-VN" };

const LANGUAGE_KEY = "fd.language";
const ZONE_KEY = "fd.timezone";

const I18nContext = createContext(null);

/** Wraps `s`, so a `key` can name its own placeholders without a separate list. */
function interpolate(template, params) {
  if (!params) return template;
  return template.replace(/\{(\w+)\}/g, (match, name) =>
    Object.prototype.hasOwnProperty.call(params, name) ? String(params[name]) : match,
  );
}

function readStored(key) {
  try {
    return window.localStorage.getItem(key);
  } catch {
    // Private browsing and a blocked origin both throw here. A setting that
    // cannot be read is not worth failing the render over.
    return null;
  }
}

function writeStored(key, value) {
  try {
    window.localStorage.setItem(key, value);
  } catch {
    // Same as above: persistence is a nicety, not a requirement.
  }
}

/** The browser's own language, if we ship a catalogue for it. */
function browserLanguage() {
  const tag = typeof navigator === "undefined" ? "" : navigator.language || "";
  const base = String(tag).slice(0, 2).toLowerCase();
  return base in CATALOGUES ? base : DEFAULT_LANGUAGE;
}

function isKnownZone(zone) {
  return TIME_ZONES.some((z) => z.id === zone);
}

/**
 * @param {object} props
 * @param {import("react").ReactNode} [props.children] The app tree that reads
 *   the shared language and zone.
 * @param {string} [props.language] Forces a language, for tests and screenshots.
 *   Left out, the provider owns it and persists the reader's choice.
 * @param {string} [props.timeZone] Same, for the zone.
 */
export function I18nProvider({ children, language: forcedLanguage, timeZone: forcedZone }) {
  const [language, setLanguageState] = useState(
    () => forcedLanguage || readStored(LANGUAGE_KEY) || browserLanguage(),
  );
  const [timeZone, setZoneState] = useState(
    () => forcedZone || readStored(ZONE_KEY) || DEFAULT_TIME_ZONE,
  );

  useEffect(() => {
    if (!forcedLanguage) writeStored(LANGUAGE_KEY, language);
  }, [language, forcedLanguage]);

  useEffect(() => {
    if (!forcedZone) writeStored(ZONE_KEY, timeZone);
  }, [timeZone, forcedZone]);

  const setLanguage = useCallback((next) => {
    if (next in CATALOGUES) setLanguageState(next);
  }, []);

  const setTimeZone = useCallback((next) => {
    // A stale or hand-edited value would make every date on the page say
    // "Invalid Date", so an unrecognised zone is dropped rather than applied.
    if (isKnownZone(next)) setZoneState(next);
  }, []);

  const value = useMemo(() => {
    const catalogue = CATALOGUES[language] || CATALOGUES[DEFAULT_LANGUAGE];
    const locale = LOCALE_TAG[language] || LOCALE_TAG[DEFAULT_LANGUAGE];

    /**
     * Look a string up, falling back to English and then to the key itself, so
     * a missing translation shows the English sentence rather than a blank or a
     * raw key.
     */
    const t = (key, params) =>
      interpolate(catalogue[key] ?? CATALOGUES[DEFAULT_LANGUAGE][key] ?? key, params);

    return { language, setLanguage, locale, timeZone, setTimeZone, t };
  }, [language, setLanguage, timeZone, setTimeZone]);

  return <I18nContext.Provider value={value}>{children}</I18nContext.Provider>;
}

/**
 * The settings every component needs.
 *
 * Falls back to the default context when there is no provider above it, so a
 * component rendered bare in a test still reads real English strings and a
 * usable zone instead of throwing on a null destructure.
 */
export function useI18n() {
  const ctx = useContext(I18nContext);
  if (ctx) return ctx;
  return {
    language: DEFAULT_LANGUAGE,
    setLanguage: () => {},
    locale: LOCALE_TAG[DEFAULT_LANGUAGE],
    timeZone: DEFAULT_TIME_ZONE,
    setTimeZone: () => {},
    t: (key, params) => interpolate(en[key] ?? key, params),
  };
}

export { LANGUAGES as languages, CATALOGUES as catalogues };