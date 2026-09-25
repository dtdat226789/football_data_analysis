import { useEffect, useMemo, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, ListSkeleton, Skeleton, TableSkeleton } from "../components/State.jsx";
import { FormPills } from "../components/FormPills.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import { BarList, Donut, StatCard } from "../components/Charts.jsx";
import PredictionChips from "../components/PredictionChips.jsx";

const POSITION_COLOR = "var(--green)";
const POINTS_COLOR = "var(--accent)";
const WIN_COLOR = "var(--green)";
const DRAW_COLOR = "var(--amber)";
const LOSS_COLOR = "var(--danger)";

function TeamStatsBlock({ data }) {
  const { seasons, totals, home_away: homeAway, best } = data;
  const pointsData = seasons.map((s) => ({ label: s.season, value: s.points ?? 0 }));
  const posData = seasons.map((s) => ({ label: s.season, value: s.position ?? 0 }));
  const wdl = [
    { label: "Won", value: totals.won, color: WIN_COLOR },
    { label: "Drawn", value: totals.drawn, color: DRAW_COLOR },
    { label: "Lost", value: totals.lost, color: LOSS_COLOR },
  ];
  const winPctData = [];
  if (homeAway.home) winPctData.push({ label: "Home", value: homeAway.home.win_pct });
  if (homeAway.away) winPctData.push({ label: "Away", value: homeAway.away.win_pct });

  return (
    <>
      <div className="kpi-row">
        <StatCard label="Matches" value={totals.played.toLocaleString()} />
        <StatCard label="Record" value={`${totals.won}W-${totals.drawn}D-${totals.lost}L`} />
        <StatCard
          label="Goals"
          value={`${totals.goals_for} : ${totals.goals_against}`}
          sub={`GD ${totals.goal_difference >= 0 ? "+" : ""}${totals.goal_difference}`}
        />
        <StatCard label="Points" value={totals.points.toLocaleString()} sub={`${totals.ppg} PPG`} />
        <StatCard label="Best finish" value={best?.position != null ? `#${best.position}` : "—"} sub={best?.position_season ?? "—"} />
      </div>
      <div className="team-stats">
        <div className="card panel">
          <BarList title="Points per season" data={pointsData} color={POINTS_COLOR} format={(v) => `${v} pts`} />
        </div>
        <div className="card panel">
          <BarList title="League position per season (lower is better)" data={posData} color={POSITION_COLOR} format={(v) => `#${v}`} />
        </div>
        <div className="card panel">
          <Donut title={`Win / draw / loss (${totals.played} games)`} segments={wdl} center={totals.played} />
        </div>
        <div className="card panel">
          <BarList title="Win % by venue" data={winPctData} color={WIN_COLOR} format={(v) => `${v}%`} />
        </div>
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
  const { slug } = useParams();
  const detail = useApi(() => api.team(slug), [slug]);

  const memberships = detail.data?.memberships || [];

  const leagues = useMemo(() => {
    const seen = new Map();
    for (const m of memberships) if (!seen.has(m.league)) seen.set(m.league, m);
    return [...seen.values()].sort((a, b) => (a.league_name || "").localeCompare(b.league_name || ""));
  }, [memberships]);

  const [league, setLeague] = useState("");
  const [season, setSeason] = useState("");
  const [searchParams, setSearchParams] = useSearchParams();
  const leagueParam = searchParams.get("league");
  const seasonParam = searchParams.get("season");

  useEffect(() => {
    if (leagueParam && league === "" && leagues.some((l) => l.league === leagueParam)) setLeague(leagueParam);
  }, [leagueParam, league, leagues]);
  useEffect(() => {
    if (leagues.length > 0 && !leagues.some((l) => l.league === league)) setLeague(leagues[0].league);
  }, [leagues, league]);
  useEffect(() => {
    const seasonRows = memberships.filter((m) => m.league === league);
    if (seasonRows.length === 0) return;
    const latest = seasonRows.reduce((best, m) =>
      seasonYear(m) >= seasonYear(best) ? m : best,
    );
    setSeason((cur) => {
      if (cur) return cur;
      if (seasonParam && seasonRows.some((m) => m.season === seasonParam)) return seasonParam;
      return latest.season;
    });
  }, [memberships, league, seasonParam]);

  const patch = (updates) => {
    const next = new URLSearchParams(searchParams);
    for (const [key, value] of Object.entries(updates)) {
      if (value) next.set(key, value);
      else next.delete(key);
    }
    setSearchParams(next);
  };
  const onLeagueChange = (value) => {
    setLeague(value);
    setSeason("");
    patch({ league: value, season: "" });
  };
  const onSeasonChange = (value) => {
    setSeason(value);
    patch({ season: value });
  };

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
  const stats = useApi(() => (league ? api.teamStats(slug, { league, view: "classic" }) : null), [slug, league]);
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
          <Skeleton height={36} width="40%" />
          <Skeleton height={14} width="25%" />
        </div>
        <TableSkeleton rows={4} cols={4} />
        <TableSkeleton rows={4} cols={4} />
      </div>
    );
  if (detail.error) return <ErrorBox error={detail.error} />;

  const team = detail.data?.team;

  return (
    <div>
      <div className="page-head">
        <h2>
          {apiName}
          {seasonMatches[0]?.logo_url && (
            <img src={seasonMatches[0].logo_url} alt="" style={{ height: 28, marginLeft: 10, verticalAlign: "middle" }} />
          )}
        </h2>
        <p>
          <span className="muted">canonical:</span> {team?.canonical_name} ·{" "}
          <span className="muted">slug:</span> {team?.canonical_slug}
        </p>
      </div>

      <div className="filters">
        <select aria-label="League" value={league} onChange={(e) => onLeagueChange(e.target.value)}>
          {leagues.map((l) => (
            <option key={l.league} value={l.league}>
              {l.league_name}
            </option>
          ))}
        </select>
        <select
          aria-label="Season"
          value={season}
          onChange={(e) => onSeasonChange(e.target.value)}
          disabled={!league}
        >
          <option value="">Season…</option>
          {memberships
            .filter((m) => m.league === league)
            .map((m) => (
              <option key={m.season} value={m.season}>
                {m.season}
              </option>
            ))}
        </select>
      </div>

      <div className="two-col">
        {standing.data && league && season && (
          <section className="card">
            <h3 style={{ marginTop: 0 }}>Standings · {season}</h3>
            {standing.data.row ? (
              <table className="data">
                <tbody>
                  <tr><th>Pos</th><td>{standing.data.row.position}</td></tr>
                  <tr><th>Record</th><td>{standing.data.row.won}W-{standing.data.row.drawn}D-{standing.data.row.lost}L</td></tr>
                  <tr><th>Goals</th><td>{standing.data.row.goals_for} : {standing.data.row.goals_against} ({standing.data.row.goal_difference >= 0 ? "+" : ""}{standing.data.row.goal_difference})</td></tr>
                  <tr><th>Points</th><td><strong>{standing.data.row.points}</strong></td></tr>
                </tbody>
              </table>
            ) : (
              <p className="muted">Not in this season's table.</p>
            )}
          </section>
        )}

        {form.data && (
          <section className="card">
            <h3 style={{ marginTop: 0 }}>Recent form</h3>
            <FormPills results={form.data.results} />
            <div className="event-list" style={{ marginTop: 12 }}>
              {form.data.results.map((r, i) => (
                <div key={i} className="event">
                  <div className="teams">
                    <span className="muted" style={{ fontSize: 12 }}>{r.date}</span>
                    <span><TeamLink name={r.home_team} /> vs <TeamLink name={r.away_team} /></span>
                  </div>
                  <div className="score muted">
                    {r.home_score} – {r.away_score} <span className={`pill ${r.team_result}`}>{r.team_result}</span>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}
      </div>

      {upcoming.length > 0 && league && (
        <section className="card" style={{ marginTop: 16 }}>
          <h3 style={{ marginTop: 0 }}>Upcoming · {league}</h3>
          <div className="event-list">
            {upcoming.map((m, i) => (
              <div key={i} className="event">
                <div className="teams">
                  <span className="muted" style={{ fontSize: 12 }}>{m.match_date} {m.time}</span>
                  <span><TeamLink name={m.home_team} /> vs <TeamLink name={m.away_team} /></span>
                </div>
                <PredictionChips predictions={m.model_predictions?.dc_v2?.calibrated} compact />
              </div>
            ))}
          </div>
        </section>
      )}

      {matches.data && (
        <section className="card" style={{ marginTop: 16 }}>
          <h3 style={{ marginTop: 0 }}>Recent matches ({matches.data.total})</h3>
          <table className="data">
            <thead>
              <tr><th>Date</th><th>Home</th><th className="num">Score</th><th>Away</th><th>Detail</th></tr>
            </thead>
            <tbody>
              {matches.data.matches.map((m) => (
                <tr key={m.api_id}>
                  <td>{m.match_date}</td>
                  <td><TeamLink name={m.home_team} /></td>
                  <td className="num"><strong>{m.home_score} – {m.away_score}</strong></td>
                  <td><TeamLink name={m.away_team} /></td>
                  <td>
                    <Link className="link" to={`/match/${m.api_id}`}>
                      view
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}

      <section className="card" style={{ marginTop: 16 }}>
        <h3 style={{ marginTop: 0 }}>Statistics · {league}</h3>
        {stats.error && <ErrorBox error={stats.error} />}
        {stats.loading && (
          <div className="team-stats">
            {Array.from({ length: 4 }, (_, i) => (
              <div key={i} className="card panel">
                <Skeleton width="60%" height={13} />
                <Skeleton height={90} />
              </div>
            ))}
          </div>
        )}
        {stats.data && !stats.loading && (
          stats.data.seasons.length === 0 ? (
            <p className="muted">No standings recorded for this team in {league}.</p>
          ) : (
            <TeamStatsBlock data={stats.data} />
          )
        )}
      </section>

      {memberships.length > 0 && (
        <section className="card" style={{ marginTop: 16 }}>
          <h3 style={{ marginTop: 0 }}>Seasons ({memberships.length})</h3>
          <table className="data">
            <thead>
              <tr><th>League</th><th>Season</th><th>API name</th><th>Slug</th></tr>
            </thead>
            <tbody>
              {memberships.map((m, i) => (
                <tr key={i}>
                  <td>{m.league} · {m.league_name}</td>
                  <td>{m.season}</td>
                  <td>{m.api_name}</td>
                  <td className="muted">{m.api_slug}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}
    </div>
  );
}