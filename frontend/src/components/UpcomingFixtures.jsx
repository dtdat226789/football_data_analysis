import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { intParam, isIsoDay, pageOffset, useParamsPatch } from "../lib/searchParams.js";
import { pageLabel } from "../lib/pagination.js";
import { ErrorBox, ListSkeleton } from "./State.jsx";
import { TeamLink } from "./TeamLink.jsx";
import PredictionChips from "./PredictionChips.jsx";
import { useFormatters } from "../i18n/useFormatters.js";

/** How many fixtures a page holds when the host page does not say otherwise. */
export const DEFAULT_PAGE_SIZE = 50;

/** The query key this list pages on. Owned here, imported by the page that resets it. */
export const UPCOMING_OFFSET_PARAM = "uoffset";

/**
 * Confidence floors offered as one click each. Most fixtures sit near 0.35
 * because neither side is favoured, so the useful cuts are "model has an
 * opinion" and "model is sure" rather than a free-text number. Only the open
 * end of the range is a word; the rest are numerals.
 */
const CONFIDENCE_STEPS = [
  { value: "", key: "market.filter.all" },
  { value: "0.45", label: "45%+" },
  { value: "0.6", label: "60%+" },
  { value: "0.75", label: "75%+" },
];

/** Route id for a fixture: the trailing `date-home-vs-away` slug segment. */
export function fixturePathId(slug) {
  return String(slug || "").replace(/\/+$/, "").split("/").pop() || "";
}

/**
 * The stored calendar day a bucket holds.
 *
 * The API buckets fixtures on the UTC date it stored them under, and the day
 * headings and chips below follow that key — so paging, `day_counts` and the
 * `from_date`/`to_date` window all keep agreeing with each other. Only the clock
 * time inside a row is converted to the reader's zone. A late fixture can
 * therefore read as an early-morning kickoff under the previous day's heading;
 * `fixtureTimeLine` spells the local date out for exactly those rows rather than
 * letting the time look like it belongs to the wrong day.
 */
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
/**
 * @param {object} props
 * @param {string} [props.league] Empty means every league.
 * @param {string} [props.fromDate] Optional ISO day. Omitted, absent, or not a
 *   plain ISO day is treated as "no lower bound" — LeagueDetail passes neither.
 * @param {string} [props.toDate] Optional ISO day, same handling.
 * @param {number} [props.pageSize] Rows per page. The host page's page-size
 *   control owns this, so both of its lists page at the same size.
 * @param {string} [props.offsetParam] Query param holding this list's offset, so
 *   it does not collide with a host page that paginates something else.
 */
export default function UpcomingFixtures({
  league,
  fromDate,
  toDate,
  pageSize = DEFAULT_PAGE_SIZE,
  offsetParam = UPCOMING_OFFSET_PARAM,
}) {
  const { t, kickoffTime, kickoffDay, dayHeading, offsetFromToday } = useFormatters();
  const [searchParams, patch] = useParamsPatch();
  const day = searchParams.get("day") ?? "";
  const minConfidence = searchParams.get("conf") ?? "";
  const offset = intParam(searchParams, offsetParam);

  // The day chip is a one-day window. `/fixtures` has no day parameter, so it has
  // to travel as `from_date`/`to_date`: sending the chip on its own only flipped
  // the sort to date order, leaving the query over every day — and page one of a
  // date-ordered fixture list starts at the soonest fixture, which made every
  // picked day render as "today".
  const sharedFrom = isIsoDay(fromDate) ? fromDate : "";
  const sharedTo = isIsoDay(toDate) ? toDate : "";
  const pickedDay = isIsoDay(day) ? day : "";
  // A day outside the shared window would invert it, and an inverted window is a
  // 422 rather than an empty list. The chips are derived from the rows the window
  // already left, so this is only reachable from a stale or hand-edited URL; the
  // window wins and the day is simply not applied.
  const dayInWindow =
    pickedDay && (!sharedFrom || pickedDay >= sharedFrom) && (!sharedTo || pickedDay <= sharedTo)
      ? pickedDay
      : "";
  const windowFrom = dayInWindow || sharedFrom;
  const windowTo = dayInWindow || sharedTo;

  // Changing a filter rewinds to the first page; staying on page 4 of a
  // narrower list is the classic way to land on an empty screen.
  const setDay = (value) => patch({ day: value, [offsetParam]: pageOffset(0) });
  const setConfidence = (value) => patch({ conf: value, [offsetParam]: pageOffset(0) });

  const upcoming = useApi(
    () =>
      api.fixtures({
        league: league || undefined,
        // Date order whenever anything is filtered, so paging is stable and the
        // day grouping means something. Matches the server's own rule.
        sort: windowFrom || windowTo || minConfidence ? "date" : "confidence",
        limit: pageSize,
        offset,
        from_date: windowFrom || undefined,
        to_date: windowTo || undefined,
        min_confidence: minConfidence || undefined,
      }),
    [league, minConfidence, offset, windowFrom, windowTo, pageSize],
  );

  const data = upcoming.data;
  const rows = data?.matches || [];
  const groups = groupByDay(rows);
  const filtered = Boolean(dayInWindow || minConfidence || sharedFrom || sharedTo);

  /** "Today" / "Tomorrow" for a stored day key, where they help. */
  const relativeFor = (isoDayKey) => {
    const offsetDays = offsetFromToday(isoDayKey);
    if (offsetDays === 0) return t("fixture.today");
    if (offsetDays === 1) return t("fixture.tomorrow");
    return null;
  };

  /** Heading for a stored day key. */
  const labelFor = (isoDayKey) => (isoDayKey === "unknown" ? t("fixture.dateUnknown") : dayHeading(isoDayKey));

  /**
   * A fixture's own meta line: the kickoff clock, plus the local date when the
   * zone has pushed it onto a different calendar day than the bucket it sits in.
   */
  const fixtureTimeLine = (m) => {
    const clock = kickoffTime(m.match_date, m.time);
    if (!isIsoDay(m.match_date) || clock === "—") return clock;
    const localDay = kickoffDay(m.match_date, m.time);
    return localDay === m.match_date ? clock : `${dayHeading(localDay)} · ${clock}`;
  };

  return (
    <section className="card">
      <h3 style={{ marginTop: 0, display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
        {t("fixture.upcoming")}
        <span className="badge">{data?.total ?? 0}</span>
        {/* The badge is the filtered total, which is not what is on screen once a
            limit is in play — so say which slice this is. */}
        {data && data.total > 0 && (
          <span className="muted" style={{ fontSize: 13, fontWeight: 400 }}>
            {data.returned < data.total
              ? t("fixture.showingRange", {
                  start: data.offset + 1,
                  end: data.offset + data.returned,
                  total: data.total,
                })
              : t("fixture.allTotal", { total: data.total })}
          </span>
        )}
      </h3>

      {/* The filters stay on screen whenever a filter is active, even once it has
          narrowed the list to nothing. Hiding them at zero results is what turns a
          too-strict choice into a dead end with no way back. */}
      {data && (data.total > 0 || filtered) && (
        <>
          <div className="market-filters" role="group" aria-label={t("fixture.confidenceAria")}>
            {CONFIDENCE_STEPS.map((step) => (
              <button
                key={step.value}
                className={"preset" + (minConfidence === step.value ? " on" : "")}
                onClick={() => setConfidence(step.value)}
                aria-pressed={minConfidence === step.value}
                title={
                  step.value
                    ? t("fixture.confidenceTitle", { value: step.value })
                    : t("fixture.confidenceAllTitle")
                }
              >
                {step.key ? t(step.key) : step.label}
              </button>
            ))}
          </div>

          {/* One chip per day present, with its true count, so a 126-match
              Saturday is visible as such rather than as an endless list. A picked
              day narrows the list to exactly that day, so the surviving chip set
              is a single entry — it has to stay visible or the pick could only be
              undone by reloading. */}
          {data.dates?.length > 1 || (dayInWindow && data.total > 0) ? (
            <div className="date-presets" role="group" aria-label={t("fixture.dayAria")}>
              <button
                className={"preset" + (dayInWindow ? "" : " on")}
                onClick={() => setDay("")}
                aria-pressed={!dayInWindow}
                title={t("fixture.dayAllTitle")}
              >
                {t("fixture.allDays")}
              </button>
              {data.dates.map((d) => (
                <button
                  key={d}
                  className={"preset" + (dayInWindow === d ? " on" : "")}
                  onClick={() => setDay(dayInWindow === d ? "" : d)}
                  aria-pressed={dayInWindow === d}
                  title={t("fixture.dayTitle", {
                    day: labelFor(d),
                    n: data.day_counts?.[d] ?? 0,
                  })}
                >
                  {relativeFor(d) || labelFor(d)}
                  <span className="muted"> {data.day_counts?.[d] ?? 0}</span>
                </button>
              ))}
            </div>
          ) : null}
        </>
      )}

      {upcoming.loading && <ListSkeleton items={4} />}
      {upcoming.error && <ErrorBox error={upcoming.error} />}
      {data && rows.length === 0 && (
        <p className="muted">
          {t("fixture.none")}
          {filtered ? ` ${t("fixture.noneFilteredSuffix")}` : league ? ` ${t("fixture.noneLeagueSuffix")}` : ""}.
        </p>
      )}

      {data && rows.length > 0 && (
        <div className="event-list">
          {groups.map(([dayBucket, dayRows]) => {
            const total = data.day_counts?.[dayBucket];
            // Only a day split by the page boundary is partial; a day the filter
            // narrowed on purpose is complete and needs no caveat.
            const partial = typeof total === "number" && dayRows.length < total;
            const dayRelative = dayBucket === "unknown" ? null : relativeFor(dayBucket);
            return (
              <div key={dayBucket} className="fixture-day">
                <h4 className="fixture-day-head">
                  {labelFor(dayBucket)}
                  {dayRelative && <span className="muted"> · {dayRelative}</span>}
                  <span className="muted">
                    {" "}
                    ·{" "}
                    {partial
                      ? t("fixture.shownOf", { shown: dayRows.length, total })
                      : t("fixture.shown", { n: dayRows.length })}
                  </span>
                  {partial && (
                    <button
                      type="button"
                      className="market-open fixture-day-more"
                      onClick={() => setDay(dayBucket)}
                    >
                      {t("fixture.seeThisDay")}
                    </button>
                  )}
                </h4>
                {dayRows.map((m) => (
                  <div
                    key={m.slug || `${m.home_team}-${m.away_team}-${dayBucket}`}
                    className="event"
                  >
                    <div className="teams">
                      <span className="muted" style={{ fontSize: 12 }}>
                        {fixtureTimeLine(m)} · {m.league_name || m.league}
                      </span>
                      <span>
                        <TeamLink name={m.home_team} /> {t("common.vs")} <TeamLink name={m.away_team} />
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
                        {t("fixture.detail")}
                      </Link>
                    ) : null}
                  </div>
                ))}
              </div>
            );
          })}
        </div>
      )}

      {data && data.total > pageSize && (
        <div className="pagination">
          <button disabled={offset === 0} onClick={() => patch({ [offsetParam]: pageOffset(offset - pageSize) })}>
            {t("common.prev")}
          </button>
          <span className="muted">{pageLabel(pageSize, offset, data.total, {
            empty: t("pagination.zero"),
            past: t("pagination.past"),
          })}</span>
          <button disabled={!data.has_more} onClick={() => patch({ [offsetParam]: pageOffset(offset + pageSize) })}>
            {t("common.next")}
          </button>
        </div>
      )}
    </section>
  );
}