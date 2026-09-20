import { useState } from "react";
import { useLeagues } from "../state/LeaguesContext.jsx";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Loading } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";

const VIEWS = [
  { key: "classic", label: "Classic" },
  { key: "luck", label: "Luck" },
  { key: "goals", label: "Goals" },
];

export default function Standings() {
  const { league, season } = useLeagues();
  const [view, setView] = useState("classic");
  const { data, loading, error } = useApi(
    () => (league && season ? api.standings(league, { season, view }) : null),
    [league, season, view],
  );

  if (loading) return <Loading label="Loading standings…" />;
  if (error) return <ErrorBox error={error} />;
  if (!data || data.rows.length === 0) return <ErrorBox error="No standings rows." />;

  const { rows } = data;
  return (
    <div>
      <div className="page-head">
        <h2>Standings</h2>
        <p>
          {league} · {data.season} · {VIEWS.find((v) => v.key === data.view)?.label} view
        </p>
      </div>

      <div className="tabs">
        {VIEWS.map((v) => (
          <button key={v.key} className={view === v.key ? "active" : ""} onClick={() => setView(v.key)}>
            {v.label}
          </button>
        ))}
      </div>

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
            {rows.map((r) => (
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
    </div>
  );
}