function pct(v) {
  return typeof v === "number" ? `${(v * 100).toFixed(0)}%` : "—";
}

/** Accept keys with underscore (pruned feed) or dot (raw dc_v2 calibrated). */
function value(p, underscored) {
  const raw = p[underscored];
  if (typeof raw === "number") return raw;
  return p[underscored.replace(/_/g, ".")];
}

/** Confidence buckets: strong >= 60%, medium >= 45%, otherwise weak. */
function strength(v) {
  if (typeof v !== "number") return "";
  if (v >= 0.6) return "chip-strong";
  if (v >= 0.45) return "chip-mid";
  return "chip-weak";
}

/**
 * Renders dc_v2 model prediction chips. Input is either the pruned
 * `predictions` object from /api/v1/fixtures (home, away, btts_yes,
 * over_1_5, over_2_5) or the raw calibrated block (home, away, btts_yes,
 * over_1.5, over_2.5, ...).
 *
 * Optionally accepts the fixture's `confidence` and `data_through` to render
 * a "conf … · as of …" meta line alongside the chips.
 */
export default function PredictionChips({ predictions, compact = false, confidence, dataThrough }) {
  const p = predictions || {};
  const chips = [
    { label: "1", value: pct(value(p, "home")), title: "Home win probability", cls: strength(value(p, "home")) },
    { label: "X", value: "—", title: "Draw probability (not modelled)", cls: "" },
    { label: "2", value: pct(value(p, "away")), title: "Away win probability", cls: strength(value(p, "away")) },
    { label: "BTTS", value: pct(value(p, "btts_yes")), title: "Both teams to score", cls: strength(value(p, "btts_yes")) },
    { label: "O1.5", value: pct(value(p, "over_1_5")), title: "Over 1.5 goals", cls: strength(value(p, "over_1_5")) },
    { label: "O2.5", value: pct(value(p, "over_2_5")), title: "Over 2.5 goals", cls: strength(value(p, "over_2_5")) },
  ];
  const showMeta = typeof confidence === "number" || dataThrough;
  return (
    <span className={"pred-chips" + (compact ? " compact" : "")}>
      {chips.map((c) => (
        <span key={c.label} className={"pred-chip " + c.cls} title={c.title}>
          {c.label} <b>{c.value}</b>
        </span>
      ))}
      {showMeta && (
        <span className="pred-meta">
          {typeof confidence === "number" && <span>conf {pct(confidence)}</span>}
          {dataThrough && <span>as of {dataThrough}</span>}
        </span>
      )}
    </span>
  );
}