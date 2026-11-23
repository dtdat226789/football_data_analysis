import { kickoffInstant } from "./datetime.js";

const SECONDS_PER_MINUTE = 60;
const SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE;
const SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR;

/** @param {number | Date} [now] */
export function timeToKickoff(date, time, now = Date.now()) {
  const kickoff = kickoffInstant(date, time);
  const current = now instanceof Date ? now.getTime() : now;
  if (!kickoff || typeof current !== "number" || !Number.isFinite(current)) return null;

  const totalSeconds = Math.max(0, Math.ceil((kickoff.getTime() - current) / 1000));
  return {
    started: totalSeconds === 0,
    totalSeconds,
    days: Math.floor(totalSeconds / SECONDS_PER_DAY),
    hours: Math.floor((totalSeconds % SECONDS_PER_DAY) / SECONDS_PER_HOUR),
    minutes: Math.floor((totalSeconds % SECONDS_PER_HOUR) / SECONDS_PER_MINUTE),
    seconds: totalSeconds % SECONDS_PER_MINUTE,
  };
}
