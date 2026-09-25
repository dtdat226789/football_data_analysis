import { useId } from "react";

function pretty(n) {
  return typeof n === "number" ? n.toLocaleString() : String(n ?? "—");
}

export function BarList({
  data,
  color = "var(--accent)",
  height = 8,
  format,
  title,
}) {
  const max = Math.max(...data.map((d) => d.value), 1);
  return (
    <div>
      {title && <div className="chart-title">{title}</div>}
      <div className="bar-list">
        {data.map((d, i) => (
          <div className="bar-row" key={i}>
            <span className="bar-label" title={d.label}>
              {d.label}
            </span>
            <div className="bar-track" style={{ height }}>
              <div
                className="bar-fill"
                style={{ width: `${Math.max((d.value / max) * 100, d.value > 0 ? 2 : 0)}%`, background: color }}
                title={`${d.label}: ${format ? format(d.value) : pretty(d.value)}`}
              />
            </div>
            <span className="bar-value">{format ? format(d.value) : pretty(d.value)}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export function Donut({
  segments,
  size = 120,
  thickness = 20,
  center,
  title,
}) {
  const uid = useId();
  const total = segments.reduce((acc, s) => acc + (s.value || 0), 0) || 1;
  const radius = (size - thickness) / 2;
  const circumference = 2 * Math.PI * radius;
  let acc = 0;
  return (
    <div className="donut-wrap">
      {title && <div className="chart-title">{title}</div>}
      <div className="donut-inline">
        <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} className="donut" role="img">
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            fill="none"
            stroke="var(--border)"
            strokeWidth={thickness}
          />
          {segments.map((s, i) => {
            const frac = (s.value || 0) / total;
            const dash = frac * circumference;
            const offset = -acc * circumference;
            acc += frac;
            if (!dash) return null;
            return (
              <circle
                key={i}
                cx={size / 2}
                cy={size / 2}
                r={radius}
                fill="none"
                stroke={s.color}
                strokeWidth={thickness}
                strokeDasharray={`${dash} ${circumference - dash}`}
                strokeDashoffset={offset}
                transform={`rotate(-90 ${size / 2} ${size / 2})`}
              />
            );
          })}
          {center != null && (
            <text x={size / 2} y={size / 2} textAnchor="middle" dominantBaseline="central" className="donut-center">
              {center}
            </text>
          )}
        </svg>
        <ul className="donut-legend">
          {segments.map((s, i) => (
            <li key={i}>
              <span className="swatch" style={{ background: s.color }} />
              {s.label}: {pretty(s.value)}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export function StatCard({ label, value, sub }) {
  return (
    <div className="kpi stat-card">
      <div className="label">{label}</div>
      <div className="value">{value}</div>
      {sub && <div className="caption">{sub}</div>}
    </div>
  );
}

export { pretty };