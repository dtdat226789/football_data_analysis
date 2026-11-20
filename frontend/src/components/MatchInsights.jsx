import { Link } from "react-router-dom";

import { TableShell } from "./ui/index.js";
import { useFormatters } from "../i18n/useFormatters.js";

const RESULT_KEY = { HOME_WIN: "result.home", DRAW: "result.draw", AWAY_WIN: "result.away" };

/** Same confidence buckets as PredictionChips, so the two read alike. */
function strength(v) {
  if (typeof v !== "number") return "";
  if (v >= 0.6) return "chip-strong";
  if (v >= 0.45) return "chip-mid";
  return "chip-weak";
}

/**
 * Pre-match context: the feature row the model was given, grouped for reading.
 * Strictly pre-match by construction — the backend never includes the result.
 */
export function PreMatchPanel({ preMatch }) {
  const { t, dec } = useFormatters();
  if (!preMatch) return null;
  const groups = preMatch.groups || {};
  const keys = Object.keys(groups);
  if (!keys.length) return null;

  return (
    <section className="card">
      <h3>
        {t("insights.preMatch")} <span className="badge">{t("insights.matchday", { n: preMatch.game_index })}</span>
      </h3>
      <p className="muted insight-summary">
        {t("insights.preMatchSummary", {
          home: preMatch.home_team,
          away: preMatch.away_team,
          season: preMatch.season,
        })}
      </p>
      {keys.map((key) => (
        <div key={key} className="insight-group">
          <h4 className="insight-group-title">
            {(preMatch.group_labels || {})[key] || key}
          </h4>
          <div className="mini-grid">
            {Object.entries(groups[key]).map(([column, cell]) => (
              <div key={column}>
                <div className="muted insight-cell-label">
                  {cell.label}
                </div>
                <div className="tabular">{dec(cell.value, 2)}</div>
              </div>
            ))}
          </div>
        </div>
      ))}
    </section>
  );
}

/**
 * The stored model view. Historical rows are in-sample unless the match is in
 * a holdout season, so the badge and warning are load-bearing, not decoration.
 */
export function ModelPanel({ model }) {
  const { t, pct } = useFormatters();
  if (!model) return null;
  const probs = model.probabilities || {};
  const meta = model.meta || {};
  const outcomeHit =
    typeof model.actual_match_result === "string" &&
    model.predicted_match_result === model.actual_match_result;
  const label = t("insights.modelView");

  return (
    <section className="card">
      <h3>
        {label}{" "}
        {model.in_sample ? (
          <span className="badge amber">{t("insights.inSample")}</span>
        ) : (
          <span className="badge green">{t("insights.outOfSample")}</span>
        )}
      </h3>

      <div className="prob-list">
        {Object.entries(probs).map(([key, value]) => (
          <div key={key} className="prob-row">
            <div className="prob-line">
              <span>{t(RESULT_KEY[key] ?? "") || key}</span>
              <span className="tabular">{pct(value)}</span>
            </div>
            <div className="bar-track prob-track" style={{ height: 8 }}>
              <div
                className="bar-fill prob-fill"
                style={{ width: `${(value || 0) * 100}%` }}
              />
            </div>
          </div>
        ))}
      </div>

      <TableShell label={label}>
        <table className="data">
          <tbody>
            <tr>
              <th scope="row">{t("insights.predicted")}</th>
              <td>
                {t(RESULT_KEY[model.predicted_match_result] ?? "") || model.predicted_match_result}{" "}
                <span className="pred-chips">
                  <span className={`pred-chip ${strength(model.confidence)}`}>
                    {t("pred.confModel")} <b>{pct(model.confidence)}</b>
                  </span>
                </span>
              </td>
            </tr>
            <tr>
              <th scope="row">{t("insights.actual")}</th>
              <td>
                {t(RESULT_KEY[model.actual_match_result] ?? "") || model.actual_match_result || "—"}{" "}
                {model.actual_match_result && (
                  <span className={`badge ${outcomeHit ? "green" : "amber"}`}>
                    {outcomeHit ? t("insights.correct") : t("insights.wrong")}
                  </span>
                )}
              </td>
            </tr>
            <tr>
              <th scope="row">{t("insights.model")}</th>
              <td>{meta.model_id || "—"}</td>
            </tr>
            <tr>
              <th scope="row">{t("insights.featureVersion")}</th>
              <td>{meta.feature_version || "—"}</td>
            </tr>
          </tbody>
        </table>
      </TableShell>

      {model.in_sample && meta.in_sample_warning && (
        <p className="muted insight-warning">
          {meta.in_sample_warning}
        </p>
      )}
    </section>
  );
}

/** Prior meetings only; the endpoint already excludes this match and later ones. */
export function HeadToHeadPanel({ headToHead, homeName, awayName }) {
  const { t, plainDay } = useFormatters();
  if (!headToHead) return null;
  const { matches = [], summary, truncated } = headToHead || {};
  const label = t("insights.headToHead");

  return (
    <section className="card">
      <h3>
        {label}{" "}
        <span className="badge">
          {t("insights.previous", { n: summary ? summary.played : matches.length })}
        </span>
      </h3>

      {summary ? (
        <p className="muted insight-summary">
          {t("insights.h2hSummary", {
            home: homeName,
            away: awayName,
            wins: summary.home_team_wins,
            draws: summary.draws,
            losses: summary.away_team_wins,
            for: summary.goals_for,
            against: summary.goals_against,
          })}
        </p>
      ) : (
        <p className="muted insight-summary">
          {t("insights.noH2h")}
        </p>
      )}

      {truncated && (
        <p className="muted insight-cell-label">
          {t("insights.truncated", { shown: matches.length, total: summary.played })}
        </p>
      )}

      {matches.length > 0 && (
        <TableShell label={label}>
          <table className="data">
            <thead>
              <tr>
                <th scope="col">{t("common.date")}</th>
                <th scope="col">{t("common.season")}</th>
                <th scope="col">{t("insights.fixture")}</th>
                <th scope="col">{t("common.score")}</th>
              </tr>
            </thead>
            <tbody>
              {matches.map((m) => (
                <tr key={m.api_id}>
                  <td>{plainDay(m.match_date)}</td>
                  <td>{m.season}</td>
                  <td>
                    <Link className="link" to={`/match/${m.api_id}`}>
                      {m.home_team} {t("common.vs")} {m.away_team}
                    </Link>
                  </td>
                  <td>
                    {typeof m.home_score === "number" && typeof m.away_score === "number"
                      ? `${m.home_score} – ${m.away_score}`
                      : "—"}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </TableShell>
      )}
    </section>
  );
}

export default function MatchInsights({ insights, homeName, awayName }) {
  if (!insights) return null;
  const { pre_match: preMatch, model, head_to_head: h2h } = insights;
  if (!preMatch && !model && !(h2h && h2h.matches && h2h.matches.length)) return null;

  return (
    <div className="two-col insights-grid">
      <PreMatchPanel preMatch={preMatch} />
      <div className="detail-side">
        <ModelPanel model={model} />
        <HeadToHeadPanel headToHead={h2h} homeName={homeName} awayName={awayName} />
      </div>
    </div>
  );
}
