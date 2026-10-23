import { NavLink, Navigate, Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard.jsx";
import Leagues from "./pages/Leagues.jsx";
import LeagueDetail from "./pages/LeagueDetail.jsx";
import Matches from "./pages/Matches.jsx";
import Teams from "./pages/Teams.jsx";
import TeamDetail from "./pages/TeamDetail.jsx";
import MatchDetail from "./pages/MatchDetail.jsx";
import FixtureDetail from "./pages/FixtureDetail.jsx";
import SettingsControls from "./i18n/SettingsControls.jsx";
import { useI18n } from "./i18n/I18nProvider.jsx";

export default function App() {
  const { t } = useI18n();

  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <span className="brand-dot" />
          <h1>{t("app.brand")}</h1>
          <span className="brand-sub">{t("app.tagline")}</span>
        </div>
        <nav className="nav">
          <NavLink to="/" end>
            {t("app.nav.dashboard")}
          </NavLink>
          <NavLink to="/leagues">{t("app.nav.leagues")}</NavLink>
          <NavLink to="/teams">{t("app.nav.teams")}</NavLink>
          <NavLink to="/matches">{t("app.nav.matches")}</NavLink>
        </nav>
        <SettingsControls />
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
          {/* Splat route: the trailing fixture id is the `date-home-vs-away`
              segment of the upstream slug. */}
          <Route path="/fixture/:league/*" element={<FixtureDetail />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  );
}