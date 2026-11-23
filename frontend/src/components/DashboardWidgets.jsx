import { useFormatters } from "../i18n/useFormatters.js";

/**
 * @typedef {Record<string, any> & { date: string, opponent: string | null }} DashGame
 * @typedef {{ key: string, labelKey: string, value: string | number,
 *   options: { value: string | number, label: string }[], onChange: (value: string) => void }} DashField
 * @typedef {{ key: string, labelKey: string, numeric?: boolean }} DashColumn
 */

const UNIT_KEYS = {
  clubRating: "kpi.unit.rating",
  goalsPerGame: "kpi.unit.perGame",
  last5GoalsPerGame: "kpi.unit.perGame",
  awayGoalsPerGame: "kpi.unit.perGame",
  pointsPerGame: "kpi.unit.perGame",
  homeGoalsPerGame: "kpi.unit.perGame",
  goalsAgainstPerGame: "kpi.unit.perGame",
  awayGoalsAgainstPerGame: "kpi.unit.perGame",
  homeGoalShare: "kpi.unit.percent",
  cleanSheetPct: "kpi.unit.percent",
  expectedPoints: "kpi.unit.points",
};

function display(value, num) {
  return value === null || value === undefined ? "—" : num(Math.round(value * 100) / 100);
}

/** @param {{ tile: { key: string, value: number|null, rank: number|null, rank_total: number } }} props */
export function KpiTile({ tile }) {
  const { t, num } = useFormatters();
  const unitKey = UNIT_KEYS[tile.key];
  return (
    <div className="dash-tile">
      <div className="dash-tile-label">{t(`kpi.${tile.key}`)}</div>
      <div className="dash-tile-value">
        {display(tile.value, num)} {unitKey && <span className="dash-tile-unit">{t(unitKey)}</span>}
      </div>
      <div className="dash-tile-rank">
        {tile.rank ? `#${tile.rank} ${t("dash.rankInLeague")}` : t("dash.noRank")}
      </div>
    </div>
  );
}

/** @param {{ games: DashGame[], metric: string, titleKey: string }} props */
export function MiniCompare({ games, metric, titleKey }) {
  const { t, num } = useFormatters();
  const max = Math.max(...games.map((game) => game[metric] ?? 0), 1);
  return (
    <div className="dash-panel dash-compare">
      <h3>{t(titleKey)}</h3>
      {games.length === 0 ? (
        <p className="dash-empty">{t("dash.noMatches")}</p>
      ) : (
        <div className="dash-bar-list">
          {games.map((game, i) => (
            <div className="dash-bar-row" key={`${game.date}-${i}`}>
              <span className="dash-bar-label" title={game.opponent || ""}>
                {game.opponent}
              </span>
              <div className="dash-bar-track">
                <div
                  className="dash-bar-fill"
                  style={{ width: `${((game[metric] ?? 0) / max) * 100}%` }}
                />
              </div>
              <span className="dash-bar-value">{num(game[metric] ?? 0)}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

/** @param {{ fields: DashField[] }} props */
export function FilterSelects({ fields }) {
  const { t } = useFormatters();
  return (
    <div className="dash-filters">
      {fields.map((field) => (
        <label className="dash-field" key={field.key}>
          <span>{t(field.labelKey)}</span>
          <select
            aria-label={t(field.labelKey)}
            value={field.value ?? ""}
            onChange={(event) => field.onChange(event.target.value)}
          >
            {field.options.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </label>
      ))}
    </div>
  );
}

/** @param {{ rows: Record<string, any>[], columns: DashColumn[] }} props */
export function RankTable({ rows, columns }) {
  const { t, num } = useFormatters();
  return (
    <table className="dash-table">
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={column.key} scope="col" className={column.numeric ? "num" : undefined}>
              {t(column.labelKey)}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((row, i) => (
          <tr key={`${row.label}-${i}`} className={row.is_selected ? "is-selected" : undefined}>
            {columns.map((column) => (
              <td key={column.key} className={column.numeric ? "num" : undefined}>
                {typeof row[column.key] === "number" ? num(Math.round(row[column.key] * 100) / 100) : (row[column.key] ?? "—")}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

/** @param {{ data: { season: string, value: number }[], label: string }} props */
export function LineTrend({ data, label }) {
  const { t, num } = useFormatters();
  const width = 520;
  const height = 180;
  const pad = 26;
  if (!data.length) return <p className="dash-empty">{t("dash.noTrend")}</p>;

  const values = data.map((point) => point.value ?? 0);
  const min = Math.min(...values);
  const max = Math.max(...values);
  const span = max - min || 1;
  const points = data.map((point, i) => ({
    x: pad + (i * (width - 2 * pad)) / Math.max(data.length - 1, 1),
    y: height - pad - ((point.value ?? 0) - min) / span * (height - 2 * pad),
    point,
  }));
  const line = points.map((p) => `${p.x},${p.y}`).join(" ");
  const area = `${pad},${height - pad} ${line} ${points[points.length - 1].x},${height - pad}`;
  const showAll = points.length <= 6;

  return (
    <svg
      className="dash-trend"
      viewBox={`0 0 ${width} ${height}`}
      role="img"
      aria-label={t("dash.trendLabel", { label })}
    >
      <polygon points={area} className="dash-trend-area" />
      <polyline points={line} className="dash-trend-line" />
      {points.map((p, i) => (
        <circle key={`${p.point.season}-${i}`} cx={p.x} cy={p.y} r={4} className="dash-trend-dot">
          <title>{`${p.point.season}: ${num(Math.round((p.point.value ?? 0) * 100) / 100)}`}</title>
        </circle>
      ))}
      {(showAll ? points : [points[0], points[points.length - 1]]).map((p, i) => (
        <text key={`${p.point.season}-label-${i}`} x={p.x} y={height - 6} textAnchor="middle" className="dash-trend-label">
          {p.point.season}
        </text>
      ))}
      <text x={4} y={pad} className="dash-trend-extent">{num(Math.round(max * 100) / 100)}</text>
      <text x={4} y={height - pad} className="dash-trend-extent">{num(Math.round(min * 100) / 100)}</text>
    </svg>
  );
}
