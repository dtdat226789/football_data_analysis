import { Link } from "react-router-dom";

const pct = (v) => (typeof v === "number" ? `${(v * 100).toFixed(1)}%` : "—");

/** fmt keeps integers clean and renders floats to 2dp; nulls become an em dash. */
function fmt(value) {
  if (value === null || value === undefined) return "—";
  if (typeof value === "number") {
    return Number.isInteger(value) ? String(value) : value.toFixed(2);
  }
  return String(value);
}

const RESULT_LABEL = { HOME_WIN: "Home win", DRAW: "Draw", AWAY_WIN: "Away win" };

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
  if (!preMatch) return null;
  const groups = preMatch.groups || {};
  const keys = Object.keys(groups);
  if (!keys.length) return null;

  return (
    <section className="card">
      <h3 style={{ marginTop: 0 }}>
        Pre-match context <span className="badge">matchday {fmt(preMatch.game_index)}</span>
      </h3>
      <p className="muted" style={{ margin: "0 0 12px" }}>
        {preMatch.home_team} vs {preMatch.away_team} · {preMatch.season} — what the model
        knew before kickoff.
      </p>
      {keys.map((key) => (
        <div key={key} style={{ marginBottom: 14 }}>
          <h4 style={{ margin: "0 0 6px", fontSize: 13, color: "var(--muted)" }}>
            {(preMatch.group_labels || {})[key] || key}
          </h4>
          <div className="mini-grid">
            {Object.entries(groups[key]).map(([column, cell]) => (
              <div key={column}>
                <div className="muted" style={{ fontSize: 12 }}>
                  {cell.label}
                </div>
                <div style={{ fontVariantNumeric: "tabular-nums" }}>{fmt(cell.value)}</div>
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
  if (!model) return null;
  const probs = model.probabilities || {};
  const meta = model.meta || {};
  const outcomeHit =
    typeof model.actual_match_result === "string" &&
    model.predicted_match_result === model.actual_match_result;

  return (
    <section className="card">
      <h3 style={{ marginTop: 0 }}>
        Model view{" "}
        {model.in_sample ? (
          <span className="badge amber">in-sample</span>
        ) : (
          <span className="badge green">out-of-sample</span>
        )}
      </h3>

      <div style={{ marginBottom: 12 }}>
        {Object.entries(probs).map(([key, value]) => (
          <div key={key} style={{ marginBottom: 8 }}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                fontSize: 13,
                marginBottom: 3,
              }}
            >
              <span>{RESULT_LABEL[key] || key}</span>
              <span style={{ fontVariantNumeric: "tabular-nums" }}>{pct(value)}</span>
            </div>
            <div className="bar-track" style={{ height: 8 }}>
              <div
                className="bar-fill"
                style={{ width: `${(value || 0) * 100}%`, background: "var(--accent)" }}
              />
            </div>
          </div>
        ))}
      </div>

      <table className="data">
        <tbody>
          <tr>
            <th>Predicted</th>
            <td>
              {RESULT_LABEL[model.predicted_match_result] || model.predicted_match_result}{" "}
              <span className="pred-chips">
                <span className={`pred-chip ${strength(model.confidence)}`}>
                  conf <b>{pct(model.confidence)}</b>
                </span>
              </span>
            </td>
          </tr>
          <tr>
            <th>Actual</th>
            <td>
              {RESULT_LABEL[model.actual_match_result] || model.actual_match_result || "—"}{" "}
              {model.actual_match_result && (
                <span className={`badge ${outcomeHit ? "green" : "amber"}`}>
                  {outcomeHit ? "correct" : "wrong"}
                </span>
              )}
            </td>
          </tr>
          <tr>
            <th>Model</th>
            <td>{meta.model_id || "—"}</td>
          </tr>
          <tr>
            <th>Feature version</th>
            <td>{meta.feature_version || "—"}</td>
          </tr>
        </tbody>
      </table>

      {model.in_sample && meta.in_sample_warning && (
        <p className="muted" style={{ marginBottom: 0, fontSize: 12 }}>
          {meta.in_sample_warning}
        </p>
      )}
    </section>
  );
}

/** Prior meetings only; the endpoint already excludes this match and later ones. */
export function HeadToHeadPanel({ headToHead, homeName, awayName }) {
  if (!headToHead) return null;
  const { matches = [], summary, truncated } = headToHead || {};

  return (
    <section className="card">
      <h3 style={{ marginTop: 0 }}>
        Head to head{" "}
        <span className="badge">
          {summary ? `${summary.played} previous` : `${matches.length} previous`}
        </span>
      </h3>

      {summary ? (
        <p className="muted" style={{ marginTop: 0 }}>
          {homeName} {summary.home_team_wins}W {summary.draws}D {summary.away_team_wins}L{" "}
          {awayName} · goals {summary.goals_for}–{summary.goals_against}
        </p>
      ) : (
        <p className="muted" style={{ marginTop: 0 }}>
          No previous meetings on record.
        </p>
      )}

      {truncated && (
        <p className="muted" style={{ fontSize: 12 }}>
          Showing the {matches.length} most recent of {summary.played}.
        </p>
      )}

      {matches.length > 0 && (
        <table className="data">
          <thead>
            <tr>
              <th>Date</th>
              <th>Season</th>
              <th>Fixture</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {matches.map((m) => (
              <tr key={m.api_id}>
                <td>{m.match_date}</td>
                <td>{m.season}</td>
                <td>
                  <Link className="link" to={`/match/${m.api_id}`}>
                    {m.home_team} vs {m.away_team}
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
      )}
    </section>
  );
}

export default function MatchInsights({ insights, homeName, awayName }) {
  if (!insights) return null;
  const { pre_match: preMatch, model, head_to_head: h2h } = insights;
  if (!preMatch && !model && !(h2h && h2h.matches && h2h.matches.length)) return null;

  return (
    <div className="two-col" style={{ marginTop: 16 }}>
      <PreMatchPanel preMatch={preMatch} />
      <div className="stack" style={{ display: "grid", gap: 16, alignContent: "start" }}>
        <ModelPanel model={model} />
        <HeadToHeadPanel headToHead={h2h} homeName={homeName} awayName={awayName} />
      </div>
    </div>
  );
}
