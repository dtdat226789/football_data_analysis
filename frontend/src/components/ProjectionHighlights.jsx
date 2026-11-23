import { useFormatters } from "../i18n/useFormatters.js";

/** Read a prediction field by either the underscored feed key or the dotted raw key. */
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

/** Highlights are already filtered to a decisive band, so green means surer. */
function tone(v) {
  if (typeof v !== "number") return "";
  return v >= 0.75 ? "chip-strong" : "chip-mid";
}

const SCOPE_KEY = {
  full_time: "projection.scope.ftShort",
  half_time: "projection.scope.htShort",
  half_to_full: "projection.scope.htftShort",
};

/** Probability of a goal-total line, expressed as a goal count. */
function goalCount(line, under) {
  return under ? Math.floor(line) : Math.floor(line) + 1;
}

/** Plain-language phrase for a goal-margin line, as quoted for one side. */
function marginPhrase(line, t) {
  if (!Number.isFinite(line)) return "";
  if (line <= -1.5) return t("highlight.margin.loseByOne");
  if (line <= -1.25) return t("highlight.margin.notLoseByTwo");
  if (line <= -0.25) return t("highlight.margin.drawOrWin");
  if (line <= 0.25) return t("highlight.margin.win");
  if (line < 1.0) return t("highlight.margin.winByOne");
  return t("highlight.margin.winByTwo");
}

/**
 * Localised label for one projection highlight.
 *
 * The backend serves structured fields (family/selection/line), so the label is
 * rebuilt from them rather than translated label strings. Families whose plain
 * wording lives on the row itself (goal margins, half/full, exact score) use
 * that wording directly.
 */
export function highlightLabel(projection, t) {
  const family = projection.family;
  const selection = projection.selection;
  if (family === "outcome") {
    if (["home", "draw", "away"].includes(selection)) {
      return t(`highlight.outcome.${selection}`);
    }
  }
  if (family === "paired_outcome") {
    if (["home_or_draw", "draw_or_away", "home_or_away"].includes(selection)) {
      return t(`highlight.paired.${selection}`);
    }
  }
  if (family === "both_score") {
    if (["yes", "no", "short"].includes(selection)) {
      return t(`highlight.both.${selection}`);
    }
  }
  if (family === "goal_totals") {
    if (selection === "over" || selection === "under") {
      const under = selection === "under";
      return t(under ? "highlight.goalTotal.under" : "highlight.goalTotal.over", {
        n: goalCount(projection.line, under),
      });
    }
  }
  if (family === "team_total") {
    if (selection === "home" || selection === "away") {
      const under = String(projection.key || "").includes(".under_");
      const side = t(selection === "home" ? "highlight.side.home" : "highlight.side.away");
      return t(under ? "highlight.teamTotal.under" : "highlight.teamTotal.over", {
        side,
        n: goalCount(projection.line, under),
      });
    }
  }
  if (family === "goal_margin") {
    if (selection === "home" || selection === "away") {
      const line = selection === "away" ? -projection.line : projection.line;
      const side = t(selection === "home" ? "highlight.side.home" : "highlight.side.away");
      const phrase = marginPhrase(line, t);
      if (phrase) return t("highlight.margin.line", { side, phrase });
    }
  }
  if (family === "half_full") {
    const [ht, ft] = String(selection || "").split("_");
    if (ht && ft) {
      return t("highlight.htft", {
        ht: t(`highlight.outcome.${ht}`),
        ft: t(`highlight.outcome.${ft}`),
      });
    }
  }
  return projection.label || projection.key || "";
}

/** One-line explanation of where a derived number came from. */
function highlightTitle(projection, t, pct0) {
  const scope = t(SCOPE_KEY[projection.scope] ?? "") || projection.scope;
  const parts = [`${highlightLabel(projection, t)} · ${scope}`];
  parts.push(
    projection.provenance === "estimated"
      ? t("projection.titleEstimated")
      : t("projection.titleExact"),
  );
  if (typeof projection.refund === "number" && projection.refund > 0) {
    parts.push(t("highlight.refund", { pct: pct0(projection.refund) }));
  }
  return parts.join(" — ");
}

/**
 * A fixture's most decisive derived projections, alongside model confidence and
 * data freshness.
 *
 * The preferred input is the pruned `predictions` object from /api/v1/fixtures,
 * which carries a `highlights` array chosen by the model's own confidence. A
 * payload without it falls back to the fixed outcome/total set from the plain
 * summary, so the row still renders while the API rolls forward.
 *
 * Supplying `onSelect` makes each highlight a button that hands its row back to
 * the caller; without it the row is read-only.
 */
/**
 * @param {object} props
 * @param {Record<string, any>} [props.predictions]
 * @param {boolean} [props.compact]
 * @param {string | number} [props.confidence]
 * @param {string} [props.dataThrough]
 * @param {(projection: object) => void} [props.onSelect]
 */
export default function ProjectionHighlights({
  predictions,
  compact = false,
  confidence,
  dataThrough,
  onSelect,
}) {
  const { t, pct0 } = useFormatters();
  const p = predictions || {};
  const highlights = Array.isArray(p.highlights)
    ? p.highlights.filter((row) => row && typeof row.probability === "number")
    : null;
  const dynamic = Boolean(highlights && highlights.length);
  const clickable = typeof onSelect === "function" && dynamic;

  const chips = dynamic
    ? highlights.map((projection) => ({
        key: projection.key || projection.label,
        label: highlightLabel(projection, t),
        value: pct0(projection.probability),
        title: highlightTitle(projection, t, pct0),
        projection,
        cls: [
          tone(projection.probability),
          projection.provenance === "estimated" ? "chip-assumed" : "",
        ]
          .filter(Boolean)
          .join(" "),
      }))
    : [
        { key: "home", label: highlightLabel({ family: "outcome", selection: "home" }, t), value: pct0(value(p, "home")), title: t("pred.homeTitle"), cls: strength(value(p, "home")) },
        { key: "draw", label: highlightLabel({ family: "outcome", selection: "draw" }, t), value: pct0(value(p, "draw")), title: t("pred.drawTitle"), cls: strength(value(p, "draw")) },
        { key: "away", label: highlightLabel({ family: "outcome", selection: "away" }, t), value: pct0(value(p, "away")), title: t("pred.awayTitle"), cls: strength(value(p, "away")) },
        { key: "o15", label: highlightLabel({ family: "goal_totals", selection: "over", line: 1.5 }, t), value: pct0(value(p, "over_1_5")), title: t("pred.o15Title"), cls: strength(value(p, "over_1_5")) },
        { key: "o25", label: highlightLabel({ family: "goal_totals", selection: "over", line: 2.5 }, t), value: pct0(value(p, "over_2_5")), title: t("pred.o25Title"), cls: strength(value(p, "over_2_5")) },
      ];

  const showMeta = typeof confidence === "number" || Boolean(dataThrough);
  return (
    <span className={"pred-chips" + (compact ? " compact" : "")}>
      {chips.map((c) =>
        clickable ? (
          <button
            key={c.key}
            type="button"
            className={"pred-chip pred-chip-btn " + c.cls}
            title={c.title}
            onClick={() => onSelect(c.projection)}
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
