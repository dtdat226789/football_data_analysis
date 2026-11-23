import { useNow } from "../hooks/useNow.js";
import { useFormatters } from "../i18n/useFormatters.js";
import { timeToKickoff } from "../lib/countdown.js";

const SECONDS_PER_HOUR = 60 * 60;

function pad(value) {
  return String(value).padStart(2, "0");
}

function labelFor(remaining, t) {
  if (remaining.totalSeconds < SECONDS_PER_HOUR) {
    return `${pad(remaining.hours)}:${pad(remaining.minutes)}:${pad(remaining.seconds)}`;
  }
  if (remaining.days > 0) {
    return t("countdown.daysHours", { days: remaining.days, hours: remaining.hours });
  }
  return t("countdown.hoursMinutes", { hours: remaining.hours, minutes: remaining.minutes });
}

export default function Countdown({ date, time }) {
  const now = useNow();
  const { t, kickoffTime } = useFormatters();
  const remaining = timeToKickoff(date, time, now);

  if (!remaining || remaining.started) return null;

  return (
    <span
      role="timer"
      className="countdown tabular"
      aria-label={t("countdown.aria", { time: kickoffTime(date, time) })}
    >
      {labelFor(remaining, t)}
    </span>
  );
}
