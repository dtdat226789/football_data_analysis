import { NavLink, Navigate, Route, Routes } from "react-router-dom";
import { useLeagues } from "./state/LeaguesContext.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import Standings from "./pages/Standings.jsx";
import Matches from "./pages/Matches.jsx";
import Teams from "./pages/Teams.jsx";
import TeamDetail from "./pages/TeamDetail.jsx";
import Analysis from "./pages/Analysis.jsx";

export default function App() {
  const { leagues, league, setLeague, seasons, season, setSeason, error } = useLeagues();

  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <span className="brand-dot" />
          <h1>Football Data</h1>
          <span className="brand-sub">analysis platform</span>
        </div>
        <nav className="nav">
          <NavLink to="/" end>
            Dashboard
          </NavLink>
          <NavLink to="/standings">Standings</NavLink>
          <NavLink to="/matches">Matches</NavLink>
          <NavLink to="/teams">Teams</NavLink>
          <NavLink to="/analysis">Analysis</NavLink>
        </nav>
        <div className="controls">
          <select
            aria-label="League"
            value={league || ""}
            onChange={(e) => setLeague(e.target.value)}
            disabled={!leagues.length}
          >
            {!leagues.length && <option value="">Loading…</option>}
            {leagues.map((l) => (
              <option key={l.slug} value={l.slug}>
                {l.name} ({l.country})
              </option>
            ))}
          </select>
          <select
            aria-label="Season"
            value={season || ""}
            onChange={(e) => setSeason(e.target.value)}
            disabled={!seasons.length}
          >
            {seasons.length === 0 && <option value="">No seasons</option>}
            {seasons.map((s) => (
              <option key={s.season} value={s.season}>
                {s.season}
              </option>
            ))}
          </select>
        </div>
      </header>

      {error && <div className="banner error">{error}</div>}

      <main className="content">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/standings" element={<Standings />} />
          <Route path="/matches" element={<Matches />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/teams/:slug" element={<TeamDetail />} />
          <Route path="/analysis" element={<Analysis />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  );
}