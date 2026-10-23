import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Skeleton } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import DataTree from "../components/DataTree.jsx";
import MatchInsights from "../components/MatchInsights.jsx";
import { useFormatters } from "../i18n/useFormatters.js";

export default function MatchDetail() {
  const { t, kickoffDay, kickoffTime, plainDay } = useFormatters();
  const { id } = useParams();
  const { data, loading, error } = useApi(() => api.match(id), [id]);
  // Insights are supplementary: if the artifact or endpoint is unavailable the
  // match page must still render, so this fetch fails soft.
  const { data: insights } = useApi(() => api.matchInsights(id), [id]);

  if (loading)
    return (
      <div>
        <Skeleton height={46} width="55%" style={{ maxWidth: 640 }} />
        <Skeleton width="35%" height={14} />
        <div className="two-col">
          <Skeleton height={140} />
          <Skeleton height={140} />
        </div>
      </div>
    );
  if (error) return <ErrorBox error={error} />;
  if (!data) return <ErrorBox error={t("page.match.noData")} />;

  const home = data.home_team;
  const away = data.away_team;
  const played = typeof data.home_score === "number" && typeof data.away_score === "number";

  return (
    <div>
      <div className="page-head">
        <h2>
          <TeamLink name={home} /> {played ? `${data.home_score} – ${data.away_score}` : t("common.vs")} <TeamLink name={away} />
        </h2>
        <p>
          {played
            ? plainDay(data.match_date)
            : `${kickoffDay(data.match_date, data.kickoff_time)} ${kickoffTime(data.match_date, data.kickoff_time)}`}
          {played ? ` · ${t("page.match.fullTime")}` : ""}
        </p>
      </div>

      <div className="two-col">
        <section className="card">
          <h3 style={{ marginTop: 0 }}>{t("page.match.facts")}</h3>
          <table className="data">
            <tbody>
              <tr>
                <th>{t("common.league")}</th>
                <td>
                  <Link className="link" to={`/leagues/${data.league}`}>
                    {data.league_name || data.league}
                  </Link>
                </td>
              </tr>
              <tr>
                <th>{t("page.match.season")}</th>
                <td>{data.season}</td>
              </tr>
              <tr>
                <th>{t("page.match.matchday")}</th>
                <td>{data.game_index}</td>
              </tr>
              <tr>
                <th>{t("page.match.halfTime")}</th>
                <td>
                  {typeof data.home_ht === "number" && typeof data.away_ht === "number"
                    ? `${data.home_ht} – ${data.away_ht}`
                    : "—"}
                </td>
              </tr>
              <tr>
                <th>{t("page.match.firstGoal")}</th>
                <td>
                  {data.first_goal_time != null
                    ? `${data.first_goal_time}${data.first_goal_time_extra ? `' +${data.first_goal_time_extra}` : "'"}`
                    : "—"}
                </td>
              </tr>
              <tr>
                <th>{t("page.match.apiId")}</th>
                <td>{data.api_id}</td>
              </tr>
            </tbody>
          </table>
        </section>

        <section className="card">
          <h3 style={{ marginTop: 0 }}>{t("page.match.teams")}</h3>
          <div className="event-list" style={{ marginTop: 10 }}>
            <div className="event">
              <div className="teams">
                <span>
                  <TeamLink name={home} /> <span className="muted">{t("page.match.home")}</span>
                </span>
              </div>
            </div>
            <div className="event">
              <div className="teams">
                <span>
                  <TeamLink name={away} /> <span className="muted">{t("page.match.away")}</span>
                </span>
              </div>
            </div>
          </div>
        </section>
      </div>

      <MatchInsights insights={insights} homeName={home} awayName={away} />

      <section className="card" style={{ marginTop: 16 }}>
        <h3 style={{ marginTop: 0 }}>{t("page.match.raw")}</h3>
        <DataTree value={data} />
      </section>
    </div>
  );
}