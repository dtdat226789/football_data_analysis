import { LANGUAGES, useI18n } from "./I18nProvider.jsx";
import { TIME_ZONES } from "../lib/datetime.js";

/**
 * Language and time zone pickers for the topbar.
 *
 * Two `<select>`s rather than a menu of toggles: the zone list is a fixed set
 * of IANA names and the language list is two entries, so both are options in a
 * native select — keyboard and mobile behaviour come free, and the chosen
 * values stay inspectable instead of hiding behind a popover.
 */
export default function SettingsControls() {
  const { t, language, setLanguage, timeZone, setTimeZone } = useI18n();

  return (
    <div className="settings-controls">
      <label className="settings-control">
        <span className="muted">{t("settings.language")}</span>
        <select
          aria-label={t("settings.language")}
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
        >
          {LANGUAGES.map((l) => (
            <option key={l.id} value={l.id}>
              {l.label}
            </option>
          ))}
        </select>
      </label>

      <label className="settings-control">
        <span className="muted">{t("settings.timezone")}</span>
        <select
          aria-label={t("settings.timezone")}
          value={timeZone}
          onChange={(e) => setTimeZone(e.target.value)}
        >
          {TIME_ZONES.map((z) => (
            <option key={z.id} value={z.id}>
              {z.label}
            </option>
          ))}
        </select>
      </label>
    </div>
  );
}