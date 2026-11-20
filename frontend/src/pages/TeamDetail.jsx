import { useMemo } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Skeleton, TableSkeleton } from "../components/State.jsx";
import { FormPills } from "../components/FormPills.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import { BarList, Donut, StatCard } from "../components/Charts.jsx";
import MatchOutlook from "../components/MatchOutlook.jsx";
import { BackLink, Badge, Card, CardHeader, PageHeader, TableShell } from "../components/ui/index.js";
import { leagueLabel, leagueNameMap } from "../lib/leagues.js";
import { useParamsPatch } from "../lib/searchParams.js";
import { useFormatters } from "../i18n/useFormatters.js";

const POSITION_COLOR = "var(--green)";
const POINTS_COLOR = "var(--accent)";
const WIN_COLOR = "var(--green)";
/** Shared empty list, so `detail.data?.memberships || …` keeps one identity. */
const NO_MEMBERSHIPS = [];
const DRAW_COLOR = "var(--amber)";
const LOSS_COLOR = "var(--red)";

function TeamStatsBlock({ data, scopeLabel }) {
  const { t, num, dec } = useFormatters();
  const { seasons, totals, home_away: homeAway, best } = data;
  const pointsData = seasons.map((s) => ({ label: s.season, value: s.points ?? 0 }));
  const posData = seasons.map((s) => ({ label: s.season, value: s.position ?? 0 }));
  const wdl = [
    { label: t("page.team.wdl.won"), value: totals.won, color: WIN_COLOR },
    { label: t("page.team.wdl.drawn"), value: totals.drawn, color: DRAW_COLOR },
    { label: t("page.team.wdl.lost"), value: totals.lost, color: LOSS_COLOR },
  ];
  const winPctData = [];
  if (homeAway.home) winPctData.push({ label: t("page.team.venue.home"), value: homeAway.home.win_pct });
  if (homeAway.away) winPctData.push({ label: t("page.team.venue.away"), value: homeAway.away.win_pct });

  return (
    <>
      <div className="kpi-row">
        <StatCard label={t("page.team.matchesKpi", { scope: scopeLabel })} value={num(totals.played)} />
        <StatCard label={t("page.team.recordKpi", { scope: scopeLabel })} value={`${totals.won}W-${totals.drawn}D-${totals.lost}L`} />
        <StatCard
          label={t("page.team.goalsKpi", { scope: scopeLabel })}
          value={`${totals.goals_for} : ${totals.goals_against}`}
          sub={`${t("page.team.gd")} ${totals.goal_difference >= 0 ? "+" : ""}${totals.goal_difference}`}
        />
        <StatCard
          label={t("page.team.pointsKpi", { scope: scopeLabel })}
          value={num(totals.points)}
          sub={`${dec(totals.ppg, 2)} ${t("page.team.ppg")}`}
        />
        <StatCard
          label={t("page.team.bestFinish")}
          value={best?.position != null ? `#${best.position}` : "—"}
          sub={
            best?.position_season
              ? `${best.position_season} · ${num(best.points)} ${t("common.pts")}`
              : "—"
          }
        />
      </div>
      <p className="detail-note">
        {t("page.team.statsSummary", { scope: scopeLabel })}
      </p>
      <div className="team-stats">
        <Card as="div" className="panel">
          <BarList title={t("page.team.chart.points")} data={pointsData} color={POINTS_COLOR} format={(v) => `${v} ${t("common.pts")}`} />
        </Card>
        <Card as="div" className="panel">
          <BarList title={t("page.team.chart.position")} data={posData} color={POSITION_COLOR} format={(v) => `#${v}`} />
        </Card>
        <Card as="div" className="panel">
          <Donut title={t("page.team.chart.wdl", { n: totals.played })} segments={wdl} center={num(totals.played)} />
        </Card>
        <Card as="div" className="panel">
          <BarList title={t("page.team.chart.winByVenue")} data={winPctData} color={WIN_COLOR} format={(v) => `${v}%`} />
        </Card>
      </div>
    </>
  );
}

function seasonYear(m) {
  if (typeof m?.start_year === "number") return m.start_year;
  const year = parseInt(String(m?.season || "").split("-")[0], 10);
  return Number.isFinite(year) ? year : 0;
}

export default function TeamDetail() {
  const { t, num, kickoffDay, kickoffTime, plainDay } = useFormatters();
  const { slug } = useParams();
  const detail = useApi(() => api.team(slug), [slug]);

  // A stable identity for "no memberships yet". An inline `|| []` allocated a new
  // array on every render, so each `memberships` dependency below compared unequal
  // each time and the memos and effects that list it recomputed unconditionally.
  const memberships = detail.data?.memberships || NO_MEMBERSHIPS;

  const leagues = useMemo(() => {
    const seen = new Map();
    for (const m of memberships) if (!seen.has(m.league)) seen.set(m.league, m);
    return [...seen.values()].sort((a, b) => (a.league_name || "").localeCompare(b.league_name || ""));
  }, [memberships]);

  const [searchParams, patch] = useParamsPatch();
  const leagueParam = searchParams.get("league");
  const seasonParam = searchParams.get("season");

  // Both selects derive from the URL, which every handler patches, so a deep
  // link and a click cannot disagree and no effect has to copy either back into
  // state. An unknown league falls back to the first one; a season that is not
  // one of that league's memberships falls back to its latest.
  const league =
    leagueParam && leagues.some((l) => l.league === leagueParam)
      ? leagueParam
      : leagues[0]?.league || "";

  const seasonRows = memberships.filter((m) => m.league === league);
  const latestSeason = seasonRows.reduce(
    (best, m) => (!best || seasonYear(m) >= seasonYear(best) ? m : best),
    null,
  )?.season;
  const season =
    seasonParam && seasonRows.some((m) => m.season === seasonParam)
      ? seasonParam
      : latestSeason || "";

  // The selected league is held as a slug; the headings below show its real name.
  const leagueNames = useMemo(() => leagueNameMap(leagues), [leagues]);
  const leagueName = leagueLabel(league, leagueNames) || league;

  const onLeagueChange = (value) => patch({ league: value, season: "" });
  const onSeasonChange = (value) => patch({ season: value });

  const seasonMatches = memberships.filter((m) => m.league === league && m.season === season);
  const apiName = seasonMatches[0]?.api_name || detail.data?.team?.canonical_name || slug;

  const form = useApi(
    () => (league && season ? api.teamForm(slug, { league, season, n: 8 }) : null),
    [slug, league, season],
  );
  const standing = useApi(
    () => (league && season ? api.teamStandings(slug, { league, season }) : null),
    [slug, league, season],
  );
  const matches = useApi(
    () => (league && season ? api.teamMatches(slug, { league, season, limit: 10, offset: 0 }) : null),
    [slug, league, season],
  );
  // Scoped to the selected season like everything else on the page; the
  // response also carries `scope` so the panel can say which window it shows.
  const stats = useApi(
    () => (league && season ? api.teamStats(slug, { league, view: "classic", season }) : null),
    [slug, league, season],
  );
  const fixtures = useApi(() => (league ? api.leagueFixtures(league) : null), [league]);

  const upcoming = useMemo(() => {
    if (!fixtures.data) return [];
    const needles = [
      apiName,
      detail.data?.team?.canonical_name,
      ...memberships.filter((m) => m.league === league).map((m) => m.api_name),
    ]
      .filter(Boolean)
      .map((n) => n.toLowerCase());
    return (fixtures.data.matches || []).filter((m) => {
      const h = (m.home_team || "").toLowerCase();
      const a = (m.away_team || "").toLowerCase();
      return needles.some((n) => h.includes(n) || a.includes(n));
    });
  }, [fixtures.data, memberships, league, apiName, detail.data?.team?.canonical_name]);

  if (detail.loading)
    return (
      <div>
        <div className="page-head">
          <div className="page-heading">
            <Skeleton height={36} width="40%" />
            <Skeleton height={14} width="25%" />
          </div>
        </div>
        <TableSkeleton rows={4} cols={4} />
        <TableSkeleton rows={4} cols={4} />
      </div>
    );
  if (detail.error) return <ErrorBox error={detail.error} />;

  const team = detail.data?.team;

  return (
    <div>
      <BackLink to="/teams">{t("page.team.back")}</BackLink>
      <PageHeader
        title={
          <>
            {apiName}
            {seasonMatches[0]?.logo_url && (
              <img className="team-crest" src={seasonMatches[0].logo_url} alt="" width={28} height={28} decoding="async" />
            )}
          </>
        }
        subtitle={
          <>
            <span className="muted">{t("page.teams.canonical")}:</span> {team?.canonical_name}
          </>
        }
        actions={
          <Link className="link" to={`/teams/${slug}/kpi?league=${league}&season=${season || ""}`}>
            {t("page.team.kpiLink")} →
          </Link>
        }
      />

      <Card className="detail-filters">
        <CardHeader title={t("page.team.scopeTitle")} />
        <div className="filters">
          <select aria-label={t("page.matches.league")} value={league} onChange={(e) => onLeagueChange(e.target.value)}>
            {leagues.map((l) => (
              <option key={l.league} value={l.league}>
                {l.league_name}
              </option>
            ))}
          </select>
          <select
            aria-label={t("common.season")}
            value={season}
            onChange={(e) => onSeasonChange(e.target.value)}
            disabled={!league}
          >
            <option value="">{t("page.league.seasonPrompt")}</option>
            {memberships
              .filter((m) => m.league === league)
              .map((m) => (
                <option key={m.season} value={m.season}>
                  {m.season}
                </option>
              ))}
          </select>
        </div>
      </Card>

      <div className="detail-stack">
        <div className="two-col">
          {standing.data && league && season && (
            <Card>
              <CardHeader title={t("page.team.standings", { season })} />
              {standing.data.row ? (
                <TableShell>
                  <table className="data">
                    <tbody>
                      <tr><th scope="row">{t("table.pos")}</th><td>{standing.data.row.position}</td></tr>
                      <tr><th scope="row">{t("page.team.record")}</th><td>{standing.data.row.won}W-{standing.data.row.drawn}D-{standing.data.row.lost}L</td></tr>
                      <tr><th scope="row">{t("page.team.goals")}</th><td>{standing.data.row.goals_for} : {standing.data.row.goals_against} ({standing.data.row.goal_difference >= 0 ? "+" : ""}{standing.data.row.goal_difference})</td></tr>
                      <tr><th scope="row">{t("page.team.points")}</th><td><strong>{standing.data.row.points}</strong></td></tr>
                    </tbody>
                  </table>
                </TableShell>
              ) : (
                <p className="muted">{t("page.team.notInTable")}</p>
              )}
            </Card>
          )}

          {form.data && (
            <Card>
              <CardHeader title={t("page.team.recentForm")} />
              <FormPills results={form.data.results} />
              <div className="event-list detail-events">
                {form.data.results.map((r, i) => (
                  <div key={i} className="event">
                    <div className="teams">
                      <span className="detail-subtle">{plainDay(r.date)}</span>
                      <span><TeamLink name={r.home_team} /> {t("common.vs")} <TeamLink name={r.away_team} /></span>
                    </div>
                    <div className="score muted">
                      {r.home_score} – {r.away_score} <span className={`pill ${r.team_result}`}>{r.team_result}</span>
                    </div>
                  </div>
                ))}
              </div>
            </Card>
          )}
        </div>

        {upcoming.length > 0 && league && (
          <Card>
            <CardHeader title={t("page.team.upcoming", { league: leagueName })} />
            <div className="event-list">
              {upcoming.map((m, i) => (
                <div key={i} className="event">
                  <div className="teams">
                    <span className="detail-subtle">
                      {kickoffDay(m.match_date, m.time)} {kickoffTime(m.match_date, m.time)}
                    </span>
                    <span><TeamLink name={m.home_team} /> {t("common.vs")} <TeamLink name={m.away_team} /></span>
                  </div>
                  <MatchOutlook predictions={m.model_predictions?.dc_v2?.calibrated} compact />
                </div>
              ))}
            </div>
          </Card>
        )}

        {matches.data && (
          <Card>
            <CardHeader title={t("page.team.recentMatches", { n: num(matches.data.total) })} />
            <TableShell>
              <table className="data">
                <thead>
                  <tr><th scope="col">{t("common.date")}</th><th scope="col">{t("common.home")}</th><th scope="col" className="num">{t("common.score")}</th><th scope="col">{t("common.away")}</th><th scope="col">{t("common.detail")}</th></tr>
                </thead>
                <tbody>
                  {matches.data.matches.map((m) => (
                    <tr key={m.api_id}>
                      <td>{plainDay(m.match_date)}</td>
                      <td><TeamLink name={m.home_team} /></td>
                      <td className="num"><strong>{m.home_score} – {m.away_score}</strong></td>
                      <td><TeamLink name={m.away_team} /></td>
                      <td>
                        <Link className="link" to={`/match/${m.api_id}`}>
                          {t("common.view")}
                        </Link>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </TableShell>
          </Card>
        )}

        <Card>
          <CardHeader title={t("page.team.statistics", { league: leagueName })} />
          {stats.error && <ErrorBox error={stats.error} />}
          {stats.loading && (
            <div className="team-stats">
              {Array.from({ length: 4 }, (_, i) => (
                <Card as="div" className="panel" key={i}>
                  <Skeleton width="60%" height={13} />
                  <Skeleton height={90} />
                </Card>
              ))}
            </div>
          )}
          {stats.data && !stats.loading && (
            stats.data.seasons.length === 0 ? (
              <p className="muted">{t("page.team.noStats", { league: leagueName })}</p>
            ) : (
              <TeamStatsBlock
                data={stats.data}
                scopeLabel={stats.data.scope === "all" ? t("page.team.scopeAll") : stats.data.scope}
              />
            )
          )}
        </Card>

        {memberships.length > 0 && (
          <Card>
            <CardHeader
              title={t("page.team.seasonsCount", { n: num(memberships.length) })}
              actions={<Badge tone="green">{leagueName}</Badge>}
            />
            <TableShell>
              <table className="data">
                <thead>
                  <tr><th scope="col">{t("common.league")}</th><th scope="col">{t("common.seasonsCol")}</th><th scope="col">{t("page.team.apiName")}</th></tr>
                </thead>
                <tbody>
                  {memberships.map((m, i) => (
                    <tr key={i}>
                      <td>{m.league_name || m.league}</td>
                      <td>{m.season}</td>
                      <td>{m.api_name}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </TableShell>
          </Card>
        )}
      </div>
    </div>
  );
}
