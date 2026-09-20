import { useState } from "react";
import { useLeagues } from "../state/LeaguesContext.jsx";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Loading } from "../components/State.jsx";
import Tree from "../components/DataTree.jsx";

const MODULES = [
  "database_profile",
  "matches_analysis",
  "goals_analysis",
  "teams_analysis",
  "season_trends",
  "scoreline_analysis",
  "relationships",
  "findings",
];

function pretty(name) {
  return name.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
}

function ModulePanel({ league, module }) {
  const { data, loading, error } = useApi(
    () => api.analysisModule(league, module),
    [league, module],
  );
  if (loading) return <Loading label={`Loading ${module}…`} />;
  if (error) return <ErrorBox error={error} />;
  const { report_name: _rn, script: _s, generated_at, config: _c, league: _l, ...body } = data;
  return (
    <div>
      <div className="muted" style={{ fontSize: 13, marginBottom: 12 }}>
        Generated {generated_at?.replace("T", " ").replace("+00:00", " UTC")}
      </div>
      <Tree value={body} />
    </div>
  );
}

function ChartsPanel({ league, charts }) {
  if (charts.length === 0) return <ErrorBox error="No charts generated for this league." />;
  return (
    <div className="chart-grid">
      {charts.map((c) => (
        <div key={c} className="card chart-card">
          <img src={api.chartUrl(league, c)} alt={c} loading="lazy" />
          <div className="caption">{c.replace(/\.png$/, "").replace(/_/g, " ")}</div>
        </div>
      ))}
    </div>
  );
}

export default function Analysis() {
  const { league } = useLeagues();
  const bundle = useApi(() => (league ? api.analysis(league) : null), [league]);
  const [tab, setTab] = useState("charts");

  if (bundle.loading) return <Loading label="Loading analysis…" />;
  if (bundle.error) return <ErrorBox error={bundle.error} />;
  if (!bundle.data?.has_data) {
    return <ErrorBox error={`No analysis reports for ${league}.`} />;
  }

  const data = bundle.data;
  const availableModules = MODULES.filter((m) => !data.missing.includes(m));

  return (
    <div>
      <div className="page-head">
        <h2>Analysis reports</h2>
        <p>
          {data.meta?.name} · {availableModules.length}/{MODULES.length} modules · {data.charts.length}{" "}
          charts
        </p>
      </div>

      <div className="tabs">
        <button className={tab === "charts" ? "active" : ""} onClick={() => setTab("charts")}>
          Charts ({data.charts.length})
        </button>
        {availableModules.map((m) => (
          <button key={m} className={tab === m ? "active" : ""} onClick={() => setTab(m)}>
            {pretty(m)}
          </button>
        ))}
      </div>

      {tab === "charts" ? (
        <ChartsPanel league={league} charts={data.charts} />
      ) : (
        <ModulePanel league={league} module={tab} />
      )}
    </div>
  );
}