import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, ListSkeleton, Skeleton } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import PredictionChips from "../components/PredictionChips.jsx";
import { useFormatters } from "../i18n/useFormatters.js";

const REGION_KEYS = {
  europe: "region.europe",
  asia: "region.asia",
  america: "region.america",
  other: "region.other",
};

export function regionBuckets(byRegion) {
  const buckets = byRegion ?? {};
  const known = Object.keys(REGION_KEYS);
  const extra = Object.keys(buckets).filter((r) => !known.includes(r));
  return [...known, ...extra].map((region) => ({
    region,
    leagues: Array.isArray(buckets[region]) ? buckets[region] : [],
  }));
}

function LeagueCard({ item, t, num }) {
  return (
    <Link to={`/leagues/${item.slug}`} className="card league-card" style={{ textDecoration: "none" }}>
      <div className="league-card-name">{item.name}</div>
      <div className="muted" style={{ fontSize: 13 }}>
        {item.country}
      </div>
      <div className="muted" style={{ fontSize: 12, marginTop: 6 }}>
        {item.matches > 0 ? t("common.matches_other", { n: num(item.matches) }) : t("common.noData")}
      </div>
    </Link>
  );
}

function RegionSection({ region, leagues, t }) {
  return (
    <section>
      <h3>
        {t(REGION_KEYS[region] ?? "") || region}
        <span className="badge">{leagues.length}</span>
      </h3>
      <div className="mini-grid">
        {leagues.slice(0, 8).map((item) => (
          <Link key={item.slug} to={`/leagues/${item.slug}`} className="card mini" style={{ textDecoration: "none" }}>
            <div className="mini-name">{item.name}</div>
            <div className="muted" style={{ fontSize: 12 }}>
              {item.country} · {item.matches > 0 ? `${item.matches} m` : t("common.noData")}
            </div>
          </Link>
        ))}
        {leagues.length > 8 && (
          <div className="muted" style={{ alignSelf: "center" }}>
            {t("common.more", { n: leagues.length - 8 })}
          </div>
        )}
      </div>
    </section>
  );
}

export default function Dashboard() {
  const { t, num, kickoffDay, kickoffTime, plainDay } = useFormatters();
  const { data, loading, error } = useApi(() => api.dashboard(), []);

  if (loading)
    return (
      <div>
        <div className="page-head">
          <Skeleton height={34} width="30%" />
          <Skeleton height={14} width="55%" />
        </div>
        <Skeleton height={120} />
        <div className="two-col" style={{ marginTop: 16 }}>
          <ListSkeleton items={4} />
          <ListSkeleton items={4} />
        </div>
      </div>
    );
  if (error) return <ErrorBox error={error} />;
  if (!data) return <ErrorBox error={t("page.dashboard.noData")} />;

  const {
    top_leagues: topLeagues = [],
    top_clubs: topClubs = [],
    recent_matches: recent = [],
    upcoming_matches: upcoming = [],
    leagues_by_region: byRegion,
  } = data;

  return (
    <div>
      <div className="page-head">
        <h2>{t("page.dashboard.title")}</h2>
        <p>
          {t("page.dashboard.summary", {
            leagues: num(data.meta?.n_leagues),
            recent: num(recent.length),
            upcoming: num(upcoming.length),
          })}
        </p>
      </div>

      <section>
        <h3>
          {t("page.dashboard.topLeagues")} <span className="badge">{t("page.dashboard.byMatches")}</span>
        </h3>
        <div className="mini-grid">
          {topLeagues.map((item) => (
            <LeagueCard key={item.slug} item={item} t={t} num={num} />
          ))}
        </div>
      </section>

      <div className="two-col">
        <section className="card">
          <h3 style={{ marginTop: 0 }}>{t("page.dashboard.upcomingTopPicks")}</h3>
          <Link className="link" to="/matches" style={{ fontSize: 13 }}>
            {t("page.dashboard.viewAll")}
          </Link>
          {upcoming.length === 0 ? (
            <p className="muted">{t("page.dashboard.noFixtures")}</p>
          ) : (
            <div className="event-list" style={{ marginTop: 10 }}>
              {upcoming.map((m, i) => (
                <div key={i} className="event">
                  <div className="teams">
                    <span className="muted" style={{ fontSize: 12 }}>
                      {kickoffDay(m.match_date, m.time)} {kickoffTime(m.match_date, m.time)}
                    </span>
                    <span>
                      <TeamLink name={m.home_team} /> {t("common.vs")} <TeamLink name={m.away_team} />
                    </span>
                  </div>
                  <div className="muted" style={{ fontSize: 12 }}>
                    {m.league_name || m.league} · {m.country}
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
          <h3 style={{ marginTop: 0 }}>{t("page.dashboard.recentResults")}</h3>
          <Link className="link" to="/matches" style={{ fontSize: 13 }}>
            {t("page.dashboard.viewAll")}
          </Link>
          {recent.length === 0 ? (
            <p className="muted">{t("page.dashboard.noResults")}</p>
          ) : (
            <div className="event-list" style={{ marginTop: 10 }}>
              {recent.map((m) => (
                <div key={m.api_id} className="event">
                  <div className="teams">
                    <span className="muted" style={{ fontSize: 12 }}>
                      {plainDay(m.match_date)} · {m.league_name || m.league}
                    </span>
                    <span>
                      <TeamLink name={m.home_team} /> <strong>{m.home_score}–{m.away_score}</strong>{" "}
                      <TeamLink name={m.away_team} />{" "}
                      <Link className="link" to={`/match/${m.api_id}`} style={{ fontSize: 12 }}>
                        {t("common.view")}
                      </Link>
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        <section className="card">
          <h3 style={{ marginTop: 0 }}>{t("page.dashboard.topClubs")}</h3>
          {topClubs.length === 0 ? (
            <p className="muted">{t("page.dashboard.noLeaders")}</p>
          ) : (
            <div className="event-list" style={{ marginTop: 10 }}>
              {topClubs.map((c, i) => (
                <div key={i} className="event">
                  <div className="teams">
                    <span>
                      <TeamLink name={c.team} /> <span className="muted">· {c.league_name}</span>
                    </span>
                  </div>
                  <div className="score">
                    {num(c.points)} {t("common.pts")} · #{num(c.position)} · {c.season}
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>
      </div>

      <section>
        <h3>{t("page.dashboard.byRegion")}</h3>
        <div className="grid regions">
          {regionBuckets(byRegion).map(({ region, leagues }) => (
            <RegionSection key={region} region={region} leagues={leagues} t={t} />
          ))}
        </div>
      </section>
    </div>
  );
}