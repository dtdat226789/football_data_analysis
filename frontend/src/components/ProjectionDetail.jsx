import { useEffect } from "react";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, TableSkeleton } from "./State.jsx";
import { highlightLabel } from "./ProjectionHighlights.jsx";
import { useFormatters } from "../i18n/useFormatters.js";

/**
 * How a cell is counted. A quarter line yields two outcomes for one scoreline, so
 * the outcome codes are looked up rather than derived — the backend already
 * knows which part of a scoreline is refunded.
 */
const OUTCOME_KEY = {
  win: "outcome.win",
  refund: "outcome.refund",
  lose: "outcome.lose",
  "win+refund": "outcome.win+refund",
  "refund+lose": "outcome.refund+lose",
  "win+lose": "outcome.win+lose",
};

/** `refund` above a hair is worth a line of its own; 0.0% refund is not. */
function hasRefund(outcomes) {
  return typeof outcomes?.refund === "number" && outcomes.refund > 0.00005;
}

/**
 * One bar per outcome, at the weight the outcome actually carries.
 * Kept to three fixed slots so the bars line up across projections instead of
 * reflowing when a line happens to be able to refund.
 */
function OutcomesBars({ outcomes, t, pct }) {
  if (!outcomes) return null;
  const entries = [
    { id: "win", key: "modal.count.wins", value: outcomes.win, cls: "count-win" },
    { id: "refund", key: "modal.count.refunds", value: outcomes.refund, cls: "count-refund" },
    { id: "lose", key: "modal.count.loses", value: outcomes.lose, cls: "count-lose" },
  ];
  return (
    <div className="count">
      {entries.map((entry) => (
        <div key={entry.id} className="count-row">
          <span className="count-label">{t(entry.key)}</span>
          <span className="bar-track" style={{ height: 8 }}>
            <span
              className={"bar-fill " + entry.cls}
              style={{ width: `${Math.max(0, Math.min(1, entry.value || 0)) * 100}%` }}
            />
          </span>
          <span className="count-value">{pct(entry.value)}</span>
        </div>
      ))}
    </div>
  );
}

/**
 * The scorelines that count for the scenario, most likely first.
 *
 * Only the top slice is listed: a match-outcome projection counts for 36 of the 81 grid cells
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
            <th>{t("projection.col.countedAs")}</th>
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
                    className="bar-fill count-cell"
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
    { id: "half_time", key: "projection.scope.half_time", pick: factors.half_time_side },
    { id: "full_time", key: "projection.scope.full_time", pick: factors.full_time_side },
  ];
  return (
    <>
      <table className="data">
        <thead>
          <tr>
            <th>{t("modal.col.half")}</th>
            <th className="num">{t("highlight.outcome.home")}</th>
            <th className="num">{t("highlight.outcome.draw")}</th>
            <th className="num">{t("highlight.outcome.away")}</th>
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
 * Why one derived projection has the number it has.
 *
 * A highlight or a projection-table row is one number with no visible mechanism. This
 * opens the arithmetic behind it: how it is counted across win/refund/lose, and
 * which scorelines in the model's 81-cell goal grid count for it — so a reader can see
 * that "Home −0.25" splits a level outcome into half a refund and half a loss
 * rather than taking the probability on trust.
 *
 * The explanation is fetched per projection instead of shipped with the fixture
 * because explaining all ~159 derived projections would dwarf the fixture itself.
 */
export default function ProjectionDetail({ league, matchId, projection, onClose }) {
  const { t, pct } = useFormatters();
  const { data, loading, error } = useApi(
    () => (league && matchId && projection?.key ? api.fixtureProjection(league, matchId, projection.key) : null),
    [league, matchId, projection?.key],
    { ttl: 10 * 60 * 1000 },
  );

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "Escape") onClose?.();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  if (!projection) return null;

  const detail = data?.projection;
  const scope = t(projection.scope ? `projection.scope.${projection.scope}` : "") || t("projection.scope.full_time");
  const title = `${highlightLabel(projection, t) || detail?.label || t("modal.title")} · ${scope}`;

  return (
    <div className="lightbox-backdrop" role="dialog" aria-modal="true" aria-label={title} onClick={onClose}>
      <div className="lightbox-frame projection-frame" onClick={(e) => e.stopPropagation()}>
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
          <div className="projection-detail">
            <div className="projection-detail-head">
              <span
                className={"badge" + (detail.provenance === "estimated" ? " amber" : " green")}
                title={detail.provenance === "estimated" ? t("projection.provenanceEstimated") : t("projection.provenanceExact")}
              >
                {detail.provenance === "estimated" ? t("projection.estimated") : t("projection.exact")}
              </span>
              {hasRefund(detail.outcomes) && <span className="badge">{t("projection.refunds")}</span>}
              <span className="muted">{detail.method}</span>
            </div>

            <h4 className="projection-detail-title">{t("modal.outcomes")}</h4>
            <OutcomesBars outcomes={detail.outcomes} t={t} pct={pct} />

            {detail.factors ? (
              <>
                <h4 className="projection-detail-title">{t("modal.whereFrom")}</h4>
                <FactorTable detail={detail} t={t} pct={pct} />
              </>
            ) : (
              <>
                <h4 className="projection-detail-title">
                  {t("modal.scorelines")}
                  <span className="muted">
                    {" "}
                    — {t("modal.gridCells", { successful: detail.successful_cells, grid: detail.grid_cells })}
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