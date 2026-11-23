import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { Empty, ErrorBox, Skeleton } from "../components/State.jsx";
import { FilterSelects, KpiTile, MiniCompare, RankTable } from "../components/DashboardWidgets.jsx";
import { TableShell } from "../components/ui/index.js";
import { enumParam, useParamsPatch } from "../lib/searchParams.js";
import { asArray, asRecord } from "../lib/shape.js";
import { safeImageUrl } from "../lib/safeUrl.js";
import { useFormatters } from "../i18n/useFormatters.js";

const N_OPTIONS = [5, 10, 20];

const TABLE_COLUMNS = [
  { key: "position", labelKey: "table.pos", numeric: true },
  { key: "label", labelKey: "kpi.table.team" },
  { key: "rating", labelKey: "kpi.rating", numeric: true },
  { key: "points", labelKey: "table.pts", numeric: true },
  { key: "expected_points", labelKey: "kpi.table.xpts", numeric: true },
];

export default function TeamKpi() {
  const { slug } = useParams();
  const [params, patch] = useParamsPatch();
  const { t, plainDay } = useFormatters();
  const rawLeague = params.get("league") || "premier";
  const season = params.get("season") || "";
  const n = Number(enumParam(params, "n", N_OPTIONS.map(String), "5"));

  const leagues = useApi(() => api.listLeagues(), []);
  const leagueSlugs = asArray(leagues.data)
    .map((item) => item?.slug)
    .filter((value) => typeof value === "string");
  const league = leagueSlugs.length
    ? enumParam(params, "league", leagueSlugs, "premier")
    : rawLeague;
  const seasons = useApi(() => api.leagueSeasons(league), [league]);
  const { data, loading, error } = useApi(
    () => api.teamKpi(slug, { league, season, n }),
    [slug, league, season, n],
  );
  const lastMatches = asArray(asRecord(data).last_matches);
  const groups = asArray(asRecord(data).groups);
  const table = asArray(asRecord(data).table);
  const logo = safeImageUrl(asRecord(data).logo_url);

  const leagueFields = [
    {
      key: "league",
      labelKey: "common.league",
      value: league,
      options: leagueSlugs.map((value, i) => ({ value, label: asArray(leagues.data)[i]?.name || value })),
      onChange: (value) => patch({ league: value, season: "" }),
    },
    {
      key: "season",
      labelKey: "common.season",
      value: season,
      options: [
        { value: "", label: t("dash.latestComplete") },
        ...(seasons.data?.seasons || [])
          .filter((item) => item.matches > 0)
          .map((item) => ({ value: item.season, label: item.season })),
      ],
      onChange: (value) => patch({ season: value }),
    },
    {
      key: "n",
      labelKey: "dash.gamesCount",
      value: n,
      options: N_OPTIONS.map((value) => ({ value, label: String(value) })),
      onChange: (value) => patch({ n: value }),
    },
  ];

  return (
    <div className="dash-scope kpi-theme">
      <Link className="dash-back" to={`/teams/${slug}`}>
        ← {t("dash.backTeam")}
      </Link>
      <div className="dash-head">
        <div>
          <h2>
            {data?.team_name || slug}
            {logo && <img src={logo} alt="" className="dash-logo" decoding="async" width={40} height={40} />}
          </h2>
          <p>{t("dash.kpiSummary", { league: data?.league_name || league, season: data?.season || season })}</p>
        </div>
        <span className="dash-badge">{t("dash.kpiBadge")}</span>
      </div>

      <FilterSelects fields={leagueFields} />
      {loading && (
        <div className="dash-panels">
          <Skeleton height={120} />
          <Skeleton height={260} />
        </div>
      )}
      {error && <ErrorBox error={error} />}
      {!loading && !error && !data && <Empty>{t("dash.noData")}</Empty>}

      {data && (
        <>
          <div className="dash-panels dash-panels-split">
            <section className="dash-panel">
              <h3>{t("dash.lastGames", { n: data.n })}</h3>
              {lastMatches.length === 0 ? (
                <p className="dash-empty">{t("dash.noMatches")}</p>
              ) : (
                <ul className="dash-match-list">
                  {lastMatches.map((game, i) => (
                    <li key={`${game.date}-${i}`}>
                      <span className="dash-match-date">{plainDay(game.date)}</span>
                      <span className="dash-match-opponent">
                        {game.venue === "home" ? t("common.home") : t("common.away")} · {game.opponent}
                      </span>
                      <span className="dash-match-score">{game.score}</span>
                      <span className={`dash-result result-${game.result}`}>{game.result}</span>
                    </li>
                  ))}
                </ul>
              )}
            </section>
            <MiniCompare games={lastMatches} metric="goals_for" titleKey="dash.goalsFor" />
            <MiniCompare games={lastMatches} metric="goals_against" titleKey="dash.goalsAgainst" />
          </div>

          {groups.map((group) => (
            <section className="dash-panel dash-group" key={group.key}>
              <h3>{t(`kpi.group.${group.key}`)}</h3>
              <div className="dash-tile-grid">
                {asArray(group.tiles).map((tile) => (
                  <KpiTile tile={tile} key={tile.key} />
                ))}
              </div>
            </section>
          ))}

          <section className="dash-panel">
            <h3>{t("dash.leagueTable")}</h3>
            {table.length === 0 ? (
              <p className="dash-empty">{t("dash.noData")}</p>
            ) : (
              <TableShell className="dash-table-wrap" label={t("dash.rankingTitle")}>
                <RankTable rows={table} columns={TABLE_COLUMNS} />
              </TableShell>
            )}
            <p className="dash-note">{t("dash.proxyNote")}</p>
            <p className="dash-note">{t("dash.ratingNote")}</p>
          </section>
          <p className="dash-attribution">{data.attribution}</p>
        </>
      )}
    </div>
  );
}
