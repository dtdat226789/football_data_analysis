import { useFormatters } from "../i18n/useFormatters.js";

/**
 * A run of W/D/L pills. The letters stay W/D/L in both languages — they are
 * the notation the scorelines beside them use, and translating them to
 * Thắng/Hòa/Thua would make the pill longer than the match it describes. The
 * accessible name is spelled out instead, so a screen reader announces the
 * word rather than the letter.
 *
 * @param {{ results?: Record<string, any>[] }} props
 *   An absent or empty list renders an em dash.
 */
export function FormPills({ results }) {
  const { t } = useFormatters();
  if (!results || results.length === 0) return <span className="muted">—</span>;
  return (
    <span className="formline">
      {results.map((r, i) => (
        <span
          key={i}
          className={`pill ${r.team_result}`}
          title={`${r.home_team} ${r.home_score}-${r.away_score} ${r.away_team}`}
          aria-label={`${resultLabel(r.team_result, t)}: ${r.home_team} ${r.home_score}-${r.away_score} ${r.away_team}`}
        >
          {r.team_result}
        </span>
      ))}
    </span>
  );
}

function resultLabel(result, t) {
  if (result === "win") return t("page.team.wdl.won");
  if (result === "draw") return t("page.team.wdl.drawn");
  if (result === "loss") return t("page.team.wdl.lost");
  return result;
}