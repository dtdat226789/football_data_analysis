import { useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, ListSkeleton, TableSkeleton } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import PredictionChips from "../components/PredictionChips.jsx";

const SIZES = [20, 50, 100];
const PRESETS = [
  { label: "7d", days: 7 },
  { label: "14d", days: 14 },
  { label: "30d", days: 30 },
];

function isoDaysAgo(days) {
  return new Date(Date.now() - days * 86400000).toISOString().slice(0, 10);
}

function pageLabel(pageSize, offset, total) {
  if (!total) return "0 matches";
  const end = Math.min(offset + pageSize, total);
  const start = Math.min(offset + 1, total);
  return `${start}–${end} of ${total}`;
}

export default function Matches() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [size, setSize] = useState(50);

  const league = searchParams.get("league") ?? "";
  const fromDate = searchParams.get("from") ?? "";
  const toDate = searchParams.get("to") ?? "";
  const offset = Number(searchParams.get("offset") || 0);

  const patch = (updates) => {
    const next = new URLSearchParams(searchParams);
    for (const [key, value] of Object.entries(updates)) {
      if (value) next.set(key, value);
      else next.delete(key);
    }
    setSearchParams(next);
  };

  const leaguesApi = useApi(() => api.listLeagues(), []);
  const upcoming = useApi(
    () => api.fixtures({ league: league || undefined, sort: "confidence", limit: 50 }),
    [league],
  );
  const recent = useApi(
    () =>
      api.matchesRecent({
        league: league || undefined,
        limit: size,
        offset,
        from_date: fromDate || undefined,
        to_date: toDate || undefined,
      }),
    [league, fromDate, toDate, offset, size],
  );

  const setLeague = (value) => patch({ league: value, offset: 0 });
  const changeDate = (field) => (e) => patch({ [field]: e.target.value, offset: 0 });
  const resetDates = () => patch({ from: "", to: "", offset: 0 });
  const preset = (days) => patch({ from: isoDaysAgo(days), to: "", offset: 0 });
  const changeSize = (e) => {
    setSize(Number(e.target.value));
    patch({ offset: 0 });
  };
  const page = (delta) => patch({ offset: Math.max(0, offset + delta * size) });

  const recentData = recent.data;

  return (
    <div>
      <div className="page-head">
        <h2>Matches</h2>
        <p>{league || "all leagues"} · upcoming top picks + recent results</p>
      </div>

      <div className="filters">
        <select aria-label="League" value={league} onChange={(e) => setLeague(e.target.value)}>
          <option value="">All leagues</option>
          {(leaguesApi.data || []).map((l) => (
            <option key={l.slug} value={l.slug}>
              {l.name}
            </option>
          ))}
        </select>
        <label className="muted" style={{ fontSize: 13 }}>
          From
        </label>
        <input type="date" aria-label="From date" value={fromDate} onChange={changeDate("from")} />
        <label className="muted" style={{ fontSize: 13 }}>
          To
        </label>
        <input type="date" aria-label="To date" value={toDate} onChange={changeDate("to")} />
        {(fromDate || toDate) && (
          <button
            className="tab-btn"
            onClick={resetDates}
            style={{ border: "1px solid var(--border)", background: "var(--card)", color: "var(--text)", borderRadius: 8, padding: "6px 10px", cursor: "pointer" }}
          >
            Reset dates
          </button>
        )}
        <span className="tab-spacer" />
        <label className="muted" style={{ fontSize: 13, display: "inline-flex", alignItems: "center", gap: 6 }}>
          Show{" "}
          <select aria-label="Page size" value={size} onChange={changeSize}>
            {SIZES.map((s) => (
              <option key={s} value={s}>
                {s}
              </option>
            ))}
          </select>
        </label>
        <div className="date-presets">
          {PRESETS.map((p) => (
            <button
              key={p.days}
              className="preset"
              onClick={() => preset(p.days)}
              title={`Recent results for the last ${p.days} days`}
            >
              {p.label}
            </button>
          ))}
          <button className="preset" onClick={resetDates} title="Clear date filters">
            All dates
          </button>
        </div>
      </div>

      <div className="two-col">
        <section className="card">
          <h3 style={{ marginTop: 0 }}>
            Upcoming <span className="badge">{upcoming.data?.total ?? 0}</span>
          </h3>
          {upcoming.loading && <ListSkeleton items={4} />}
          {upcoming.error && <ErrorBox error={upcoming.error} />}
          {upcoming.data && upcoming.data.matches.length === 0 && (
            <p className="muted">No upcoming fixtures{league ? " for this league" : ""}.</p>
          )}
          {upcoming.data && upcoming.data.matches.length > 0 && (
            <div className="event-list">
              {upcoming.data.matches.map((m, i) => (
                <div key={i} className="event">
                  <div className="teams">
                    <span className="muted" style={{ fontSize: 12 }}>
                      {m.match_date} {m.time} · {m.league}
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
                </div>
              ))}
            </div>
          )}
        </section>

        <section className="card">
          <h3 style={{ marginTop: 0 }}>
            Recent <span className="badge">{recentData?.total ?? 0}</span>
          </h3>
          {recent.loading && <TableSkeleton rows={6} cols={5} />}
          {recent.error && <ErrorBox error={recent.error} />}
          {recentData && (
            <table className="data">
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Home</th>
                  <th className="num">Score</th>
                  <th>Away</th>
                  <th>League</th>
                  <th>Detail</th>
                </tr>
              </thead>
              <tbody>
                {recentData.matches.map((m) => (
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
                    <td className="muted">{m.league}</td>
                    <td>
                      <Link className="link" to={`/match/${m.api_id}`}>
                        view
                      </Link>
                    </td>
                  </tr>
                ))}
                {recentData.matches.length === 0 && (
                  <tr>
                    <td colSpan={6} className="muted">
                      No finished matches match the filters.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          )}
          {recentData && recentData.total > 0 && (
            <div className="pagination">
              <button disabled={offset === 0} onClick={() => page(-1)}>
                ‹ Prev
              </button>
              <span className="muted">{pageLabel(size, offset, recentData.total)}</span>
              <button disabled={offset + size >= recentData.total} onClick={() => page(1)}>
                Next ›
              </button>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}