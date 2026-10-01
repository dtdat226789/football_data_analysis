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
 * Tone for a derived market chip. Only markets the backend considered decisive
 * ever reach here, so the whole range is 60-95% and the mid/strong split is
 * moved up: within that band, greener means the model is surer.
 */
function chipTone(v) {
  if (typeof v !== "number") return "";
  return v >= 0.75 ? "chip-strong" : "chip-mid";
}

const SCOPE_TEXT = {
  full_time: "full time",
  half_time: "half time",
  half_to_full: "half time / full time",
};

/** One-line explanation of where a derived number came from. */
function marketTitle(market) {
  const scope = SCOPE_TEXT[market.scope] || market.scope;
  const parts = [`${market.label} · ${scope}`];
  if (market.provenance === "modelled") {
    parts.push("assumed: the model does not publish this split, so it is derived");
  } else {
    parts.push("from the model's goal distribution");
  }
  if (typeof market.push === "number" && market.push > 0) {
    parts.push(`${pct(market.push)} push`);
  }
  return parts.join(" — ");
}

/**
 * Renders dc_v2 model prediction chips.
 *
 * Preferred input is the pruned `predictions` object from /api/v1/fixtures,
 * which carries a `selected` array of markets the model is confident about.
 * Those are rendered as-is, so the chip row follows the model's own read
 * instead of a fixed list — a decisive O2.5 appears, a coin-flip market does
 * not, and the draw shows up on the rare fixture the model actually rates a
 * draw at 60% or better.
 *
 * Older payloads with no `selected` fall back to the fixed home/away/BTTS/O1.5/
 * O2.5 set read off the top-level keys, so nothing breaks while the backend is
 * being rolled forward.
 *
 * Optionally accepts the fixture's `confidence` and `data_through` to render
 * a "conf … · as of …" meta line alongside the chips.
 *
 * Passing `onSelect` makes each derived chip a button that hands its market row
 * back to the caller, so the chip row can open that market's explanation. Left
 * out, the chips stay inert spans and the markup is unchanged — the list views
 * render them as a summary, not as a control.
 */
export default function PredictionChips({
  predictions,
  compact = false,
  confidence,
  dataThrough,
  onSelect,
}) {
  const p = predictions || {};
  const selected = Array.isArray(p.selected) ? p.selected.filter((m) => m && typeof m.probability === "number") : null;
  const dynamic = selected && selected.length > 0;
  // Only a derived chip carries a market key the backend can explain, so the
  // legacy fixed set stays inert even when onSelect is supplied.
  const clickable = typeof onSelect === "function" && dynamic;

  const chips = dynamic
    ? selected.map((market) => ({
        key: market.key || market.label,
        label: market.label,
        value: pct(market.probability),
        title: marketTitle(market),
        market,
        cls: [chipTone(market.probability), market.provenance === "modelled" ? "chip-assumed" : ""]
          .filter(Boolean)
          .join(" "),
      }))
    : [
        { key: "home", label: "1", value: pct(value(p, "home")), title: "Home win probability", cls: strength(value(p, "home")) },
        { key: "draw", label: "X", value: "—", title: "Draw probability (not modelled)", cls: "" },
        { key: "away", label: "2", value: pct(value(p, "away")), title: "Away win probability", cls: strength(value(p, "away")) },
        { key: "btts", label: "BTTS", value: pct(value(p, "btts_yes")), title: "Both teams to score", cls: strength(value(p, "btts_yes")) },
        { key: "o15", label: "O1.5", value: pct(value(p, "over_1_5")), title: "Over 1.5 goals", cls: strength(value(p, "over_1_5")) },
        { key: "o25", label: "O2.5", value: pct(value(p, "over_2_5")), title: "Over 2.5 goals", cls: strength(value(p, "over_2_5")) },
      ];

  const showMeta = typeof confidence === "number" || dataThrough;
  return (
    <span className={"pred-chips" + (compact ? " compact" : "")}>
      {chips.map((c) =>
        clickable ? (
          <button
            key={c.key}
            type="button"
            className={"pred-chip pred-chip-btn " + c.cls}
            title={c.title}
            onClick={() => onSelect(c.market)}
          >
            {c.label} <b>{c.value}</b>
          </button>
        ) : (
          <span key={c.key} className={"pred-chip " + c.cls} title={c.title}>
            {c.label} <b>{c.value}</b>
          </span>
        ),
      )}
      {showMeta && (
        <span className="pred-meta">
          {typeof confidence === "number" && <span>conf {pct(confidence)}</span>}
          {dataThrough && <span>as of {dataThrough}</span>}
        </span>
      )}
    </span>
  );
}
