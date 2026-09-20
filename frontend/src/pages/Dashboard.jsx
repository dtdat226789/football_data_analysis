import { useLeagues } from "../state/LeaguesContext.jsx";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Empty, Loading } from "../components/State.jsx";

function fmt(v, digits) {
  if (typeof v !== "number") return v ?? "—";
  return digits != null ? v.toFixed(digits) : v.toLocaleString();
}

export default function Dashboard() {
  const { league, detail, latestSeason } = useLeagues();
  const { data, loading, error } = useApi(() => (league ? api.analysis(league) : null), [league]);

  if (loading) return <Loading label="Loading analysis bundle…" />;
  if (error) return <ErrorBox error={error} />;
  if (!data || !data.has_data) {
    return (
      <Empty>
        No analysis reports for {league}. Run <code>run_analysis.py --league {league}</code> first.
      </Empty>
    );
  }

  const { reports, charts, meta } = data;
  const ma = reports.matches_analysis;
  const overall = ma?.overall;
  const head = reports.findings?.headline_stats;
  const findings = reports.findings?.key_findings || [];
  const anomalies = reports.findings?.anomalies || [];
  const champions = reports.season_trends?.champions || [];
  const comparison = reports.findings?.comparison || [];

  const kpis = [
    { label: "Total matches", value: fmt(overall?.n_matches) },
    { label: "Avg goals / match", value: fmt(overall?.avg_goals, 2) },
    { label: "Home win %", value: `${fmt(overall?.home_win_pct, 1)}%` },
    { label: "Draw %", value: `${fmt(overall?.draw_pct, 1)}%` },
    { label: "Away win %", value: `${fmt(overall?.away_win_pct, 1)}%` },
    { label: "Most common scoreline", value: head?.most_common_scoreline ?? fmt(overall?.goalless ? `0-0` : "—") },
    { label: "Dominant team", value: head?.dominant_team ?? "—" },
    { label: "Champion (most titles)", value: head?.champion_most_titles ?? "—" },
  ];

  return (
    <div>
      <div className="page-head">
        <h2>Dashboard — {meta?.name}</h2>
        <p>
          {meta?.country} · {meta?.format} · {detail?.seasons?.length ?? "—"} seasons · latest: {latestSeason}
        </p>
      </div>

      <div className="kpi-row">
        {kpis.map((k) => (
          <div key={k.label} className="kpi">
            <div className="label">{k.label}</div>
            <div className="value">{k.value}</div>
          </div>
        ))}
      </div>

      <div className="grid" style={{ gridTemplateColumns: "2fr 1fr" }}>
        <section className="card">
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

        <div className="grid">
          <section className="card">
            <h3 style={{ marginTop: 0 }}>Champions</h3>
            {champions.length === 0 ? (
              <p className="muted">—</p>
            ) : (
              <ul style={{ paddingLeft: 18, lineHeight: 1.8, margin: 0 }}>
                {champions
                  .slice()
                  .reverse()
                  .map((c) => (
                    <li key={c.season}>
                      <strong>{c.season}</strong>: {c.champion} ({c.champion_pts} pts,
                      margin {c.margin_pts})
                    </li>
                  ))}
              </ul>
            )}
          </section>

          {anomalies.length > 0 && (
            <section className="card">
              <h3 style={{ marginTop: 0 }}>
                Anomalies <span className="badge amber">{anomalies.length}</span>
              </h3>
              <ul style={{ paddingLeft: 18, lineHeight: 1.5, margin: 0, fontSize: 13 }}>
                {anomalies.map((a, i) => (
                  <li key={i}>
                    <span className="muted">{a.code}</span>: {a.message}
                  </li>
                ))}
              </ul>
            </section>
          )}
        </div>
      </div>

      {comparison.length > 0 && (
        <section className="card" style={{ marginTop: 16 }}>
          <h3 style={{ marginTop: 0 }}>Data health</h3>
          <table className="data">
            <thead>
              <tr>
                <th>Report</th>
                <th className="num">Size (kb)</th>
                <th>Sections</th>
              </tr>
            </thead>
            <tbody>
              {comparison.map((c) => (
                <tr key={c.module}>
                  <td>{c.module}</td>
                  <td className="num">{typeof c.size_kb === "number" ? c.size_kb.toFixed(1) : "—"}</td>
                  <td>{Array.isArray(c.sections) ? c.sections.join(", ") : "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}

      {charts.length > 0 && (
        <section style={{ marginTop: 16 }}>
          <h3>Charts</h3>
          <div className="chart-grid">
            {charts.map((c) => (
              <div key={c} className="card chart-card">
                <img src={api.chartUrl(league, c)} alt={c} loading="lazy" />
                <div className="caption">{c.replace(/\.png$/, "").replace(/_/g, " ")}</div>
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}