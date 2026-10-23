import { useMemo, useState } from "react";

import { useFormatters } from "../i18n/useFormatters.js";

/** Display order, then label. Anything unlisted sorts to the end. */
const FAMILY_ORDER = [
  "result",
  "double_chance",
  "totals",
  "btts",
  "asian_handicap",
  "ht_ft",
  "team_total",
  "correct_score",
];

const FAMILY_KEY = {
  result: "market.family.result",
  double_chance: "market.family.double_chance",
  totals: "market.family.totals",
  btts: "market.family.btts",
  asian_handicap: "market.family.asian_handicap",
  ht_ft: "market.family.ht_ft",
  team_total: "market.family.team_total",
  correct_score: "market.family.correct_score",
};

const SCOPE_KEY = {
  full_time: "market.scope.full_time",
  half_time: "market.scope.half_time",
  half_to_full: "market.scope.half_to_full",
};

const FILTERS = [
  { id: "all", key: "market.filter.all" },
  { id: "full_time", key: "market.filter.full_time" },
  { id: "half_time", key: "market.filter.half_time" },
  { id: "assumed", key: "market.filter.assumed" },
];

/** Sort a market row within its family: by line, then by probability. */
function compareRows(a, b) {
  const lineA = typeof a.line === "number" ? a.line : -Infinity;
  const lineB = typeof b.line === "number" ? b.line : -Infinity;
  if (lineA !== lineB) return lineA - lineB;
  return b.probability - a.probability;
}

/**
 * The full derived market menu for a fixture.
 *
 * Rows arrive from the API already grouped-ready and already tagged: each one
 * carries `provenance` ("model" for numbers read off the model's own goal
 * distribution, "modelled" for the half-time markets that need a split the feed
 * does not publish) and `promotable` (whether the model was confident enough to
 * put it in the chip row). The "Featured" marker surfaces the latter so a
 * reader can see which of these are driving the summary.
 *
 * Asian handicap rows carry `push`, so a line that can refund is honest about it
 * instead of showing a single misleading number.
 *
 * Passing `onSelect` makes every row openable: the row itself stays a real
 * `<tr>` and the clickable control is a button in the first cell, so keyboard
 * order, row semantics and any future row-level selection keep working instead
 * of the whole row becoming a div.
 */
/**
 * @param {object} props
 * @param {Record<string, any>[]} [props.markets] Absent or not an array renders nothing.
 * @param {Record<string, any>[]} [props.selected] Markets already chosen elsewhere.
 * @param {(row: Record<string, any>) => void} [props.onSelect] Omit it for a read-only
 *   table: the clickable column is not rendered at all.
 */
export default function MarketTable({ markets, selected = [], onSelect }) {
  const { t, pct } = useFormatters();
  const [filter, setFilter] = useState("all");
  const featured = useMemo(
    () => new Set(selected.map((m) => m && m.key).filter(Boolean)),
    [selected],
  );

  const grouped = useMemo(() => {
    const rows = Array.isArray(markets) ? markets.filter((m) => m && typeof m.probability === "number") : [];
    const filtered = rows.filter((m) => {
      if (filter === "assumed") return m.provenance === "modelled";
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
  }, [markets, filter]);

  if (!Array.isArray(markets) || !markets.length) return null;

  const assumed = markets.filter((m) => m && m.provenance === "modelled").length;

  return (
    <section className="card">
      <h3 style={{ marginTop: 0, display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
        {t("market.title")}
        <span className="muted" style={{ fontSize: 13, fontWeight: 400 }}>
          {t("market.derived", { n: markets.length })}
        </span>
        {assumed > 0 && (
          <span className="badge amber" title={t("market.assumedBadgeTitle")}>
            {t("market.assumedCount", { n: assumed })}
          </span>
        )}
      </h3>

      <div className="market-filters">
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
        <p className="muted">{t("market.noMatch")}</p>
      ) : (
        grouped.map(([family, rows]) => (
          <div key={family} className="market-group">
            <h4>{t(FAMILY_KEY[family] ?? "") || family}</h4>
            <table className="data">
              <thead>
                <tr>
                  <th>{t("market.col.market")}</th>
                  <th>{t("market.col.scope")}</th>
                  <th>{t("market.col.source")}</th>
                  <th className="num">{t("market.col.probability")}</th>
                </tr>
              </thead>
              <tbody>
                {rows.map((row) => (
                  <tr key={row.key} className={featured.has(row.key) ? "featured" : ""}>
                    <td>
                      {onSelect ? (
                        <button
                          type="button"
                          className="market-open"
                          onClick={() => onSelect(row)}
                          title={t("market.howSettles", { label: row.label })}
                        >
                          {row.label}
                        </button>
                      ) : (
                        row.label
                      )}
                      {featured.has(row.key) && <span className="market-flag">{t("market.featured")}</span>}
                    </td>
                    <td className="muted">{t(SCOPE_KEY[row.scope] ?? "") || row.scope}</td>
                    <td>
                      <span
                        className={"badge" + (row.provenance === "modelled" ? " amber" : " green")}
                        title={
                          row.provenance === "modelled"
                            ? t("market.provenanceAssumed")
                            : t("market.provenanceModel")
                        }
                      >
                        {row.provenance === "modelled" ? t("market.assumed") : t("market.model")}
                      </span>
                    </td>
                    <td className="num">
                      {pct(row.probability)}
                      {typeof row.push === "number" && row.push > 0 && (
                        <span className="muted market-push">
                          {" "}
                          · {t("market.push", { pct: pct(row.push) })}
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