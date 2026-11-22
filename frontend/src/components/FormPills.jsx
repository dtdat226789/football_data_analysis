import { useFormatters } from "../i18n/useFormatters.js";

function resultCode(result) {
  const value = String(result ?? "").toUpperCase();
  if (value === "W" || value === "WIN") return "W";
  if (value === "D" || value === "DRAW") return "D";
  if (value === "L" || value === "LOSS") return "L";
  return "";
}

function resultLabel(result, t) {
  const code = resultCode(result);
  if (code) return t(`result.${code}`);
  return String(result ?? "");
}

export function FormPills({ results }) {
  const { t } = useFormatters();
  if (!Array.isArray(results) || results.length === 0) {
    return <span className="muted">—</span>;
  }
  return (
    <span className="formline">
      {results.map((r, i) => {
        const code = resultCode(r?.team_result);
        const score = `${r?.home_team ?? ""} ${r?.home_score ?? ""}-${r?.away_score ?? ""} ${r?.away_team ?? ""}`;
        return (
          <span
            key={i}
            className={`pill ${code}`}
            title={score}
            aria-label={`${resultLabel(r?.team_result, t)}: ${score}`}
          >
            {code || "—"}
          </span>
        );
      })}
    </span>
  );
}
