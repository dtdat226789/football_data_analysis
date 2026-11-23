import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, ListSkeleton, Skeleton } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import ProjectionHighlights from "../components/ProjectionHighlights.jsx";
import Countdown from "../components/Countdown.jsx";
import { Badge, Card, CardHeader, PageHeader } from "../components/ui/index.js";
import { useFormatters } from "../i18n/useFormatters.js";
import { asArray, asRecord } from "../lib/shape.js";

const REGION_KEYS = {
  europe: "region.europe",
  asia: "region.asia",
  america: "region.america",
  other: "region.other",
};

/** Regions stay compact: the catalogue itself is one click away. */
const REGION_LIMIT = 5;

export function regionBuckets(byRegion) {
  const buckets = byRegion ?? {};
  const known = Object.keys(REGION_KEYS);
  const extra = Object.keys(buckets).filter((r) => !known.includes(r));
  return [...known, ...extra].map((region) => ({
    region,
    leagues: Array.isArray(buckets[region]) ? buckets[region] : [],
  }));
}

function KpiStrip({ meta, recent, upcoming, t, num }) {
  const items = [
    { label: t("page.dashboard.kpi.leagues"), value: num(meta?.n_leagues ?? 0) },
    { label: t("page.dashboard.kpi.withFixtures"), value: num(meta?.with_fixtures ?? 0) },
    { label: t("page.dashboard.kpi.recent"), value: num(recent.length) },
    { label: t("page.dashboard.kpi.upcoming"), value: num(meta?.n_upcoming ?? upcoming.length) },
  ];
  return (
    <div className="dashboard-kpis">
      {items.map((item) => (
        <div className="kpi" key={item.label}>
          <div className="label">{item.label}</div>
          <div className="value">{item.value}</div>
        </div>
      ))}
    </div>
  );
}

function RegionSection({ region, leagues, t }) {
  const label = t(REGION_KEYS[region] ?? "") || region;
  const more = leagues.length - REGION_LIMIT;
  return (
    <section className="region-group" aria-label={label}>
      <h4 className="region-head">
        {label} <Badge>{leagues.length}</Badge>
      </h4>
      <ul className="region-list">
        {leagues.slice(0, REGION_LIMIT).map((item) => (
          <li className="region-row" key={item.slug}>
            <Link className="region-link" to={`/leagues/${item.slug}`}>
              {item.name}
            </Link>
            <span className="region-count">{item.country || t("common.noData")}</span>
          </li>
        ))}
        {leagues.length === 0 && <li className="muted region-count">{t("common.noData")}</li>}
      </ul>
      {more > 0 && (
        <Link className="link region-more" to="/leagues">
          {t("page.dashboard.seeAllLeagues")} · {t("common.more", { n: more })}
        </Link>
      )}
    </section>
  );
}

export default function Dashboard() {
  const { t, num, kickoffDay, kickoffTime, plainDay } = useFormatters();
  const { data, loading, error } = useApi(() => api.dashboard(), []);

  if (loading)
    return (
      <div>
        <PageHeader title={t("page.dashboard.title")} />
        <div className="dashboard-kpis">
          {[0, 1, 2, 3].map((key) => (
            <Skeleton key={key} height={64} />
          ))}
        </div>
        <div className="two-col">
          <ListSkeleton items={4} />
          <ListSkeleton items={4} />
        </div>
      </div>
    );
  if (error) return <ErrorBox error={error} />;
  if (!data) return <ErrorBox error={t("page.dashboard.noData")} />;

  const payload = asRecord(data);
  const topLeagues = asArray(payload.top_leagues);
  const topClubs = asArray(payload.top_clubs);
  const recent = asArray(payload.recent_matches);
  const upcoming = asArray(payload.upcoming_matches);
  const byRegion = asRecord(payload.leagues_by_region);
  const meta = asRecord(payload.meta);

  return (
    <div>
      <PageHeader
        title={t("page.dashboard.title")}
        subtitle={t("page.dashboard.summary", {
          leagues: num(meta?.n_leagues),
          recent: num(recent.length),
          upcoming: num(upcoming.length),
        })}
      />

      <KpiStrip meta={meta} recent={recent} upcoming={upcoming} t={t} num={num} />

      <div className="dashboard-highlights">
        <Card>
          <CardHeader
            title={t("page.dashboard.topLeagues")}
            actions={<Badge>{t("page.dashboard.byMatches")}</Badge>}
          />
          <ol className="rank-list">
            {topLeagues.map((item, i) => (
              <li key={item.slug}>
                <Link className="rank-row" to={`/leagues/${item.slug}`}>
                  <span className="rank">{num(i + 1)}</span>
                  <span className="rank-main">
                    <span className="rank-name">{item.name}</span>
                    <span className="rank-meta">{item.country}</span>
                  </span>
                  <span className="rank-value">
                    {item.matches > 0
                      ? t("common.matches_other", { n: num(item.matches) })
                      : t("common.noData")}
                  </span>
                </Link>
              </li>
            ))}
          </ol>
        </Card>

        <Card>
          <CardHeader title={t("page.dashboard.topClubs")} />
          <ol className="rank-list">
            {topClubs.map((c, i) => (
              <li key={`${c.league}-${c.team}-${i}`}>
                <div className="rank-row">
                  <span className="rank">{num(i + 1)}</span>
                  <span className="rank-main">
                    <span className="rank-name">
                      <TeamLink name={c.team} />
                    </span>
                    <span className="rank-meta">
                      {c.league_name || c.league} · {c.season}
                    </span>
                  </span>
                  <span className="rank-value">
                    {num(c.points)} {t("common.pts")}
                  </span>
                </div>
              </li>
            ))}
          </ol>
          {topClubs.length === 0 && <p className="muted">{t("page.dashboard.noLeaders")}</p>}
        </Card>
      </div>

      <div className="two-col">
        <Card>
          <CardHeader
            title={t("page.dashboard.upcoming")}
            actions={
              <Link className="link" to="/matches">
                {t("page.dashboard.viewAll")}
              </Link>
            }
          />
          {upcoming.length === 0 ? (
            <p className="muted">{t("page.dashboard.noFixtures")}</p>
          ) : (
            <div className="event-list">
              {upcoming.map((m, i) => (
                <div key={`${m.slug || m.api_id || ""}-${i}`} className="event">
                  <div className="teams">
                    <span className="event-time">
                      {kickoffDay(m.match_date, m.time)} {kickoffTime(m.match_date, m.time)}
                      <Countdown date={m.match_date} time={m.time} />
                    </span>
                    <span>
                      <TeamLink name={m.home_team} /> {t("common.vs")} <TeamLink name={m.away_team} />
                    </span>
                  </div>
                  <div className="event-time">
                    {m.league_name || m.league} · {m.country}
                  </div>
                  <ProjectionHighlights
                    predictions={m.predictions}
                    compact
                    confidence={m.predictions?.confidence}
                    dataThrough={m.predictions?.data_through}
                  />
                </div>
              ))}
            </div>
          )}
        </Card>

        <Card>
          <CardHeader
            title={t("page.dashboard.recentResults")}
            actions={
              <Link className="link" to="/matches">
                {t("page.dashboard.viewAll")}
              </Link>
            }
          />
          {recent.length === 0 ? (
            <p className="muted">{t("page.dashboard.noResults")}</p>
          ) : (
            <div className="event-list">
              {recent.map((m) => (
                <div key={m.api_id} className="event">
                  <div className="teams">
                    <span className="event-time">
                      {plainDay(m.match_date)} · {m.league_name || m.league}
                    </span>
                    <span>
                      <TeamLink name={m.home_team} /> <strong>{m.home_score}–{m.away_score}</strong>{" "}
                      <TeamLink name={m.away_team} />{" "}
                      <Link className="link" to={`/match/${m.api_id}`}>
                        {t("common.view")}
                      </Link>
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </Card>
      </div>

      <Card>
        <CardHeader title={t("page.dashboard.byRegion")} />
        <div className="region-grid">
          {regionBuckets(byRegion).map(({ region, leagues }) => (
            <RegionSection key={region} region={region} leagues={leagues} t={t} />
          ))}
        </div>
      </Card>
    </div>
  );
}
