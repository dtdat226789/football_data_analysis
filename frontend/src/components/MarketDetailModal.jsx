import { useEffect } from "react";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, TableSkeleton } from "./State.jsx";

const pct = (v) => (typeof v === "number" ? `${(v * 100).toFixed(1)}%` : "—");

const SCOPE_LABEL = {
  full_time: "Full time",
  half_time: "Half time",
  half_to_full: "HT / FT",
};

/** How a cell settles. A quarter line yields two outcomes for one scoreline. */
const OUTCOME_LABEL = {
  win: "wins",
  push: "pushes",
  lose: "loses",
  "win+push": "wins half, pushes half",
  "push+lose": "pushes half, loses half",
  "win+lose": "wins half, loses half",
};

function outcomeText(outcome) {
  return OUTCOME_LABEL[outcome] || outcome;
}

/** `push` above a hair is worth a line of its own; 0.0% push is not. */
function hasPush(settlement) {
  return typeof settlement?.push === "number" && settlement.push > 0.00005;
}

/**
 * One bar per settlement outcome, at the weight the outcome actually carries.
 * Kept to three fixed slots so the bars line up across markets instead of
 * reflowing when a line happens to be able to refund.
 */
function SettlementBars({ settlement }) {
  if (!settlement) return null;
  const entries = [
    { id: "win", label: "Wins", value: settlement.win, cls: "settle-win" },
    { id: "push", label: "Pushes", value: settlement.push, cls: "settle-push" },
    { id: "lose", label: "Loses", value: settlement.lose, cls: "settle-lose" },
  ];
  return (
    <div className="settle">
      {entries.map((entry) => (
        <div key={entry.id} className="settle-row">
          <span className="settle-label">{entry.label}</span>
          <span className="bar-track" style={{ height: 8 }}>
            <span
              className={"bar-fill " + entry.cls}
              style={{ width: `${Math.max(0, Math.min(1, entry.value || 0)) * 100}%` }}
            />
          </span>
          <span className="settle-value">{pct(entry.value)}</span>
        </div>
      ))}
    </div>
  );
}

/**
 * The scorelines that pay the bet, most likely first.
 *
 * Only the top slice is listed: a 1X2 market pays on 36 of the 81 grid cells
 * and the tail past the eighth contributes almost nothing, so the count line
 * above carries the full picture and this carries the shape.
 */
const TOP_CELLS = 8;

function CellList({ detail }) {
  const cells = Array.isArray(detail.cells) ? detail.cells : [];
  if (!cells.length) return null;
  const widest = cells[0]?.probability || 1;
  return (
    <>
      <table className="data cell-table">
        <thead>
          <tr>
            <th>Score</th>
            <th>Settles as</th>
            <th className="num">Chance</th>
            <th className="num">Share</th>
          </tr>
        </thead>
        <tbody>
          {cells.slice(0, TOP_CELLS).map((cell) => (
            <tr key={cell.score}>
              <td>{cell.score}</td>
              <td className="muted">{outcomeText(cell.outcome)}</td>
              <td className="num">
                <span className="cell-bar">
                  <span
                    className="bar-fill settle-cell"
                    style={{ width: `${(cell.probability / widest) * 100}%` }}
                  />
                </span>
                {pct(cell.probability)}
              </td>
              <td className="num">{pct(cell.share)}</td>
            </tr>
          ))}
        </tbody>
      </table>
      {cells.length > TOP_CELLS && (
        <p className="muted cell-more">
          and {cells.length - TOP_CELLS} further scoreline{cells.length - TOP_CELLS === 1 ? "" : "s"}.
        </p>
      )}
    </>
  );
}

/** HT/FT has no cells: it is a product of the two halves' own 1X2 splits. */
function FactorTable({ detail }) {
  const factors = detail.factors;
  if (!factors) return null;
  const sides = [
    { id: "half_time", label: "Half time", pick: factors.half_time_side },
    { id: "full_time", label: "Full time", pick: factors.full_time_side },
  ];
  return (
    <>
      <table className="data">
        <thead>
          <tr>
            <th>Half</th>
            <th className="num">1</th>
            <th className="num">X</th>
            <th className="num">2</th>
          </tr>
        </thead>
        <tbody>
          {sides.map((side) => {
            const row = factors[side.id] || {};
            return (
              <tr key={side.id} className={side.pick ? "featured" : ""}>
                <td>{side.label}</td>
                {["home", "draw", "away"].map((outcome) => (
                  <td key={outcome} className="num">
                    {pct(row[outcome])}
                  </td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
      <p className="muted cell-more">
        The two halves are multiplied together, so this market is a product of the rows above
        rather than a set of scorelines.
      </p>
    </>
  );
}

/**
 * Why one derived market has the number it has.
 *
 * A chip or a market-table row is one number with no visible mechanism. This
 * opens the arithmetic behind it: how it settles across win/push/lose, and
 * which scorelines in the model's 81-cell goal grid pay it — so a reader can see
 * that "Home -0.25" splits a level result into half a refund and half a loss
 * rather than taking the probability on trust.
 *
 * The explanation is fetched per market instead of shipped with the fixture
 * because explaining all ~159 derived markets would dwarf the fixture itself.
 */
export default function MarketDetailModal({ league, matchId, market, onClose }) {
  const { data, loading, error } = useApi(
    () => (league && matchId && market?.key ? api.fixtureMarket(league, matchId, market.key) : null),
    [league, matchId, market?.key],
    { ttl: 10 * 60 * 1000 },
  );

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "Escape") onClose?.();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  if (!market) return null;

  const detail = data?.market;
  const title = `${market.label || detail?.label || "Market"} · ${SCOPE_LABEL[market.scope] || market.scope || "Full time"}`;

  return (
    <div className="lightbox-backdrop" role="dialog" aria-modal="true" aria-label={title} onClick={onClose}>
      <div className="lightbox-frame market-frame" onClick={(e) => e.stopPropagation()}>
        <div className="lightbox-head">
          <span className="caption">{title}</span>
          <button type="button" className="lightbox-close" onClick={onClose} aria-label="Close">
            ×
          </button>
        </div>

        {loading && <TableSkeleton rows={4} cols={4} />}
        {error && <ErrorBox error={error} />}
        {!loading && !error && detail === null && (
          <p className="muted">This market has no explanation to show.</p>
        )}
        {!loading && !error && detail && (
          <div className="market-detail">
            <div className="market-detail-head">
              <span
                className={"badge" + (detail.provenance === "modelled" ? " amber" : " green")}
                title={
                  detail.provenance === "modelled"
                    ? "Assumed — the model does not publish the half-time goal split, so this is derived, not published"
                    : "From the model's goal distribution"
                }
              >
                {detail.provenance === "modelled" ? "assumed" : "model"}
              </span>
              {hasPush(detail.settlement) && <span className="badge">refunds</span>}
              <span className="muted">{detail.method}</span>
            </div>

            <h4 className="market-detail-title">Settlement</h4>
            <SettlementBars settlement={detail.settlement} />

            {detail.factors ? (
              <>
                <h4 className="market-detail-title">Where it comes from</h4>
                <FactorTable detail={detail} />
              </>
            ) : (
              <>
                <h4 className="market-detail-title">
                  Scorelines that pay it
                  <span className="muted">
                    {" "}
                    — {detail.paying_cells} of {detail.grid_cells} grid cells
                  </span>
                </h4>
                <CellList detail={detail} />
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
