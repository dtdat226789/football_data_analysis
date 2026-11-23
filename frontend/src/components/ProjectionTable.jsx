import { useMemo, useState } from "react";

import { useFormatters } from "../i18n/useFormatters.js";
import { highlightLabel } from "./ProjectionHighlights.jsx";

/** Display order, then label. Anything unlisted sorts to the end. */
const FAMILY_ORDER = [
  "outcome",
  "paired_outcome",
  "goal_totals",
  "both_score",
  "goal_margin",
  "half_full",
  "team_total",
  "exact_score",
];

const FAMILY_KEY = {
  outcome: "projection.family.outcome",
  paired_outcome: "projection.family.paired_outcome",
  goal_totals: "projection.family.goal_totals",
  both_score: "projection.family.both_score",
  goal_margin: "projection.family.goal_margin",
  half_full: "projection.family.half_full",
  team_total: "projection.family.team_total",
  exact_score: "projection.family.exact_score",
};

const SCOPE_KEY = {
  full_time: "projection.scope.full_time",
  half_time: "projection.scope.half_time",
  half_to_full: "projection.scope.half_to_full",
};

const FILTERS = [
  { id: "all", key: "projection.filter.all" },
  { id: "full_time", key: "projection.filter.full_time" },
  { id: "half_time", key: "projection.filter.half_time" },
  { id: "estimated", key: "projection.filter.estimated" },
];

/** Sort a projection row within its family: by line, then by probability. */
function compareRows(a, b) {
  const lineA = typeof a.line === "number" ? a.line : -Infinity;
  const lineB = typeof b.line === "number" ? b.line : -Infinity;
  if (lineA !== lineB) return lineA - lineB;
  return b.probability - a.probability;
}

/**
 * The full derived projection menu for a fixture.
 *
 * Rows arrive from the API already grouped-ready and already tagged: each one
 * carries `provenance` ("exact" for numbers read off the model's own goal
 * distribution, "estimated" for the half-time projections that need a split the feed
 * does not publish) and `promotable` (whether the model was confident enough to
 * put it in the highlight row). The "Featured" marker surfaces the latter so a
 * reader can see which of these are driving the summary.
 *
 * Goal-margin rows carry `refund`, so a line that can refund is honest about it
 * instead of showing a single misleading number.
 *
 * Passing `onSelect` makes every row openable: the row itself stays a real
 * `<tr>` and the clickable control is a button in the first cell, so keyboard
 * order, row semantics and any future row-level selection keep working instead
 * of the whole row becoming a div.
 */
/**
 * @param {object} props
 * @param {Record<string, any>[]} [props.projections] Absent or not an array renders nothing.
 * @param {Record<string, any>[]} [props.highlights] Projections already chosen elsewhere.
 * @param {(row: Record<string, any>) => void} [props.onSelect] Omit it for a read-only
 *   table: the clickable column is not rendered at all.
 */
export default function ProjectionTable({ projections, highlights = [], onSelect }) {
  const { t, pct } = useFormatters();
  const [filter, setFilter] = useState("all");
  const featured = useMemo(
    () => new Set(highlights.map((m) => m && m.key).filter(Boolean)),
    [highlights],
  );

  const grouped = useMemo(() => {
    const rows = Array.isArray(projections) ? projections.filter((m) => m && typeof m.probability === "number") : [];
    const filtered = rows.filter((m) => {
      if (filter === "estimated") return m.provenance === "estimated";
      if (filter === "all") return true;
      return m.scope === filter;
    });
    const buckets = new Map();
    for (const row of filtered) {
      if (!buckets.has(row.family)) buckets.set(row.family, []);
      buckets.get(row.family).push(row);
    }
    return [...buckets.entries()]
      .sort((a, b) => {
        const rankA = FAMILY_ORDER.indexOf(a[0]);
        const rankB = FAMILY_ORDER.indexOf(b[0]);
        return (rankA < 0 ? 99 : rankA) - (rankB < 0 ? 99 : rankB) || a[0].localeCompare(b[0]);
      })
      .map(([family, familyRows]) => [family, familyRows.slice().sort(compareRows)]);
  }, [projections, filter]);

  if (!Array.isArray(projections) || !projections.length) return null;

  const estimated = projections.filter((m) => m && m.provenance === "estimated").length;

  return (
    <section className="card">
      <h3 style={{ marginTop: 0, display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
        {t("projection.title")}
        <span className="muted" style={{ fontSize: 13, fontWeight: 400 }}>
          {t("projection.derived", { n: projections.length })}
        </span>
        {estimated > 0 && (
          <span className="badge amber" title={t("projection.estimatedBadgeTitle")}>
            {t("projection.estimatedCount", { n: estimated })}
          </span>
        )}
      </h3>

      <div className="projection-filters">
        {FILTERS.map((option) => (
          <button
            key={option.id}
            className={"preset" + (filter === option.id ? " on" : "")}
            onClick={() => setFilter(option.id)}
            aria-pressed={filter === option.id}
          >
            {t(option.key)}
          </button>
        ))}
      </div>

      {grouped.length === 0 ? (
        <p className="muted">{t("projection.noMatch")}</p>
      ) : (
        grouped.map(([family, rows]) => (
          <div key={family} className="projection-group">
            <h4>{t(FAMILY_KEY[family] ?? "") || family}</h4>
            <table className="data">
              <thead>
                <tr>
                  <th>{t("projection.col.projection")}</th>
                  <th>{t("projection.col.scope")}</th>
                  <th>{t("projection.col.source")}</th>
                  <th className="num">{t("projection.col.probability")}</th>
                </tr>
              </thead>
              <tbody>
                {rows.map((row) => (
                  <tr key={row.key} className={featured.has(row.key) ? "featured" : ""}>
                    <td>
                      {onSelect ? (
                        <button
                          type="button"
                          className="projection-open"
                          onClick={() => onSelect(row)}
                          title={t("projection.howCounted", { label: highlightLabel(row, t) })}
                        >
                          {highlightLabel(row, t)}
                        </button>
                      ) : (
                        highlightLabel(row, t)
                      )}
                      {featured.has(row.key) && <span className="projection-flag">{t("projection.featured")}</span>}
                    </td>
                    <td className="muted">{t(SCOPE_KEY[row.scope] ?? "") || row.scope}</td>
                    <td>
                      <span
                        className={"badge" + (row.provenance === "estimated" ? " amber" : " green")}
                        title={
                          row.provenance === "estimated"
                            ? t("projection.provenanceEstimated")
                            : t("projection.provenanceExact")
                        }
                      >
                        {row.provenance === "estimated" ? t("projection.estimated") : t("projection.exact")}
                      </span>
                    </td>
                    <td className="num">
                      {pct(row.probability)}
                      {typeof row.refund === "number" && row.refund > 0 && (
                        <span className="muted projection-refund">
                          {" "}
                          · {t("projection.refund", { pct: pct(row.refund) })}
                        </span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))
      )}
    </section>
  );
}