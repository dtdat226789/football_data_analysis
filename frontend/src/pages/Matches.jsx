import { useMemo } from "react";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import MatchTable from "../components/MatchTable.jsx";
import UpcomingFixtures, { UPCOMING_OFFSET_PARAM } from "../components/UpcomingFixtures.jsx";
import { Badge, Card, CardHeader, PageHeader } from "../components/ui/index.js";
import { leagueLabel, leagueNameMap } from "../lib/leagues.js";
import { pageLabel } from "../lib/pagination.js";
import { enumParam, intParam, isIsoDay, pageOffset, useParamsPatch } from "../lib/searchParams.js";
import { asArray } from "../lib/shape.js";
import { useFormatters } from "../i18n/useFormatters.js";

const SIZES = [20, 50, 100];
const DEFAULT_SIZE = 50;
const PRESETS = [
  { label: "7d", days: 7 },
  { label: "14d", days: 14 },
  { label: "30d", days: 30 },
];

function isoDaysAgo(days, now) {
  return new Date(now - days * 86400000).toISOString().slice(0, 10);
}

export default function Matches() {
  const { t } = useFormatters();
  const [searchParams, patch] = useParamsPatch();

  const rawLeague = searchParams.get("league") ?? "";
  const leaguesApi = useApi(() => api.listLeagues(), []);
  const leagueSlugs = asArray(leaguesApi.data)
    .map((item) => item?.slug)
    .filter((value) => typeof value === "string");
  const league = leagueSlugs.length
    ? enumParam(searchParams, "league", leagueSlugs, "")
    : rawLeague;
  // A date that is not a plain ISO day would reach FastAPI as a 422, and the
  // inputs below cannot produce one — so anything else in the URL is dropped.
  const fromDate = isIsoDay(searchParams.get("from")) ? searchParams.get("from") : "";
  const toDate = isIsoDay(searchParams.get("to")) ? searchParams.get("to") : "";
  const offset = intParam(searchParams, "offset");
  const sizeParam = searchParams.get("size");
  const size = SIZES.includes(Number(sizeParam)) ? Number(sizeParam) : DEFAULT_SIZE;

  // One clock read per render, so a preset's pressed state and its tooltip
  // cannot describe different days.
  const now = Date.now();

  const leagueNames = useMemo(() => leagueNameMap(leaguesApi.data), [leaguesApi.data]);
  // The league and the date window are shared by both lists, so changing one
  // rewinds both pages. It also drops the upcoming list's day chip: the chips are
  // built from the rows the league and window left behind, so a chip chosen before
  // the change can name a day that no longer holds anything, and a one-day window
  // for it would hide the whole list.
  const rewind = (updates) =>
    patch({
      ...updates,
      offset: pageOffset(0),
      [UPCOMING_OFFSET_PARAM]: pageOffset(0),
      day: "",
    });

  const setLeague = (value) => rewind({ league: value });
  const changeDate = (field) => (e) => rewind({ [field]: e.target.value });
  const resetDates = () => rewind({ from: "", to: "" });
  const preset = (days) => rewind({ from: isoDaysAgo(days, now), to: "" });
  // The page size governs both columns, so changing it rewinds both of them:
  // an offset is counted in units of a page size, and page 3 of 50 is not page 3
  // of 100.
  const changeSize = (e) =>
    patch({
      size: e.target.value,
      offset: pageOffset(0),
      [UPCOMING_OFFSET_PARAM]: pageOffset(0),
    });
  const page = (delta) => patch({ offset: pageOffset(offset + delta * size) });

  // A window whose end is before its start is not a narrower window, it is a
  // wrong request: the API answers 422 and both cards turn into an error box
  // quoting the backend. The inputs below bound each other so this cannot be
  // picked, but a hand-edited URL can still arrive inverted. Handled like every
  // other unreadable param in this file — `?offset=abc` and a non-ISO `?from` are
  // both dropped rather than sent — so an impossible window is ignored instead of
  // asked for, and the filter bar says that it was ignored.
  const invertedWindow = Boolean(fromDate && toDate && fromDate > toDate);
  const windowFrom = invertedWindow ? "" : fromDate;
  const windowTo = invertedWindow ? "" : toDate;

  const recent = useApi(
    () =>
      api.matchesRecent({
        league: league || undefined,
        limit: size,
        offset,
        from_date: windowFrom || undefined,
        to_date: windowTo || undefined,
      }),
    [league, windowFrom, windowTo, offset, size],
  );

  const recentData = recent.data;
  const dateWindow = Boolean(fromDate || toDate);

  return (
    <div>
      <PageHeader
        title={t("page.matches.title")}
        subtitle={t("page.matches.summary", {
          league: leagueLabel(league, leagueNames) || t("page.matches.allLeagues"),
        })}
      />

      <Card className="match-filters">
        <CardHeader title={t("page.matches.filtersTitle")} />

        {/* Everything in this group changes both lists, which is why changing
            one of it also rewinds both offsets and clears the day chip. */}
        <div className="filter-group" role="group" aria-label={t("page.matches.sharedFilters")}>
          <span className="filter-group-label">{t("page.matches.sharedFilters")}</span>
          <div className="filter-row">
            <label className="filter-field">
              {t("page.matches.league")}
              <select aria-label={t("page.matches.league")} value={league} onChange={(e) => setLeague(e.target.value)}>
                <option value="">{t("page.matches.allLeagues")}</option>
                {(leaguesApi.data || []).map((l) => (
                  <option key={l.slug} value={l.slug}>
                    {l.name}
                  </option>
                ))}
              </select>
            </label>
            {/* The league list is the one filter that can fail silently: without it
                the select collapses to "All leagues" and the heading above falls back
                to the raw slug. Both states are said out loud instead. */}
            {leaguesApi.loading && <span className="card-meta">{t("page.matches.loadingLeagues")}</span>}
            {leaguesApi.error && (
              <span className="card-meta">
                {t("page.matches.leaguesUnavailable")} —{" "}
                <button className="preset" onClick={leaguesApi.reload} title={leaguesApi.error}>
                  {t("common.retry")}
                </button>
              </span>
            )}
            <div className="date-range">
              <span className="filter-group-label">{t("page.matches.dateWindow")}</span>
              <div className="date-range-inputs">
                {/* The two inputs bound each other, so the picker cannot produce a
                    window the API would reject. */}
                <input
                  type="date"
                  aria-label={t("page.matches.fromDate")}
                  value={fromDate}
                  max={toDate || undefined}
                  onChange={changeDate("from")}
                />
                <input
                  type="date"
                  aria-label={t("page.matches.toDate")}
                  value={toDate}
                  min={fromDate || undefined}
                  onChange={changeDate("to")}
                />
                {(fromDate || toDate) && (
                  <button className="preset" onClick={resetDates}>
                    {t("page.matches.resetDates")}
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>

        {/* These controls frame the shared window, but only alter how the lists
            are presented — the confidence/day filters live inside the upcoming
            card, where they belong to that list alone. */}
        <div className="filter-group" role="group" aria-label={t("page.matches.listOptions")}>
          <span className="filter-group-label">{t("page.matches.listOptions")}</span>
          <div className="filter-row">
            <div className="date-presets" role="group" aria-label={t("page.matches.presets")}>
              {PRESETS.map((p) => {
                const presetFrom = isoDaysAgo(p.days, now);
                return (
                  <button
                    key={p.days}
                    className={"preset" + (fromDate === presetFrom ? " on" : "")}
                    onClick={() => preset(p.days)}
                    aria-pressed={fromDate === presetFrom}
                    title={t("page.matches.presetTitle", { date: presetFrom })}
                  >
                    {p.label}
                  </button>
                );
              })}
              <button
                className="preset"
                onClick={resetDates}
                aria-pressed={!dateWindow}
                title={t("page.matches.clearDates")}
              >
                {t("page.matches.allDates")}
              </button>
            </div>
            <label className="filter-inline">
              {t("page.matches.show")}{" "}
              <select aria-label={t("page.matches.pageSize")} value={size} onChange={changeSize}>
                {SIZES.map((s) => (
                  <option key={s} value={s}>
                    {s}
                  </option>
                ))}
              </select>
            </label>
            {dateWindow && <span className="card-meta">{t("page.matches.windowApplies")}</span>}
          </div>
        </div>

        {invertedWindow && (
          <span className="error-box filter-alert" role="alert">
            {t("page.matches.inverted")}
          </span>
        )}
      </Card>

      <div className="two-col">
        {/* One "Show" control governs both columns, so the size reaches the
            upcoming list too — it used to page at a hardcoded 50 regardless. */}
        <UpcomingFixtures league={league} fromDate={windowFrom} toDate={windowTo} pageSize={size} />

        <Card>
          <CardHeader
            title={t("page.matches.recent")}
            actions={<Badge>{recentData?.total ?? 0}</Badge>}
          />
          <MatchTable
            state={recent}
            showLeague
            emptyMessage={
              recentData?.total > 0 && offset > 0
                ? t("page.matches.pastEnd")
                : t("page.matches.noFinished")
            }
          />
          {recentData && recentData.total > 0 && (
            <div className="pagination">
              <button disabled={offset === 0} onClick={() => page(-1)}>
                {t("common.prev")}
              </button>
              <span className="muted">
                {pageLabel(size, offset, recentData.total, {
                  empty: t("pagination.zero"),
                  past: t("pagination.past"),
                })}
              </span>
              <button disabled={offset + size >= recentData.total} onClick={() => page(1)}>
                {t("common.next")}
              </button>
            </div>
          )}
        </Card>
      </div>
    </div>
  );
}
