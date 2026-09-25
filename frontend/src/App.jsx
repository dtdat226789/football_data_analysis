import { NavLink, Navigate, Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard.jsx";
import Leagues from "./pages/Leagues.jsx";
import LeagueDetail from "./pages/LeagueDetail.jsx";
import Matches from "./pages/Matches.jsx";
import Teams from "./pages/Teams.jsx";
import TeamDetail from "./pages/TeamDetail.jsx";
import MatchDetail from "./pages/MatchDetail.jsx";

export default function App() {
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
          <NavLink to="/leagues">Leagues</NavLink>
          <NavLink to="/teams">Teams</NavLink>
          <NavLink to="/matches">Matches</NavLink>
        </nav>
      </header>

      <main className="content">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/leagues" element={<Leagues />} />
          <Route path="/leagues/:slug" element={<LeagueDetail />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/teams/:slug" element={<TeamDetail />} />
          <Route path="/matches" element={<Matches />} />
          <Route path="/match/:id" element={<MatchDetail />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  );
}