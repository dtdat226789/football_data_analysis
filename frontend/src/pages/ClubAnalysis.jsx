import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { Empty, ErrorBox, Skeleton } from "../components/State.jsx";
import { FilterSelects, KpiTile, LineTrend, RankTable } from "../components/DashboardWidgets.jsx";
import { TableShell } from "../components/ui/index.js";
import { enumParam, useParamsPatch } from "../lib/searchParams.js";
import { asArray, asRecord } from "../lib/shape.js";
import { useFormatters } from "../i18n/useFormatters.js";

const RANKING_COLUMNS = [
  { key: "label", labelKey: "kpi.table.team" },
  { key: "rating", labelKey: "kpi.rating", numeric: true },
  { key: "played", labelKey: "table.p", numeric: true },
  { key: "goals", labelKey: "kpi.table.goals", numeric: true },
  { key: "goals_per_game", labelKey: "kpi.goalsPerGame", numeric: true },
];

export default function ClubAnalysis() {
  const [params, patch] = useParamsPatch();
  const { t } = useFormatters();
  const rawLeague = params.get("league") || "premier";
  const season = params.get("season") || "";
  const team = params.get("team") || "";

  const leagues = useApi(() => api.listLeagues(), []);
  const leagueSlugs = asArray(leagues.data)
    .map((item) => item?.slug)
    .filter((value) => typeof value === "string");
  const league = leagueSlugs.length
    ? enumParam(params, "league", leagueSlugs, "premier")
    : rawLeague;
  const { data, loading, error } = useApi(
    () => api.clubAnalysis({ league, season, team }),
    [league, season, team],
  );
  const seasons = asArray(asRecord(data).seasons);
  const teams = asArray(asRecord(data).teams);
  const kpis = asArray(asRecord(data).kpis);
  const ranking = asArray(asRecord(data).ranking);
  const timeline = asArray(asRecord(data).timeline);

  const fields = [
    {
      key: "league",
      labelKey: "common.league",
      value: league,
      options: leagueSlugs.map((value, i) => ({ value, label: asArray(leagues.data)[i]?.name || value })),
      onChange: (value) => patch({ league: value, season: "", team: "" }),
    },
    {
      key: "season",
      labelKey: "common.season",
      value: season,
      options: [
        { value: "", label: t("dash.latestComplete") },
        ...seasons.map((item) => ({ value: item.season, label: item.season })),
      ],
      onChange: (value) => patch({ season: value, team: "" }),
    },
    {
      key: "team",
      labelKey: "kpi.table.team",
      value: team,
      options: [
        { value: "", label: t("dash.autoTeam") },
        ...teams.map((item) => ({ value: item.slug, label: item.name })),
      ],
      onChange: (value) => patch({ team: value }),
    },
  ];

  return (
    <div className="dash-scope club-theme">
      <div className="dash-head">
        <div>
          <h2>{t("dash.clubTitle")}</h2>
          <p>{t("dash.clubSummary", { league: data?.league_name || league, season: data?.season || season })}</p>
        </div>
        <span className="dash-badge">{t("dash.clubBadge")}</span>
      </div>

      <FilterSelects fields={fields} />
      {loading && (
        <div className="dash-panels">
          <Skeleton height={110} />
          <Skeleton height={240} />
        </div>
      )}
      {error && <ErrorBox error={error} />}
      {!loading && !error && !data && <Empty>{t("dash.noData")}</Empty>}

      {data && (
        <>
          <div className="dash-kpi-grid">
            {kpis.map((tile) => (
              <KpiTile tile={tile} key={tile.key} />
            ))}
          </div>

          <div className="dash-panels dash-panels-split">
            <section className="dash-panel">
              <h3>{t("dash.trendTitle")}</h3>
              <LineTrend data={timeline} label={t("kpi.goalsPerGame")} />
            </section>
            <section className="dash-panel">
              <h3>{t("dash.rankingTitle")}</h3>
              {ranking.length === 0 ? (
                <p className="dash-empty">{t("dash.noData")}</p>
              ) : (
                <TableShell className="dash-table-wrap" label={t("dash.rankingTitle")}>
                  <RankTable rows={ranking} columns={RANKING_COLUMNS} />
                </TableShell>
              )}
            </section>
          </div>

          {data.team?.slug && (
            <Link className="dash-back" to={`/teams/${data.team.slug}/kpi?league=${league}&season=${data.season}`}>
              {t("dash.viewTeamKpi", { team: data.team.name || data.team.slug })} →
            </Link>
          )}
          <p className="dash-note">{t("dash.proxyNote")}</p>
          <p className="dash-note">{t("dash.ratingNote")}</p>
          <p className="dash-attribution">{data.attribution}</p>
        </>
      )}
    </div>
  );
}
