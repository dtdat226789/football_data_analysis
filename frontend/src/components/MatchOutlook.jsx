import { useFormatters } from "../i18n/useFormatters.js";

/**
 * Read a prediction field by either the pruned feed's underscore key or the
 * raw dc_v2 block's dotted key.
 */
function value(predictions, key) {
  const source = predictions || {};
  const candidates = [key, key.replace(/_([^_]*)$/, ".$1"), key.replace(/_/g, ".")];
  for (const candidate of candidates) {
    if (typeof source[candidate] === "number") return source[candidate];
  }
  return null;
}

/** Confidence buckets: strong >= 60%, medium >= 45%, otherwise weak. */
function strength(v) {
  if (typeof v !== "number") return "";
  if (v >= 0.6) return "chip-strong";
  if (v >= 0.45) return "chip-mid";
  return "chip-weak";
}

const TOTALS = [
  { key: "over_1_5", goals: 2 },
  { key: "over_2_5", goals: 3 },
];

/**
 * A fixture's plain-language outlook: the chance the match reaches two or three
 * goals, alongside the model's confidence and how fresh its data is.
 *
 * The numbers are the model's own goal distribution, presented as football
 * statistics.
 */
/**
 * @param {object} props
 * @param {Record<string, any>} [props.predictions]
 * @param {boolean} [props.compact]
 * @param {string | number} [props.confidence]
 * @param {string} [props.dataThrough]
 */
export default function MatchOutlook({ predictions, compact = false, confidence, dataThrough }) {
  const { t, pct0 } = useFormatters();
  const chips = TOTALS.map((row) => ({ ...row, probability: value(predictions, row.key) })).filter(
    (row) => typeof row.probability === "number",
  );
  const conf =
    typeof confidence === "number" ? confidence : value(predictions, "confidence");
  const through = dataThrough || predictions?.data_through;
  const showMeta = typeof conf === "number" || Boolean(through);

  if (!chips.length && !showMeta) return null;

  return (
    <span className={"pred-chips" + (compact ? " compact" : "")}>
      {chips.map((chip) => (
        <span
          key={chip.key}
          className={"pred-chip " + strength(chip.probability)}
          title={t("outlook.goalsTitle", { n: chip.goals })}
        >
          {t("outlook.goalsPlus", { n: chip.goals })} <b>{pct0(chip.probability)}</b>
        </span>
      ))}
      {showMeta && (
        <span className="pred-meta">
          {typeof conf === "number" && (
            <span>{t("pred.confModel")} {pct0(conf)}</span>
          )}
          {through && <span>{t("pred.asOf")} {through}</span>}
        </span>
      )}
    </span>
  );
}
