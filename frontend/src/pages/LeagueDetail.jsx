import { useEffect, useMemo, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Empty, ListSkeleton, Skeleton, TableSkeleton } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import ChartGrid from "../components/ChartGrid.jsx";
import PredictionChips from "../components/PredictionChips.jsx";

const VIEWS = [
  { key: "classic", label: "Classic" },
  { key: "luck", label: "Luck" },
  { key: "goals", label: "Goals" },
];

const TABS = [
  { key: "standings", label: "Standings" },
  { key: "analysis", label: "Analysis" },
  { key: "matches", label: "Matches" },
  { key: "seasons", label: "Seasons" },
];

function fmt(v, digits) {
  if (typeof v !== "number") return v ?? "—";
  return digits != null ? v.toFixed(digits) : v.toLocaleString();
}

function StandingsTab({ league, season, view, setView }) {
  const { data, loading, error } = useApi(
    () => api.standings(league, { season, view }),
    [league, season, view],
  );
  return (
    <div>
      <div className="tabs">
        {VIEWS.map((v) => (
          <button key={v.key} className={view === v.key ? "active" : ""} onClick={() => setView(v.key)}>
            {v.label}
          </button>
        ))}
      </div>
      {loading && <TableSkeleton rows={8} cols={10} />}
      {error && <ErrorBox error={error} />}
      {!loading && !error && data && (
        <div className="card">
          <table className="data">
            <thead>
              <tr>
                <th>Pos</th>
                <th>Team</th>
                <th className="num">P</th>
                <th className="num">W</th>
                <th className="num">D</th>
                <th className="num">L</th>
                <th className="num">GF</th>
                <th className="num">GA</th>
                <th className="num">GD</th>
                <th className="num">Pts</th>
              </tr>
            </thead>
            <tbody>
              {data.rows.map((r) => (
                <tr key={r.team}>
                  <td>{r.position}</td>
                  <td>
                    <TeamLink name={r.team} />
                  </td>
                  <td className="num">{r.played}</td>
                  <td className="num">{r.won}</td>
                  <td className="num">{r.drawn}</td>
                  <td className="num">{r.lost}</td>
                  <td className="num">{r.goals_for}</td>
                  <td className="num">{r.goals_against}</td>
                  <td className="num">{r.goal_difference}</td>
                  <td className="num">
                    <strong>{r.points}</strong>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

function AnalysisTab({ league }) {
  const { data, loading, error } = useApi(() => api.analysis(league), [league]);
  if (loading)
    return (
      <div>
        <div className="kpi-row">
          {Array.from({ length: 5 }, (_, i) => (
            <div key={i} className="kpi">
              <Skeleton width="70%" height={12} />
              <Skeleton width="40%" height={18} />
            </div>
          ))}
        </div>
        <Skeleton height={120} />
      </div>
    );
  if (error) return <ErrorBox error={error} />;
  if (!data || !data.has_data) {
    return (
      <Empty>
        No analysis reports for {league}. Run <code>run_analysis.py --league {league}</code> first.
      </Empty>
    );
  }
  const { reports, charts, meta } = data;
  const overall = reports.matches_analysis?.overall;
  const findings = reports.findings?.key_findings || [];
  const kpis = [
    { label: "Total matches", value: fmt(overall?.n_matches) },
    { label: "Avg goals / match", value: fmt(overall?.avg_goals, 2) },
    { label: "Home win %", value: `${fmt(overall?.home_win_pct, 1)}%` },
    { label: "Draw %", value: `${fmt(overall?.draw_pct, 1)}%` },
    { label: "Away win %", value: `${fmt(overall?.away_win_pct, 1)}%` },
  ];
  return (
    <div>
      <div className="kpi-row">
        {kpis.map((k) => (
          <div key={k.label} className="kpi">
            <div className="label">{k.label}</div>
            <div className="value">{k.value}</div>
          </div>
        ))}
      </div>
      <section className="card" style={{ marginTop: 16 }}>
        <h3 style={{ marginTop: 0 }}>Key findings</h3>
        {findings.length === 0 ? (
          <p className="muted">No findings recorded.</p>
        ) : (
          <ol style={{ paddingLeft: 20, lineHeight: 1.6 }}>
            {findings.map((f, i) => (
              <li key={i}>
                <strong>
                  <span className="badge green">F{f.id}</span> {f.finding}
                </strong>
                <div className="muted" style={{ fontSize: 13 }}>
                  {f.detail}
                </div>
              </li>
            ))}
          </ol>
        )}
      </section>
      {charts.length > 0 && (
        <section style={{ marginTop: 16 }}>
          <h3>Charts</h3>
          <p className="muted" style={{ fontSize: 13 }}>
            Select a chart to view it full screen.
          </p>
          <ChartGrid league={league} charts={charts} />
        </section>
      )}
    </div>
  );
}

function MatchesTab({ league, season }) {
  const recent = useApi(() => api.matches(league, { season, limit: 20 }), [league, season]);
  const upcoming = useApi(() => api.leagueFixtures(league), [league]);
  return (
    <div className="two-col">
      <section className="card">
        <h3 style={{ marginTop: 0 }}>Upcoming · {season}</h3>
        {upcoming.loading && <ListSkeleton items={3} />}
        {upcoming.error && <ErrorBox error={upcoming.error} />}
        {upcoming.data && upcoming.data.matches.length === 0 && (
          <p className="muted">No collected fixtures for this league.</p>
        )}
        {upcoming.data && upcoming.data.matches.length > 0 && (
          <div className="event-list">
            {upcoming.data.matches.map((m, i) => (
              <div key={m.slug || i} className="event">
                <div className="teams">
                  <span className="muted" style={{ fontSize: 12 }}>
                    {m.match_date} {m.time}
                  </span>
                  <span>
                    <TeamLink name={m.home_team} /> vs <TeamLink name={m.away_team} />
                  </span>
                </div>
                <PredictionChips predictions={m.model_predictions?.dc_v2?.calibrated} compact />
              </div>
            ))}
          </div>
        )}
      </section>

      <section className="card">
        <h3 style={{ marginTop: 0 }}>Recent · {season}</h3>
        {recent.loading && <TableSkeleton rows={6} cols={4} />}
        {recent.error && <ErrorBox error={recent.error} />}
        {recent.data && (
          <table className="data">
            <thead>
              <tr>
                <th>Date</th>
                <th>Home</th>
                <th className="num">Score</th>
                <th>Away</th>
                <th>Detail</th>
              </tr>
            </thead>
            <tbody>
              {recent.data.matches.map((m) => (
                <tr key={m.api_id}>
                  <td>{m.match_date}</td>
                  <td>
                    <TeamLink name={m.home_team} />
                  </td>
                  <td className="num">
                    <strong>
                      {m.home_score} – {m.away_score}
                    </strong>
                  </td>
                  <td>
                    <TeamLink name={m.away_team} />
                  </td>
                  <td>
                    <Link className="link" to={`/match/${m.api_id}`}>
                      view
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </div>
  );
}

function SeasonsTab({ detail }) {
  const seasons = detail.seasons || [];
  return (
    <div className="card">
      <table className="data">
        <thead>
          <tr>
            <th>Season</th>
            <th>Start</th>
            <th>End</th>
            <th className="num">Matches</th>
            <th className="num">Teams</th>
            <th className="num">Standings</th>
            <th>State</th>
          </tr>
        </thead>
        <tbody>
          {seasons.map((s) => (
            <tr key={s.season}>
              <td>{s.season}</td>
              <td>{s.start_year}</td>
              <td>{s.end_year}</td>
              <td className="num">{s.matches}</td>
              <td className="num">{s.teams}</td>
              <td className="num">{s.standings_rows}</td>
              <td>{s.season_state}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default function LeagueDetail() {
  const { slug } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();

  const tab = searchParams.get("tab") || "standings";
  const view = searchParams.get("view") || "classic";
  const urlSeason = searchParams.get("season");

  const patch = (updates) => {
    const next = new URLSearchParams(searchParams);
    for (const [key, value] of Object.entries(updates)) {
      if (value) next.set(key, value);
      else next.delete(key);
    }
    setSearchParams(next);
  };

  const [season, setSeason] = useState(urlSeason || null);
  useEffect(() => {
    if (urlSeason) setSeason(urlSeason);
  }, [urlSeason]);

  const detail = useApi(() => api.league(slug), [slug]);

  const seasons = useMemo(
    () => (detail.data?.seasons ? [...detail.data.seasons].sort((a, b) => a.start_year - b.start_year) : []),
    [detail.data],
  );
  const latestSeason = useMemo(() => {
    const withMatches = seasons.filter((s) => s.matches > 0);
    const pool = withMatches.length ? withMatches : seasons;
    return pool.length ? pool[pool.length - 1].season : null;
  }, [seasons]);

  useEffect(() => {
    if (latestSeason) setSeason((cur) => cur || latestSeason);
  }, [latestSeason]);

  if (detail.loading)
    return (
      <div>
        <div className="page-head">
          <Skeleton height={34} width="45%" />
          <Skeleton height={14} width="30%" />
        </div>
        <TableSkeleton rows={6} cols={10} />
      </div>
    );
  if (detail.error) return <ErrorBox error={detail.error} />;
  if (!detail.data) return <ErrorBox error="No league data." />;

  const meta = detail.data;
  const setTab = (key) => patch({ tab: key });
  const setView = (v) => patch({ view: v });
  const changeSeason = (value) => {
    setSeason(value);
    patch({ season: value });
  };

  return (
    <div>
      <div className="page-head">
        <h2>{meta.name}</h2>
        <p>
          {meta.country} · {meta.region} · {meta.format} · {meta.teams} teams · {seasons.length} seasons
        </p>
      </div>

      <div className="tabs">
        {TABS.map((t) => (
          <button key={t.key} className={tab === t.key ? "active" : ""} onClick={() => setTab(t.key)}>
            {t.label}
          </button>
        ))}
        <span className="tab-spacer" />
        <select aria-label="Season" value={season || ""} onChange={(e) => changeSeason(e.target.value)}>
          <option value="">Season…</option>
          {seasons.map((s) => (
            <option key={s.season} value={s.season}>
              {s.season} {s.matches === 0 ? "(no data)" : ""}
            </option>
          ))}
        </select>
      </div>

      {tab === "standings" && <StandingsTab league={slug} season={season} view={view} setView={setView} />}
      {tab === "analysis" && <AnalysisTab league={slug} />}
      {tab === "matches" && <MatchesTab league={slug} season={season} />}
      {tab === "seasons" && <SeasonsTab detail={detail.data} />}
    </div>
  );
}