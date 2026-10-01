import { useMemo, useState } from "react";

function pct(v) {
  return typeof v === "number" ? `${(v * 100).toFixed(1)}%` : "—";
}

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

const FAMILY_LABEL = {
  result: "Result",
  double_chance: "Double chance",
  totals: "Goals (over/under)",
  btts: "Both teams to score",
  asian_handicap: "Asian handicap",
  ht_ft: "Half time / full time",
  team_total: "Team totals",
  correct_score: "Correct score",
};

const SCOPE_LABEL = {
  full_time: "Full time",
  half_time: "Half time",
  half_to_full: "HT / FT",
};

const FILTERS = [
  { id: "all", label: "All" },
  { id: "full_time", label: "Full time" },
  { id: "half_time", label: "Half time" },
  { id: "assumed", label: "Assumed only" },
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
export default function MarketTable({ markets, selected = [], onSelect }) {
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
        Markets
        <span className="muted" style={{ fontSize: 13, fontWeight: 400 }}>
          {markets.length} derived
        </span>
        {assumed > 0 && (
          <span className="badge amber" title="dc_v2 does not publish a half-time goal split; these assume it is proportional to the full-time one">
            {assumed} assumed
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
            {option.label}
          </button>
        ))}
      </div>

      {grouped.length === 0 ? (
        <p className="muted">No markets match this filter.</p>
      ) : (
        grouped.map(([family, rows]) => (
          <div key={family} className="market-group">
            <h4>{FAMILY_LABEL[family] || family}</h4>
            <table className="data">
              <thead>
                <tr>
                  <th>Market</th>
                  <th>Scope</th>
                  <th>Source</th>
                  <th className="num">Probability</th>
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
                          title={`How ${row.label} settles`}
                        >
                          {row.label}
                        </button>
                      ) : (
                        row.label
                      )}
                      {featured.has(row.key) && <span className="market-flag">featured</span>}
                    </td>
                    <td className="muted">{SCOPE_LABEL[row.scope] || row.scope}</td>
                    <td>
                      <span
                        className={"badge" + (row.provenance === "modelled" ? " amber" : " green")}
                        title={
                          row.provenance === "modelled"
                            ? "Assumed — the model does not publish the half-time goal split, so this is derived, not published"
                            : "From the model's goal distribution"
                        }
                      >
                        {row.provenance === "modelled" ? "assumed" : "model"}
                      </span>
                    </td>
                    <td className="num">
                      {pct(row.probability)}
                      {typeof row.push === "number" && row.push > 0 && (
                        <span className="muted market-push"> · {pct(row.push)} push</span>
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
