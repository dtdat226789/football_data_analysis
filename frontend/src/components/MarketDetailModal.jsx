import { useEffect } from "react";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, TableSkeleton } from "./State.jsx";
import { chipLabel } from "./PredictionChips.jsx";
import { useFormatters } from "../i18n/useFormatters.js";

/**
 * How a cell settles. A quarter line yields two outcomes for one scoreline, so
 * the outcome codes are looked up rather than derived — the backend already
 * knows which half of the stake a scoreline refunds.
 */
const OUTCOME_KEY = {
  win: "outcome.win",
  push: "outcome.push",
  lose: "outcome.lose",
  "win+push": "outcome.win+push",
  "push+lose": "outcome.push+lose",
  "win+lose": "outcome.win+lose",
};

/** `push` above a hair is worth a line of its own; 0.0% push is not. */
function hasPush(settlement) {
  return typeof settlement?.push === "number" && settlement.push > 0.00005;
}

/**
 * One bar per settlement outcome, at the weight the outcome actually carries.
 * Kept to three fixed slots so the bars line up across markets instead of
 * reflowing when a line happens to be able to refund.
 */
function SettlementBars({ settlement, t, pct }) {
  if (!settlement) return null;
  const entries = [
    { id: "win", key: "modal.settle.wins", value: settlement.win, cls: "settle-win" },
    { id: "push", key: "modal.settle.pushes", value: settlement.push, cls: "settle-push" },
    { id: "lose", key: "modal.settle.loses", value: settlement.lose, cls: "settle-lose" },
  ];
  return (
    <div className="settle">
      {entries.map((entry) => (
        <div key={entry.id} className="settle-row">
          <span className="settle-label">{t(entry.key)}</span>
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

function CellList({ detail, t, pct }) {
  const cells = Array.isArray(detail.cells) ? detail.cells : [];
  if (!cells.length) return null;
  const widest = cells[0]?.probability || 1;
  return (
    <>
      <table className="data cell-table">
        <thead>
          <tr>
            <th>{t("modal.col.score")}</th>
            <th>{t("market.col.settlesAs")}</th>
            <th className="num">{t("modal.col.chance")}</th>
            <th className="num">{t("modal.col.share")}</th>
          </tr>
        </thead>
        <tbody>
          {cells.slice(0, TOP_CELLS).map((cell) => (
            <tr key={cell.score}>
              <td>{cell.score}</td>
              <td className="muted">{t(OUTCOME_KEY[cell.outcome] ?? "") || cell.outcome}</td>
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
          {t(cells.length - TOP_CELLS === 1 ? "modal.moreCellsOne" : "modal.moreCells", {
            n: cells.length - TOP_CELLS,
          })}
        </p>
      )}
    </>
  );
}

/** HT/FT has no cells: it is a product of the two halves' own 1X2 splits. */
function FactorTable({ detail, t, pct }) {
  const factors = detail.factors;
  if (!factors) return null;
  const sides = [
    { id: "half_time", key: "market.scope.half_time", pick: factors.half_time_side },
    { id: "full_time", key: "market.scope.full_time", pick: factors.full_time_side },
  ];
  return (
    <>
      <table className="data">
        <thead>
          <tr>
            <th>{t("modal.col.half")}</th>
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
                <td>{t(side.key)}</td>
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
      <p className="muted cell-more">{t("modal.halvesNote")}</p>
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
  const { t, pct, line } = useFormatters();
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
  const scope = t(market.scope ? `market.scope.${market.scope}` : "") || t("market.scope.full_time");
  const title = `${chipLabel(market, t, line) || detail?.label || t("modal.title")} · ${scope}`;

  return (
    <div className="lightbox-backdrop" role="dialog" aria-modal="true" aria-label={title} onClick={onClose}>
      <div className="lightbox-frame market-frame" onClick={(e) => e.stopPropagation()}>
        <div className="lightbox-head">
          <span className="caption">{title}</span>
          <button type="button" className="lightbox-close" onClick={onClose} aria-label={t("common.close")}>
            ×
          </button>
        </div>

        {loading && <TableSkeleton rows={4} cols={4} />}
        {error && <ErrorBox error={error} />}
        {!loading && !error && detail === null && (
          <p className="muted">{t("modal.noExplanation")}</p>
        )}
        {!loading && !error && detail && (
          <div className="market-detail">
            <div className="market-detail-head">
              <span
                className={"badge" + (detail.provenance === "modelled" ? " amber" : " green")}
                title={detail.provenance === "modelled" ? t("market.provenanceAssumed") : t("market.provenanceModel")}
              >
                {detail.provenance === "modelled" ? t("market.assumed") : t("market.model")}
              </span>
              {hasPush(detail.settlement) && <span className="badge">{t("market.refunds")}</span>}
              <span className="muted">{detail.method}</span>
            </div>

            <h4 className="market-detail-title">{t("modal.settlement")}</h4>
            <SettlementBars settlement={detail.settlement} t={t} pct={pct} />

            {detail.factors ? (
              <>
                <h4 className="market-detail-title">{t("modal.whereFrom")}</h4>
                <FactorTable detail={detail} t={t} pct={pct} />
              </>
            ) : (
              <>
                <h4 className="market-detail-title">
                  {t("modal.scorelines")}
                  <span className="muted">
                    {" "}
                    — {t("modal.gridCells", { paying: detail.paying_cells, grid: detail.grid_cells })}
                  </span>
                </h4>
                <CellList detail={detail} t={t} pct={pct} />
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}