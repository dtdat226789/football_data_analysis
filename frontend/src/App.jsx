import { useState } from "react";
import { NavLink, Navigate, Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard.jsx";
import Leagues from "./pages/Leagues.jsx";
import LeagueDetail from "./pages/LeagueDetail.jsx";
import Matches from "./pages/Matches.jsx";
import Teams from "./pages/Teams.jsx";
import TeamDetail from "./pages/TeamDetail.jsx";
import MatchDetail from "./pages/MatchDetail.jsx";
import FixtureDetail from "./pages/FixtureDetail.jsx";
import TeamKpi from "./pages/TeamKpi.jsx";
import ClubAnalysis from "./pages/ClubAnalysis.jsx";
import SettingsControls from "./i18n/SettingsControls.jsx";
import { useI18n } from "./i18n/I18nProvider.jsx";

export default function App() {
  const { t } = useI18n();
  const [navOpen, setNavOpen] = useState(false);

  return (
    <div className="app">
      <a className="skip-link" href="#main-content">
        {t("app.skipToContent")}
      </a>

      <header className="topbar">
        <div className="topbar-brand">
          <div className="brand">
            <span className="brand-dot" />
            <h1>{t("app.brand")}</h1>
            <span className="brand-sub">{t("app.tagline")}</span>
          </div>
        </div>

        <nav
          id="primary-navigation"
          className={`topbar-nav${navOpen ? " is-open" : ""}`}
          aria-label={t("app.nav.label")}
          onClick={() => setNavOpen(false)}
        >
          <div className="nav">
            <div className="nav-group" role="group" aria-label={t("app.nav.group.main")}>
              <NavLink to="/" end>
                {t("app.nav.dashboard")}
              </NavLink>
              <NavLink to="/matches">{t("app.nav.matches")}</NavLink>
            </div>
            <span className="nav-divider" aria-hidden="true" />
            <div className="nav-group" role="group" aria-label={t("app.nav.group.browse")}>
              <NavLink to="/leagues">{t("app.nav.leagues")}</NavLink>
              <NavLink to="/teams">{t("app.nav.teams")}</NavLink>
              <NavLink to="/club-analysis">{t("app.nav.clubAnalysis")}</NavLink>
            </div>
          </div>
        </nav>

        <div className="topbar-settings">
          <SettingsControls />
        </div>

        <button
          type="button"
          className="nav-toggle"
          aria-label={navOpen ? t("app.nav.close") : t("app.nav.open")}
          aria-expanded={navOpen}
          aria-controls="primary-navigation"
          onClick={() => setNavOpen((open) => !open)}
        >
          <span className="nav-toggle-icon" aria-hidden="true" />
        </button>
      </header>

      <main className="content" id="main-content" tabIndex={-1}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/leagues" element={<Leagues />} />
          <Route path="/leagues/:slug" element={<LeagueDetail />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/teams/:slug" element={<TeamDetail />} />
          <Route path="/teams/:slug/kpi" element={<TeamKpi />} />
          <Route path="/matches" element={<Matches />} />
          <Route path="/match/:id" element={<MatchDetail />} />
          {/* Splat route: the trailing fixture id is the `date-home-vs-away`
              segment of the upstream slug. */}
          <Route path="/fixture/:league/*" element={<FixtureDetail />} />
          <Route path="/club-analysis" element={<ClubAnalysis />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  );
}
