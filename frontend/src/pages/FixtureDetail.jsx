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

const RESULT_LABEL = { home: "Home win", draw: "Draw", away: "Away win" };
const SCOPE_LABEL = { full_time: "Full time", half_time: "Half time" };

const pct = (v) => (typeof v === "number" ? `${(v * 100).toFixed(1)}%` : "—");

/** fmt keeps integers clean, renders floats to `dp` places, nulls become an em dash. */
function fmt(value, dp = 2) {
  if (value === null || value === undefined) return "—";
  if (typeof value === "number") {
    return Number.isInteger(value) ? String(value) : value.toFixed(dp);
  }
  return String(value);
}

/** Strip the `over_`/`ht_over_` prefix the API keeps, leaving the quoted line. */
function lineLabel(line) {
  return String(line || "").replace(/^ht_/, "").replace(/^over_/, "Over ");
}

/**
 * The model's full read on an unplayed fixture: the 1/X/2 split with bars, the
 * expected goals behind it, and the gates/ratings/sample-size metadata that says
 * how much to trust the number.
 */
function PredictabilityPanel({ prediction, onSelectMarket }) {
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
        Prediction{" "}
        <span className="badge">{prediction.model || "—"}</span>
        {status.stale && <span className="badge amber">stale</span>}
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
              <span>{RESULT_LABEL[key]}</span>
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
            <th>Expected goals</th>
            <td>
              {fmt(goals.home)} – {fmt(goals.away)}
              <span className="muted" style={{ marginLeft: 8 }}>
                HT total {fmt(goals.half_time_total)}
              </span>
            </td>
          </tr>
          <tr>
            <th>Ratings</th>
            <td>
              {["home", "away"].map((side) => (
                <span key={side} style={{ marginRight: 12 }}>
                  {side} att {fmt(ratings[side]?.attack)} / def {fmt(ratings[side]?.defence)}
                </span>
              ))}
            </td>
          </tr>
          <tr>
            <th>Sample size</th>
            <td>
              {["home", "away"].map((side) => (
                <span key={side} style={{ marginRight: 12 }}>
                  {side} {fmt(effective[side], 1)}
                </span>
              ))}
              <span className="muted">effective matches</span>
            </td>
          </tr>
          <tr>
            <th>Draw inflation</th>
            <td>
              {fmt(prediction.xi, 4)}
              <span className="muted" style={{ marginLeft: 8 }}>
                sigma {fmt(prediction.sigma)}
              </span>
            </td>
          </tr>
          <tr>
            <th>Gates</th>
            <td>
              {Object.entries(gates).length
                ? Object.entries(gates)
                    .map(([name, passed]) => `${name}: ${passed ? "pass" : "fail"}`)
                    .join(" · ")
                : "—"}
            </td>
          </tr>
          <tr>
            <th>Data through</th>
            <td>
              {prediction.data_through || "—"}
              <span className="muted" style={{ marginLeft: 8 }}>
                {status.matches_behind ? `${status.matches_behind} matches behind` : ""}
              </span>
            </td>
          </tr>
          <tr>
            <th>Computed</th>
            <td className="muted">{prediction.computed_at || "—"}</td>
          </tr>
        </tbody>
      </table>
    </section>
  );
}

/** Every over/under line the model priced, uncalibrated beside calibrated. */
function GoalLinesPanel({ lines }) {
  if (!lines || !lines.length) return null;
  return (
    <section className="card">
      <h3 style={{ marginTop: 0 }}>Goal lines</h3>
      <table className="data">
        <thead>
          <tr>
            <th>Scope</th>
            <th>Line</th>
            <th className="num">Raw</th>
            <th className="num">Calibrated</th>
          </tr>
        </thead>
        <tbody>
          {lines.map((row) => (
            <tr key={row.line}>
              <td className="muted">{SCOPE_LABEL[row.scope] || row.scope}</td>
              <td>{lineLabel(row.line)}</td>
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
          ({side})
        </span>
      </h3>

      <div style={{ marginBottom: 10 }}>
        <span className="muted" style={{ fontSize: 12, display: "block" }}>
          Form (last {team.form?.length || 0})
        </span>
        <FormPills results={team.form} />
      </div>

      <table className="data">
        <tbody>
          <tr>
            <th>Venue split</th>
            <td>
              {venue ? (
                <>
                  {venue.wins}W {venue.draws}D {venue.losses}L · win rate{" "}
                  {pct(venue.win_rate)} · {fmt(venue.goals_avg)} scored,{" "}
                  {fmt(venue.conceded_avg)} conceded
                </>
              ) : (
                "—"
              )}
            </td>
          </tr>
          <tr>
            <th>Rest</th>
            <td>{team.rest_days != null ? `${team.rest_days} days` : "—"}</td>
          </tr>
          <tr>
            <th>Played</th>
            <td>{team.games_before ?? "—"}</td>
          </tr>
          <tr>
            <th>Table</th>
            <td>
              {standings ? (
                <>
                  {standings.position} · {standings.points} pts · {standings.goal_difference > 0 ? "+" : ""}
                  {standings.goal_difference} · {standings.played} played
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
  if (!data) return <ErrorBox error="No fixture data." />;

  const home = data.teams?.home;
  const away = data.teams?.away;

  return (
    <div>
      <div className="page-head">
        <h2>
          {home?.logo ? (
            <img src={home.logo} alt="" width={24} height={24} style={{ objectFit: "contain" }} />
          ) : null}{" "}
          <TeamLink name={home?.name} /> vs <TeamLink name={away?.name} />{" "}
          {away?.logo ? (
            <img src={away.logo} alt="" width={24} height={24} style={{ objectFit: "contain" }} />
          ) : null}
        </h2>
        <p>
          {data.match_date} {data.kickoff?.time || ""}
          {data.matchday ? ` · matchday ${data.matchday}` : ""}
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
        <h3 style={{ marginTop: 0 }}>Fixture record</h3>
        <table className="data">
          <tbody>
            <tr>
              <th>League</th>
              <td>
                <Link className="link" to={`/leagues/${data.league}`}>
                  {data.league_name || data.real_league_name || data.league}
                </Link>
                {data.country ? <span className="muted"> · {data.country}</span> : null}
              </td>
            </tr>
            <tr>
              <th>Matchday</th>
              <td>{data.matchday ?? "—"}</td>
            </tr>
            <tr>
              <th>Season</th>
              <td>
                {data.season || "—"}
                {data.season_state ? <span className="muted"> · {data.season_state}</span> : null}
              </td>
            </tr>
            <tr>
              <th>Kickoff</th>
              <td>{data.kickoff?.match_datetime || data.kickoff?.time || "—"}</td>
            </tr>
            <tr>
              <th>Label</th>
              <td>{data.kickoff?.label || "—"}</td>
            </tr>
            <tr>
              <th>Phase</th>
              <td>{data.kickoff?.league_phase_status || "—"}</td>
            </tr>
            {data.kickoff?.portal_link ? (
              <tr>
                <th>Source</th>
                <td>
                  <a className="link" href={data.kickoff.portal_link} target="_blank" rel="noreferrer">
                    football-charts.com
                  </a>
                </td>
              </tr>
            ) : null}
            <tr>
              <th>Slug</th>
              <td className="muted">{data.slug || "—"}</td>
            </tr>
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
