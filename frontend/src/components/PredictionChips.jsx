import { useFormatters } from "../i18n/useFormatters.js";

/**
 * Accept keys with underscore (pruned feed) or dot (raw dc_v2 calibrated).
 */
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

const SCOPE_KEY = {
  full_time: "market.scope.ftShort",
  half_time: "market.scope.htShort",
  half_to_full: "market.scope.htftShort",
};

/**
 * Localised label for one market chip.
 *
 * The backend serves markets with structured fields (family/selection/line),
 * so the label is rebuilt from those rather than translated label strings.
 * English renders the shorthand the reader is looking for (O1.5, X, BTTS, 1/1)
 * and Vietnamese expands each to a readable phrase, keeping the number format
 * locale-aware. Falls back to the raw label for shapes it does not recognise.
 */
export function chipLabel(market, t, line) {
  const family = market.family;
  const selection = market.selection;
  if (family === "result") {
    if (selection === "home" || selection === "draw" || selection === "away") {
      return t(`chip.result.${selection}`);
    }
  }
  if (family === "double_chance") {
    if (selection === "home_or_draw" || selection === "draw_or_away" || selection === "home_or_away") {
      return t(`chip.dc.${selection}`);
    }
  }
  if (family === "btts") {
    if (selection === "yes" || selection === "no" || selection === "short") {
      return t(`chip.btts.${selection}`);
    }
  }
  if (family === "totals") {
    if (selection === "over" || selection === "under") {
      const key = selection === "over" ? "chip.totals.over" : "chip.totals.under";
      return t(key, { line: line(market.line) });
    }
  }
  if (family === "team_total") {
    if (selection === "home" || selection === "away") {
      // The over/under side is encoded in the market key, e.g. ".over_1.5".
      const over = String(market.key || "").includes(".over_");
      const side = t(selection === "home" ? "chip.side.home" : "chip.side.away");
      const key = over ? "chip.teamTotal.over" : "chip.teamTotal.under";
      return t(key, { side, line: line(market.line) });
    }
  }
  if (family === "asian_handicap") {
    if (selection === "home" || selection === "away") {
      // The stored line is always the home side's; the away side is its negation.
      const raw = selection === "away" ? -market.line : market.line;
      const sign = raw < 0 ? "-" : "+";
      const side = t(selection === "home" ? "chip.side.home" : "chip.side.away");
      return t("chip.handicap", { side, line: `${sign}${line(Math.abs(raw))}` });
    }
  }
  if (family === "ht_ft") {
    const [ht, ft] = String(selection || "").split("_");
    const side = (s) =>
      t(s === "home" ? "chip.ht.home" : s === "away" ? "chip.ht.away" : s === "draw" ? "chip.ht.draw" : "");
    return t("chip.htft", { ht: side(ht), ft: side(ft) });
  }
  if (family === "correct_score") {
    // The scoreline lives in the key tail ("2-1"); `selection` is just a
    // positional marker on these rows.
    const tail = String(market.key || "").split(".").pop();
    const score = /^\d+-\d+$/.test(tail) ? tail : market.label;
    return t("chip.correctScore", { score });
  }
  return market.label || market.key || "";
}

/** One-line explanation of where a derived number came from. */
function marketTitle(market, t, line, pct0) {
  const scope = t(SCOPE_KEY[market.scope] ?? "") || market.scope;
  const parts = [`${chipLabel(market, t, line)} · ${scope}`];
  if (market.provenance === "modelled") {
    parts.push(t("market.titleAssumed"));
  } else {
    parts.push(t("market.titleModel"));
  }
  if (typeof market.push === "number" && market.push > 0) {
    parts.push(t("market.push", { pct: pct0(market.push) }));
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
/**
 * @param {object} props
 * @param {Record<string, any>} [props.predictions]
 * @param {boolean} [props.compact]
 * @param {string | number} [props.confidence]
 * @param {string} [props.dataThrough]
 * @param {(market: object) => void} [props.onSelect] Supplied only when the chips
 *   are interactive; without it the row is read-only.
 */
export default function PredictionChips({
  predictions,
  compact = false,
  confidence,
  dataThrough,
  onSelect,
}) {
  const { t, pct0, line } = useFormatters();
  const p = predictions || {};
  const selected = Array.isArray(p.selected) ? p.selected.filter((m) => m && typeof m.probability === "number") : null;
  const dynamic = selected && selected.length > 0;
  // Only a derived chip carries a market key the backend can explain, so the
  // legacy fixed set stays inert even when onSelect is supplied.
  const clickable = typeof onSelect === "function" && dynamic;

  const chips = dynamic
    ? selected.map((market) => ({
        key: market.key || market.label,
        label: chipLabel(market, t, line),
        value: pct0(market.probability),
        title: marketTitle(market, t, line, pct0),
        market,
        cls: [chipTone(market.probability), market.provenance === "modelled" ? "chip-assumed" : ""]
          .filter(Boolean)
          .join(" "),
      }))
    : [
        { key: "home", label: chipLabel({ family: "result", selection: "home" }, t, line), value: pct0(value(p, "home")), title: t("pred.homeTitle"), cls: strength(value(p, "home")) },
        { key: "draw", label: chipLabel({ family: "result", selection: "draw" }, t, line), value: "—", title: t("pred.drawTitle"), cls: "" },
        { key: "away", label: chipLabel({ family: "result", selection: "away" }, t, line), value: pct0(value(p, "away")), title: t("pred.awayTitle"), cls: strength(value(p, "away")) },
        { key: "btts", label: chipLabel({ family: "btts", selection: "short" }, t, line), value: pct0(value(p, "btts_yes")), title: t("pred.bttsTitle"), cls: strength(value(p, "btts_yes")) },
        { key: "o15", label: chipLabel({ family: "totals", selection: "over", line: 1.5 }, t, line), value: pct0(value(p, "over_1_5")), title: t("pred.o15Title"), cls: strength(value(p, "over_1_5")) },
        { key: "o25", label: chipLabel({ family: "totals", selection: "over", line: 2.5 }, t, line), value: pct0(value(p, "over_2_5")), title: t("pred.o25Title"), cls: strength(value(p, "over_2_5")) },
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
          {typeof confidence === "number" && <span>{t("pred.conf")} {pct0(confidence)}</span>}
          {dataThrough && <span>{t("pred.asOf")} {dataThrough}</span>}
        </span>
      )}
    </span>
  );
}