import { useMemo, useState } from "react";
import { useLeagues } from "../state/LeaguesContext.jsx";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Loading } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";

const PAGE_SIZE = 50;

function MatchModal({ apiId, onClose }) {
  const { data, loading, error } = useApi(() => api.match(apiId), [apiId]);
  if (!loading && error) return null;
  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <button className="close" onClick={onClose}>
          ×
        </button>
        {loading ? (
          <Loading label="Loading match…" />
        ) : data ? (
          <>
            <h3>
              <TeamLink name={data.home_team} /> {data.home_score} – {data.away_score}{" "}
              <TeamLink name={data.away_team} />
            </h3>
            <div className="muted" style={{ marginBottom: 12 }}>
              {data.season} · {data.match_date} {data.kickoff_time} · game {data.game_index}
            </div>
            <table className="data">
              <tbody>
                <tr>
                  <th>Half-time</th>
                  <td>
                    {data.home_ht} – {data.away_ht}
                  </td>
                </tr>
                <tr>
                  <th>First goal</th>
                  <td>
                    {data.first_goal_time ?? "—"}
                    {data.first_goal_time_extra ? ` (${data.first_goal_time_extra}?)` : ""}
                  </td>
                </tr>
                <tr>
                  <th>API id</th>
                  <td>{data.api_id}</td>
                </tr>
              </tbody>
            </table>
          </>
        ) : null}
      </div>
    </div>
  );
}

export default function Matches() {
  const { league, season } = useLeagues();
  const [offset, setOffset] = useState(0);
  const [fromDate, setFromDate] = useState("");
  const [toDate, setToDate] = useState("");
  const [selected, setSelected] = useState(null);

  const params = useMemo(
    () => ({
      season,
      from_date: fromDate || undefined,
      to_date: toDate || undefined,
      limit: PAGE_SIZE,
      offset,
    }),
    [season, fromDate, toDate, offset],
  );

  const { data, loading, error } = useApi(
    () => (league ? api.matches(league, params) : null),
    [league, params],
  );

  const resetOffset = () => setOffset(0);

  return (
    <div>
      <div className="page-head">
        <h2>Matches</h2>
        <p>
          {league} · {data?.season ?? season} · {data ? `${data.total} matches` : "…"}
        </p>
      </div>

      <div className="filters">
        <label className="muted" style={{ fontSize: 13 }}>
          From
        </label>
        <input type="date" value={fromDate} onChange={(e) => { setFromDate(e.target.value); resetOffset(); }} />
        <label className="muted" style={{ fontSize: 13 }}>
          To
        </label>
        <input type="date" value={toDate} onChange={(e) => { setToDate(e.target.value); resetOffset(); }} />
        {(fromDate || toDate) && (
          <button
            className="tabs"
            style={{ border: "1px solid var(--border)", background: "var(--card)", color: "var(--text)", borderRadius: 8, padding: "6px 10px", cursor: "pointer" }}
            onClick={() => { setFromDate(""); setToDate(""); resetOffset(); }}
          >
            Clear filters
          </button>
        )}
      </div>

      {loading && <Loading label="Loading matches…" />}
      {error && <ErrorBox error={error} />}
      {!loading && !error && data && (
        <>
          <div className="card">
            <table className="data">
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Home</th>
                  <th className="num">Score</th>
                  <th>Away</th>
                  <th className="num">HT</th>
                </tr>
              </thead>
              <tbody>
                {data.matches.map((m) => (
                  <tr key={m.api_id} onClick={() => setSelected(m.api_id)} style={{ cursor: "pointer" }}>
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
                    <td className="num muted">
                      {m.home_ht} – {m.away_ht}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            {data.matches.length === 0 && <p className="muted">No matches for these filters.</p>}
          </div>

          <div className="pagination">
            <button disabled={offset === 0} onClick={() => setOffset(Math.max(0, offset - PAGE_SIZE))}>
              ‹ Prev
            </button>
            <span className="muted">
              {data.total === 0 ? 0 : offset + 1}–{Math.min(offset + PAGE_SIZE, data.total)} of {data.total}
            </span>
            <button
              disabled={offset + PAGE_SIZE >= data.total}
              onClick={() => setOffset(offset + PAGE_SIZE)}
            >
              Next ›
            </button>
          </div>

          {selected && <MatchModal apiId={selected} onClose={() => setSelected(null)} />}
        </>
      )}
    </div>
  );
}