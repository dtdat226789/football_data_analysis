import { useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Skeleton } from "../components/State.jsx";
import { FormPills } from "../components/FormPills.jsx";
import MarketDetailModal from "../components/MarketDetailModal.jsx";
import MatchInsights from "../components/MatchInsights.jsx";
import MarketTable from "../components/MarketTable.jsx";
import PredictionChips from "../components/PredictionChips.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import { useFormatters } from "../i18n/useFormatters.js";

const RESULT_KEY = { home: "result.home", draw: "result.draw", away: "result.away" };
const SCOPE_KEY = { full_time: "market.scope.full_time", half_time: "market.scope.half_time" };

/** Strip the `over_`/`ht_over_` prefix the API keeps, leaving the quoted line. */
function lineLabel(line, t) {
  const s = String(line || "");
  const over = s.replace(/^ht_/, "").replace(/^over_/, "");
  return over === s ? s : `${t("fixture.over")} ${over}`;
}

/**
 * The model's full read on an unplayed fixture: the 1/X/2 split with bars, the
 * expected goals behind it, and the gates/ratings/sample-size metadata that says
 * how much to trust the number.
 */
function PredictabilityPanel({ prediction, onSelectMarket }) {
  const { t, pct, dec } = useFormatters();
  if (!prediction) return null;
  const probs = prediction.probabilities || {};
  const goals = prediction.expected_goals || {};
  const ratings = prediction.ratings || {};
  const effective = prediction.effective_matches || {};
  const status = prediction.data_status || {};
  const gates = prediction.gates || {};

  return (
    <section className="card">
      <h3 style={{ marginTop: 0 }}>
        {t("predictability.title")}{" "}
        <span className="badge">{prediction.model || "—"}</span>
        {status.stale && <span className="badge amber">{t("predictability.stale")}</span>}
      </h3>

      <div style={{ marginBottom: 12 }}>
        {["home", "draw", "away"].map((key) => (
          <div key={key} style={{ marginBottom: 8 }}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                fontSize: 13,
                marginBottom: 3,
              }}
            >
              <span>{t(RESULT_KEY[key])}</span>
              <span style={{ fontVariantNumeric: "tabular-nums" }}>{pct(probs[key])}</span>
            </div>
            <div className="bar-track" style={{ height: 8 }}>
              <div
                className="bar-fill"
                style={{ width: `${(probs[key] || 0) * 100}%`, background: "var(--accent)" }}
              />
            </div>
          </div>
        ))}
      </div>

      <PredictionChips
        predictions={{ ...prediction.summary, selected: prediction.selected }}
        confidence={prediction.summary?.confidence}
        dataThrough={prediction.data_through}
        onSelect={onSelectMarket}
      />

      <table className="data" style={{ marginTop: 12 }}>
        <tbody>
          <tr>
            <th>{t("predictability.expectedGoals")}</th>
            <td>
              {dec(goals.home, 2)} – {dec(goals.away, 2)}
              <span className="muted" style={{ marginLeft: 8 }}>
                {t("predictability.htTotal")} {dec(goals.half_time_total, 2)}
              </span>
            </td>
          </tr>
          <tr>
            <th>{t("predictability.ratings")}</th>
            <td>
              {["home", "away"].map((side) => (
                <span key={side} style={{ marginRight: 12 }}>
                  {side} att {dec(ratings[side]?.attack, 2)} / def {dec(ratings[side]?.defence, 2)}
                </span>
              ))}
            </td>
          </tr>
          <tr>
            <th>{t("predictability.sampleSize")}</th>
            <td>
              {["home", "away"].map((side) => (
                <span key={side} style={{ marginRight: 12 }}>
                  {side} {dec(effective[side], 1)}
                </span>
              ))}
              <span className="muted">{t("predictability.effectiveMatches")}</span>
            </td>
          </tr>
          <tr>
            <th>{t("predictability.drawInflation")}</th>
            <td>
              {dec(prediction.xi, 4)}
              <span className="muted" style={{ marginLeft: 8 }}>
                sigma {dec(prediction.sigma, 1)}
              </span>
            </td>
          </tr>
          <tr>
            <th>{t("predictability.gates")}</th>
            <td>
              {Object.entries(gates).length
                ? Object.entries(gates)
                    .map(([name, passed]) => `${name}: ${passed ? t("predictability.pass") : t("predictability.fail")}`)
                    .join(" · ")
                : "—"}
            </td>
          </tr>
          <tr>
            <th>{t("predictability.dataThrough")}</th>
            <td>
              {prediction.data_through || "—"}
              <span className="muted" style={{ marginLeft: 8 }}>
                {status.matches_behind ? t("predictability.matchesBehind", { n: status.matches_behind }) : ""}
              </span>
            </td>
          </tr>
          <tr>
            <th>{t("predictability.computed")}</th>
            <td className="muted">{prediction.computed_at || "—"}</td>
          </tr>
        </tbody>
      </table>
    </section>
  );
}

/** Every over/under line the model priced, uncalibrated beside calibrated. */
function GoalLinesPanel({ lines }) {
  const { t, pct } = useFormatters();
  if (!lines || !lines.length) return null;
  return (
    <section className="card">
      <h3 style={{ marginTop: 0 }}>{t("predictability.goalLines")}</h3>
      <table className="data">
        <thead>
          <tr>
            <th>{t("market.col.scope")}</th>
            <th>{t("predictability.col.line")}</th>
            <th className="num">{t("predictability.col.raw")}</th>
            <th className="num">{t("predictability.col.calibrated")}</th>
          </tr>
        </thead>
        <tbody>
          {lines.map((row) => (
            <tr key={row.line}>
              <td className="muted">{t(SCOPE_KEY[row.scope] ?? "") || row.scope}</td>
              <td>{lineLabel(row.line, t)}</td>
              <td className="num">{pct(row.raw)}</td>
              <td className="num">{pct(row.calibrated)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

/** One side: crest, name, recent form, and the split that venue implies. */
function TeamCard({ side, team, standings }) {
  const { t, pct, dec } = useFormatters();
  if (!team) return null;
  const venue = team.venue;
  return (
    <section className="card">
      <h3 style={{ marginTop: 0, display: "flex", alignItems: "center", gap: 8 }}>
        {team.logo ? (
          <img src={team.logo} alt="" width={22} height={22} style={{ objectFit: "contain" }} />
        ) : null}
        <TeamLink name={team.name} />
        <span className="muted" style={{ fontSize: 13, fontWeight: 400 }}>
          {t(side === "home" ? "page.team.venue.home" : "page.team.venue.away")}
        </span>
      </h3>

      <div style={{ marginBottom: 10 }}>
        <span className="muted" style={{ fontSize: 12, display: "block" }}>
          {t("predictability.form", { n: team.form?.length || 0 })}
        </span>
        <FormPills results={team.form} />
      </div>

      <table className="data">
        <tbody>
          <tr>
            <th>{t("predictability.venueSplit")}</th>
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
            <th>{t("predictability.rest")}</th>
            <td>{team.rest_days != null ? t("predictability.restDays", { n: team.rest_days }) : "—"}</td>
          </tr>
          <tr>
            <th>{t("predictability.played")}</th>
            <td>{team.games_before ?? "—"}</td>
          </tr>
          <tr>
            <th>{t("predictability.table")}</th>
            <td>
              {standings ? (
                <>
                  {t("predictability.tableLine", {
                    position: standings.position,
                    points: standings.points,
                    gd: `${standings.goal_difference > 0 ? "+" : ""}${standings.goal_difference}`,
                    played: standings.played,
                  })}
                </>
              ) : (
                "—"
              )}
            </td>
          </tr>
        </tbody>
      </table>
    </section>
  );
}

export default function FixtureDetail() {
  const { t, kickoffDay, kickoffTime, instantTime, instantHeading } = useFormatters();
  const { league, "*": matchId } = useParams();
  const { data, loading, error } = useApi(
    () => (league && matchId ? api.fixtureDetail(league, matchId) : null),
    [league, matchId],
  );
  // One market at a time: the chips and the table hand over the row they were
  // clicked on, and the modal fetches the explanation for that row alone.
  const [market, setMarket] = useState(null);

  if (loading)
    return (
      <div>
        <Skeleton height={46} width="55%" style={{ maxWidth: 640 }} />
        <Skeleton width="35%" height={14} />
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

  return (
    <div>
      <div className="page-head">
        <h2>
          {home?.logo ? (
            <img src={home.logo} alt="" width={24} height={24} style={{ objectFit: "contain" }} />
          ) : null}{" "}
          <TeamLink name={home?.name} /> {t("common.vs")} <TeamLink name={away?.name} />{" "}
          {away?.logo ? (
            <img src={away.logo} alt="" width={24} height={24} style={{ objectFit: "contain" }} />
          ) : null}
        </h2>
        <p>
          {kickoffDay(data.match_date, data.kickoff?.time)} {kickoffTime(data.match_date, data.kickoff?.time)}
          {data.matchday ? ` · ${t("page.fixture.matchdayLine", { n: data.matchday })}` : ""}
          {data.season ? ` · ${data.season}` : ""}
          {data.status ? ` · ${data.status}` : ""}
        </p>
      </div>

      <div className="two-col">
        <PredictabilityPanel prediction={data.predictability} onSelectMarket={setMarket} />
        <div className="stack" style={{ display: "grid", gap: 16, alignContent: "start" }}>
          <TeamCard side="home" team={home} standings={data.standings?.home} />
          <TeamCard side="away" team={away} standings={data.standings?.away} />
        </div>
      </div>

      <div style={{ marginTop: 16 }}>
        <GoalLinesPanel lines={data.predictability?.lines} />
      </div>

      <div style={{ marginTop: 16 }}>
        <MarketTable
          markets={data.predictability?.markets}
          selected={data.predictability?.selected}
          onSelect={setMarket}
        />
      </div>

      {/* Reused verbatim: the endpoint returns these two sections in exactly the
          shape /matches/{api_id}/insights uses. */}
      <MatchInsights
        insights={{ pre_match: data.pre_match, model: null, head_to_head: data.head_to_head }}
        homeName={home?.name}
        awayName={away?.name}
      />

      <section className="card" style={{ marginTop: 16 }}>
        <h3 style={{ marginTop: 0 }}>{t("page.fixture.record")}</h3>
        <table className="data">
          <tbody>
            <tr>
              <th>{t("common.league")}</th>
              <td>
                <Link className="link" to={`/leagues/${data.league}`}>
                  {data.league_name || data.real_league_name || data.league}
                </Link>
                {data.country ? <span className="muted"> · {data.country}</span> : null}
              </td>
            </tr>
            <tr>
              <th>{t("page.fixture.matchday")}</th>
              <td>{data.matchday ?? "—"}</td>
            </tr>
            <tr>
              <th>{t("common.season")}</th>
              <td>
                {data.season || "—"}
                {data.season_state ? <span className="muted"> · {data.season_state}</span> : null}
              </td>
            </tr>
            <tr>
              <th>{t("page.fixture.kickoff")}</th>
              <td>
                {data.kickoff?.match_datetime
                  ? `${instantHeading(data.kickoff.match_datetime)} · ${instantTime(data.kickoff.match_datetime)}`
                  : data.kickoff?.time || "—"}
              </td>
            </tr>
            <tr>
              <th>{t("page.fixture.label")}</th>
              <td>{data.kickoff?.label || "—"}</td>
            </tr>
            <tr>
              <th>{t("page.fixture.phase")}</th>
              <td>{data.kickoff?.league_phase_status || "—"}</td>
            </tr>
            {data.kickoff?.portal_link ? (
              <tr>
                <th>{t("page.fixture.source")}</th>
                <td>
                  <a className="link" href={data.kickoff.portal_link} target="_blank" rel="noreferrer">
                    football-charts.com
                  </a>
                </td>
              </tr>
            ) : null}
          </tbody>
        </table>
      </section>

      {market && (
        <MarketDetailModal
          league={league}
          matchId={data.match_id || matchId}
          market={market}
          onClose={() => setMarket(null)}
        />
      )}
    </div>
  );
}
