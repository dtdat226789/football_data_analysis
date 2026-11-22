import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Skeleton } from "../components/State.jsx";
import { FormPills } from "../components/FormPills.jsx";
import MatchInsights from "../components/MatchInsights.jsx";
import MatchOutlook from "../components/MatchOutlook.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import { BackLink, Badge, Card, CardHeader, PageHeader, TableShell } from "../components/ui/index.js";
import { useFormatters } from "../i18n/useFormatters.js";
import { safeHttpsUrl, safeImageUrl } from "../lib/safeUrl.js";

/**
 * The model's full read on an unplayed fixture: goal totals, expected goals,
 * and the gates/ratings/sample-size metadata that says how much to trust the
 * number.
 */
function PredictabilityPanel({ prediction }) {
  const { t, dec } = useFormatters();
  if (!prediction) return null;
  const goals = prediction.expected_goals || {};
  const ratings = prediction.ratings || {};
  const effective = prediction.effective_matches || {};
  const status = prediction.data_status || {};
  const gates = prediction.gates || {};

  return (
    <Card>
      <CardHeader
        title={t("predictability.title")}
        actions={
          <>
            <Badge>{prediction.model || "—"}</Badge>
            {status.stale && <Badge tone="amber">{t("predictability.stale")}</Badge>}
          </>
        }
      />

      <MatchOutlook
        predictions={prediction.summary}
        confidence={prediction.summary?.confidence}
        dataThrough={prediction.data_through}
      />

      <TableShell>
        <table className="data">
          <tbody>
            <tr>
              <th scope="row">{t("predictability.expectedGoals")}</th>
              <td>
                {dec(goals.home, 2)} – {dec(goals.away, 2)}
                <span className="detail-inline-note">
                  {t("predictability.htTotal")} {dec(goals.half_time_total, 2)}
                </span>
              </td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.ratings")}</th>
              <td>
                {["home", "away"].map((side) => (
                  <span key={side} className="detail-inline-item">
                    {side} {t("predictability.attackShort")} {dec(ratings[side]?.attack, 2)} / {t("predictability.defenceShort")} {dec(ratings[side]?.defence, 2)}
                  </span>
                ))}
              </td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.sampleSize")}</th>
              <td>
                {["home", "away"].map((side) => (
                  <span key={side} className="detail-inline-item">
                    {side} {dec(effective[side], 1)}
                  </span>
                ))}
                <span className="muted">{t("predictability.effectiveMatches")}</span>
              </td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.drawInflation")}</th>
              <td>
                {dec(prediction.xi, 4)}
                <span className="detail-inline-note">
                  {t("predictability.sigma")} {dec(prediction.sigma, 1)}
                </span>
              </td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.gates")}</th>
              <td>
                {Object.entries(gates).length
                  ? Object.entries(gates)
                      .map(([name, passed]) => `${name}: ${passed ? t("predictability.pass") : t("predictability.fail")}`)
                      .join(" · ")
                  : "—"}
              </td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.dataThrough")}</th>
              <td>
                {prediction.data_through || "—"}
                <span className="detail-inline-note">
                  {status.matches_behind ? t("predictability.matchesBehind", { n: status.matches_behind }) : ""}
                </span>
              </td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.computed")}</th>
              <td className="muted">{prediction.computed_at || "—"}</td>
            </tr>
          </tbody>
        </table>
      </TableShell>
    </Card>
  );
}

/** One side: crest, name, recent form, and the split that venue implies. */
function TeamCard({ side, team, standings }) {
  const { t, pct, dec } = useFormatters();
  if (!team) return null;
  const logo = safeImageUrl(team.logo);
  const venue = team.venue;
  return (
    <Card>
      <CardHeader
        title={
          <span className="detail-team-heading">
            {logo ? (
              <img className="team-crest" src={logo} alt="" width={22} height={22} decoding="async" />
            ) : null}
            <TeamLink name={team.name} />
            <span className="detail-team-side">
              {t(side === "home" ? "page.team.venue.home" : "page.team.venue.away")}
            </span>
          </span>
        }
      />

      <div className="detail-form">
        <span className="detail-subtle detail-block">
          {t("predictability.form", { n: team.form?.length || 0 })}
        </span>
        <FormPills results={team.form} />
      </div>

      <TableShell>
        <table className="data">
          <tbody>
            <tr>
              <th scope="row">{t("predictability.venueSplit")}</th>
              <td>
                {venue ? (
                  <>
                    {venue.wins}W {venue.draws}D {venue.losses}L · {t("predictability.winRate")}{" "}
                    {pct(venue.win_rate)} · {dec(venue.goals_avg, 1)} {t("predictability.scored")},{" "}
                    {dec(venue.conceded_avg, 1)} {t("predictability.conceded")}
                  </>
                ) : (
                  "—"
                )}
              </td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.rest")}</th>
              <td>{team.rest_days != null ? t("predictability.restDays", { n: team.rest_days }) : "—"}</td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.played")}</th>
              <td>{team.games_before ?? "—"}</td>
            </tr>
            <tr>
              <th scope="row">{t("predictability.table")}</th>
              <td>
                {standings ? (
                  t("predictability.tableLine", {
                    position: standings.position,
                    points: standings.points,
                    gd: `${standings.goal_difference > 0 ? "+" : ""}${standings.goal_difference}`,
                    played: standings.played,
                  })
                ) : (
                  "—"
                )}
              </td>
            </tr>
          </tbody>
        </table>
      </TableShell>
    </Card>
  );
}

export default function FixtureDetail() {
  const { t, kickoffDay, kickoffTime, instantTime, instantHeading } = useFormatters();
  const { league, "*": matchId } = useParams();
  const { data, loading, error } = useApi(
    () => (league && matchId ? api.fixtureDetail(league, matchId) : null),
    [league, matchId],
  );

  if (loading)
    return (
      <div>
        <div className="page-head">
          <div className="page-heading">
            <Skeleton className="detail-heading-skeleton" height={46} width="55%" />
            <Skeleton width="35%" height={14} />
          </div>
        </div>
        <div className="two-col">
          <Skeleton height={200} />
          <Skeleton height={200} />
        </div>
      </div>
    );
  if (error) return <ErrorBox error={error} />;
  if (!data) return <ErrorBox error={t("page.fixture.noData")} />;

  const home = data.teams?.home;
  const away = data.teams?.away;
  const portalLink = safeHttpsUrl(data.kickoff?.portal_link);
  const homeLogo = safeImageUrl(home?.logo);
  const awayLogo = safeImageUrl(away?.logo);

  return (
    <div>
      <BackLink to={`/leagues/${data.league || league}?tab=matches&season=${data.season || ""}`}>
        {t("page.fixture.back")}
      </BackLink>
      <PageHeader
        title={
          <>
            {homeLogo ? (
              <img className="team-crest" src={homeLogo} alt="" width={24} height={24} decoding="async" />
            ) : null}{" "}
            <TeamLink name={home?.name} /> {t("common.vs")} <TeamLink name={away?.name} />{" "}
            {awayLogo ? (
              <img className="team-crest" src={awayLogo} alt="" width={24} height={24} decoding="async" />
            ) : null}
          </>
        }
        subtitle={
          <>
            {kickoffDay(data.match_date, data.kickoff?.time)} {kickoffTime(data.match_date, data.kickoff?.time)}
            {data.matchday ? ` · ${t("page.fixture.matchdayLine", { n: data.matchday })}` : ""}
            {data.season ? ` · ${data.season}` : ""}
            {data.status ? ` · ${data.status}` : ""}
          </>
        }
      />

      <div className="detail-stack">
        <div className="two-col">
          <PredictabilityPanel prediction={data.predictability} />
          <div className="detail-side">
            <TeamCard side="home" team={home} standings={data.standings?.home} />
            <TeamCard side="away" team={away} standings={data.standings?.away} />
          </div>
        </div>

        {/* Reused verbatim: the endpoint returns these two sections in exactly the
            shape /matches/{api_id}/insights uses. */}
        <MatchInsights
          insights={{ pre_match: data.pre_match, model: null, head_to_head: data.head_to_head }}
          homeName={home?.name}
          awayName={away?.name}
        />

        <Card>
          <CardHeader title={t("page.fixture.record")} />
          <TableShell>
            <table className="data">
              <tbody>
                <tr>
                  <th scope="row">{t("common.league")}</th>
                  <td>
                    <Link className="link" to={`/leagues/${data.league}`}>
                      {data.league_name || data.real_league_name || data.league}
                    </Link>
                    {data.country ? <span className="muted"> · {data.country}</span> : null}
                  </td>
                </tr>
                <tr>
                  <th scope="row">{t("page.fixture.matchday")}</th>
                  <td>{data.matchday ?? "—"}</td>
                </tr>
                <tr>
                  <th scope="row">{t("common.season")}</th>
                  <td>
                    {data.season || "—"}
                    {data.season_state ? <span className="muted"> · {data.season_state}</span> : null}
                  </td>
                </tr>
                <tr>
                  <th scope="row">{t("page.fixture.kickoff")}</th>
                  <td>
                    {data.kickoff?.match_datetime
                      ? `${instantHeading(data.kickoff.match_datetime)} · ${instantTime(data.kickoff.match_datetime)}`
                      : data.kickoff?.time || "—"}
                  </td>
                </tr>
                <tr>
                  <th scope="row">{t("page.fixture.label")}</th>
                  <td>{data.kickoff?.label || "—"}</td>
                </tr>
                <tr>
                  <th scope="row">{t("page.fixture.phase")}</th>
                  <td>{data.kickoff?.league_phase_status || "—"}</td>
                </tr>
                {portalLink ? (
                  <tr>
                    <th scope="row">{t("page.fixture.source")}</th>
                    <td>
                      <a
                        className="link"
                        href={portalLink}
                        target="_blank"
                        rel="noopener noreferrer"
                        referrerPolicy="no-referrer"
                      >
                        football-charts.com
                      </a>
                    </td>
                  </tr>
                ) : null}
              </tbody>
            </table>
          </TableShell>
        </Card>
      </div>
    </div>
  );
}
