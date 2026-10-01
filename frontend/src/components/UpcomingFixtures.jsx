import { Link, useSearchParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, ListSkeleton } from "./State.jsx";
import { TeamLink } from "./TeamLink.jsx";
import PredictionChips from "./PredictionChips.jsx";

/** How many fixtures a page holds. A weekend is ~200 rows, so this pages. */
const PAGE_SIZE = 50;

/**
 * Confidence floors offered as one click each. Most fixtures sit near 0.35
 * because neither side is favoured, so the useful cuts are "model has an
 * opinion" and "model is sure" rather than a free-text number.
 */
const CONFIDENCE_STEPS = [
  { value: "", label: "All" },
  { value: "0.45", label: "45%+" },
  { value: "0.6", label: "60%+" },
  { value: "0.75", label: "75%+" },
];

const DAY_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
const MONTH_NAMES = [
  "Jan", "Feb", "Mar", "Apr", "May", "Jun",
  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
];

/**
 * "Sat 3 Oct" for an ISO day.
 *
 * Parsed with an explicit local midnight rather than a trailing `Z`: the dates
 * are plain calendar days, and reading them as UTC would shift every heading a
 * day backwards for anyone west of Greenwich.
 */
export function dayLabel(iso) {
  const d = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(d.getTime())) return iso;
  return `${DAY_NAMES[d.getDay()]} ${d.getDate()} ${MONTH_NAMES[d.getMonth()]}`;
}

/** "Today" / "Tomorrow" where they help, else null. */
function relativeDay(iso) {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const target = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(target.getTime())) return null;
  const days = Math.round((target - today) / 86400000);
  if (days === 0) return "Today";
  if (days === 1) return "Tomorrow";
  return null;
}

/** Route id for a fixture: the trailing `date-home-vs-away` slug segment. */
export function fixturePathId(slug) {
  return String(slug || "").replace(/\/+$/, "").split("/").pop() || "";
}

/** Group a page of fixtures into day buckets, preserving the server's order. */
function groupByDay(matches) {
  const groups = new Map();
  for (const m of matches) {
    const key = m.match_date || "unknown";
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(m);
  }
  return [...groups.entries()];
}

/**
 * The upcoming fixture list, grouped by day and paged.
 *
 * The stored snapshot is a weekend burst — a few hundred fixtures spread over a
 * handful of days — so a flat slice sorted by confidence hides everything past
 * the first page and moves the page boundary every time a match is collected.
 * Grouping by day and paging in date order keeps a page stable and makes the
 * shape of the weekend visible; the day chips and the confidence floor are how a
 * reader narrows a 126-match Saturday down to something readable.
 */
export default function UpcomingFixtures({ league, fromDate, toDate, offsetParam = "uoffset" }) {
  const [searchParams, setSearchParams] = useSearchParams();
  const day = searchParams.get("day") ?? "";
  const minConfidence = searchParams.get("conf") ?? "";
  const offset = Number(searchParams.get(offsetParam) || 0);

  const patch = (updates) => {
    const next = new URLSearchParams(searchParams);
    for (const [key, value] of Object.entries(updates)) {
      if (value !== "" && value !== null && value !== undefined) next.set(key, value);
      else next.delete(key);
    }
    setSearchParams(next);
  };

  // Changing a filter rewinds to the first page; staying on page 4 of a
  // narrower list is the classic way to land on an empty screen.
  const setDay = (value) => patch({ day: value, [offsetParam]: 0 });
  const setConfidence = (value) => patch({ conf: value, [offsetParam]: 0 });

  const upcoming = useApi(
    () =>
      api.fixtures({
        league: league || undefined,
        // Date order whenever anything is filtered, so paging is stable and the
        // day grouping means something. Matches the server's own rule.
        sort: day || minConfidence || fromDate || toDate ? "date" : "confidence",
        limit: PAGE_SIZE,
        offset,
        from_date: fromDate || undefined,
        to_date: toDate || undefined,
        min_confidence: minConfidence || undefined,
      }),
    [league, day, minConfidence, offset, fromDate, toDate],
  );

  const data = upcoming.data;
  const rows = data?.matches || [];
  const groups = groupByDay(rows);
  const filtered = Boolean(day || minConfidence || fromDate || toDate);

  return (
    <section className="card">
      <h3 style={{ marginTop: 0, display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
        Upcoming
        <span className="badge">{data?.total ?? 0}</span>
        {/* The badge is the filtered total, which is not what is on screen once a
            limit is in play — so say which slice this is. */}
        {data && data.total > 0 && (
          <span className="muted" style={{ fontSize: 13, fontWeight: 400 }}>
            {data.returned < data.total
              ? `showing ${data.offset + 1}–${data.offset + data.returned} of ${data.total}`
              : `all ${data.total}`}
          </span>
        )}
      </h3>

      {data && data.total > 0 && (
        <>
          <div className="market-filters" role="group" aria-label="Filter by model confidence">
            {CONFIDENCE_STEPS.map((step) => (
              <button
                key={step.label}
                className={"preset" + (minConfidence === step.value ? " on" : "")}
                onClick={() => setConfidence(step.value)}
                aria-pressed={minConfidence === step.value}
                title={
                  step.value
                    ? `Only fixtures where the model's strongest side is at least ${step.value}`
                    : "Every upcoming fixture"
                }
              >
                {step.label}
              </button>
            ))}
          </div>

          {/* One chip per day present, with its true count, so a 126-match
              Saturday is visible as such rather than as an endless list. */}
          {data.dates?.length > 1 && (
            <div className="date-presets" role="group" aria-label="Filter by day">
              <button
                className={"preset" + (day ? "" : " on")}
                onClick={() => setDay("")}
                aria-pressed={!day}
                title="Every day"
              >
                All days
              </button>
              {data.dates.map((d) => (
                <button
                  key={d}
                  className={"preset" + (day === d ? " on" : "")}
                  onClick={() => setDay(day === d ? "" : d)}
                  aria-pressed={day === d}
                  title={`${dayLabel(d)} — ${data.day_counts?.[d] ?? 0} fixtures`}
                >
                  {relativeDay(d) || dayLabel(d)}
                  <span className="muted"> {data.day_counts?.[d] ?? 0}</span>
                </button>
              ))}
            </div>
          )}
        </>
      )}

      {upcoming.loading && <ListSkeleton items={4} />}
      {upcoming.error && <ErrorBox error={upcoming.error} />}
      {data && rows.length === 0 && (
        <p className="muted">
          No upcoming fixtures
          {filtered ? " match these filters" : league ? " for this league" : ""}.
        </p>
      )}

      {data && rows.length > 0 && (
        <div className="event-list">
          {groups.map(([dayKey, dayRows]) => {
            const total = data.day_counts?.[dayKey];
            // Only a day split by the page boundary is partial; a day the filter
            // narrowed on purpose is complete and needs no caveat.
            const partial = typeof total === "number" && dayRows.length < total;
            return (
              <div key={dayKey} className="fixture-day">
                <h4 className="fixture-day-head">
                  {dayKey === "unknown" ? "Date unknown" : dayLabel(dayKey)}
                  {relativeDay(dayKey) && (
                    <span className="muted"> · {relativeDay(dayKey)}</span>
                  )}
                  <span className="muted">
                    {" "}
                    · {dayRows.length} shown
                    {partial ? ` of ${total}` : ""}
                  </span>
                  {partial && (
                    <button
                      type="button"
                      className="market-open fixture-day-more"
                      onClick={() => setDay(dayKey)}
                    >
                      see this day
                    </button>
                  )}
                </h4>
                {dayRows.map((m, i) => (
                  <div key={m.slug || `${dayKey}-${i}`} className="event">
                    <div className="teams">
                      <span className="muted" style={{ fontSize: 12 }}>
                        {m.time} · {m.league_name || m.league}
                      </span>
                      <span>
                        <TeamLink name={m.home_team} /> vs <TeamLink name={m.away_team} />
                      </span>
                    </div>
                    <PredictionChips
                      predictions={m.predictions}
                      compact
                      confidence={m.predictions?.confidence}
                      dataThrough={m.predictions?.data_through}
                    />
                    {m.slug ? (
                      <Link
                        className="link"
                        style={{ fontSize: 12 }}
                        to={`/fixture/${m.league}/${fixturePathId(m.slug)}`}
                      >
                        detail
                      </Link>
                    ) : null}
                  </div>
                ))}
              </div>
            );
          })}
        </div>
      )}

      {data && data.total > PAGE_SIZE && (
        <div className="pagination">
          <button disabled={offset === 0} onClick={() => patch({ [offsetParam]: Math.max(0, offset - PAGE_SIZE) })}>
            ‹ Prev
          </button>
          <span className="muted">
            {data.offset + 1}–{data.offset + data.returned} of {data.total}
          </span>
          <button disabled={!data.has_more} onClick={() => patch({ [offsetParam]: offset + PAGE_SIZE })}>
            Next ›
          </button>
        </div>
      )}
    </section>
  );
}
