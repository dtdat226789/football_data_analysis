import { useParams } from "react-router-dom";
import { useLeagues } from "../state/LeaguesContext.jsx";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Loading } from "../components/State.jsx";
import { FormPills } from "../components/FormPills.jsx";
import { TeamLink } from "../components/TeamLink.jsx";

export default function TeamDetail() {
  const { slug } = useParams();
  const { league, season } = useLeagues();

  const detail = useApi(() => api.team(slug), [slug]);
  const form = useApi(
    () => (league && season ? api.teamForm(slug, { league, season, n: 8 }) : null),
    [slug, league, season],
  );
  const standing = useApi(
    () => (league && season ? api.teamStandings(slug, { league, season }) : null),
    [slug, league, season],
  );
  const matches = useApi(
    () =>
      league && season ? api.teamMatches(slug, { league, season, limit: 10, offset: 0 }) : null,
    [slug, league, season],
  );

  if (detail.loading) return <Loading label="Loading team…" />;
  if (detail.error) return <ErrorBox error={detail.error} />;

  const team = detail.data?.team;
  const memberships = detail.data?.memberships || [];
  const recent = memberships.filter((m) => m.league === league && m.season === season);
  const apiName = recent[0]?.api_name || team?.canonical_name || slug;

  return (
    <div>
      <div className="page-head">
        <h2>
          {apiName}
          {recent[0]?.logo_url && (
            <img
              src={recent[0].logo_url}
              alt=""
              style={{ height: 28, marginLeft: 10, verticalAlign: "middle" }}
            />
          )}
        </h2>
        <p>
          <span className="muted">canonical:</span> {team?.canonical_name} ·{" "}
          <span className="muted">slug:</span> {team?.canonical_slug}
        </p>
      </div>

      <div className="two-col">
        {standing.data && (
          <section className="card">
            <h3 style={{ marginTop: 0 }}>
              Standings · {league} {season}
            </h3>
            {standing.data.row ? (
              <table className="data">
                <tbody>
                  <tr>
                    <th>Pos</th>
                    <td>{standing.data.row.position}</td>
                  </tr>
                  <tr>
                    <th>Record</th>
                    <td>
                      {standing.data.row.won}W-{standing.data.row.drawn}D-
                      {standing.data.row.lost}L
                    </td>
                  </tr>
                  <tr>
                    <th>Goals</th>
                    <td>
                      {standing.data.row.goals_for} : {standing.data.row.goals_against} (
                      {standing.data.row.goal_difference >= 0 ? "+" : ""}
                      {standing.data.row.goal_difference})
                    </td>
                  </tr>
                  <tr>
                    <th>Points</th>
                    <td>
                      <strong>{standing.data.row.points}</strong>
                    </td>
                  </tr>
                </tbody>
              </table>
            ) : (
              <p className="muted">Not in this season's table.</p>
            )}
          </section>
        )}

        {form.data && (
          <section className="card">
            <h3 style={{ marginTop: 0 }}>Recent form</h3>
            <FormPills results={form.data.results} />
            <div className="event-list" style={{ marginTop: 12 }}>
              {form.data.results.map((r, i) => (
                <div key={i} className="event">
                  <div className="teams">
                    <span className="muted" style={{ fontSize: 12 }}>
                      {r.date}
                    </span>
                    <span>
                      <TeamLink name={r.home_team} /> vs <TeamLink name={r.away_team} />
                    </span>
                  </div>
                  <div className="score muted">
                    {r.home_score} – {r.away_score}{" "}
                    <span className={`pill ${r.team_result}`}>{r.team_result}</span>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}
      </div>

      {matches.data && (
        <section className="card" style={{ marginTop: 16 }}>
          <h3 style={{ marginTop: 0 }}>Recent matches ({matches.data.total})</h3>
          <table className="data">
            <thead>
              <tr>
                <th>Date</th>
                <th>Home</th>
                <th className="num">Score</th>
                <th>Away</th>
              </tr>
            </thead>
            <tbody>
              {matches.data.matches.map((m) => (
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
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}

      {memberships.length > 0 && (
        <section className="card" style={{ marginTop: 16 }}>
          <h3 style={{ marginTop: 0 }}>Memberships ({memberships.length})</h3>
          <table className="data">
            <thead>
              <tr>
                <th>League</th>
                <th>Season</th>
                <th>API name</th>
                <th>Slug</th>
              </tr>
            </thead>
            <tbody>
              {memberships.map((m, i) => (
                <tr key={i}>
                  <td>
                    {m.league} · {m.league_name}
                  </td>
                  <td>{m.season}</td>
                  <td>{m.api_name}</td>
                  <td className="muted">{m.api_slug}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}
    </div>
  );
}