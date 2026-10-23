
import { useCallback } from "react";

import { useFormatters } from "../i18n/useFormatters.js";

/**
 * @param {object} props
 * @param {{ label: string, value: number }[]} props.data
 * @param {string} [props.color]
 * @param {number} [props.height]
 * @param {(value: number) => string} [props.format] Falls back to `pretty`.
 * @param {string} [props.title] Omitted heading.
 */
export function BarList({
  data,
  color = "var(--accent)",
  height = 8,
  format,
  title,
}) {
  const { num } = useFormatters();
  const pretty = useCallback((v) => num(v), [num]);
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

/**
 * @param {object} props
 * @param {{ label: string, value: number, color: string }[]} props.segments
 * @param {number} [props.size]
 * @param {number} [props.thickness]
 * @param {string} [props.center] Label in the hole.
 * @param {string} [props.title] Omitted heading.
 */
export function Donut({
  segments,
  size = 120,
  thickness = 20,
  center,
  title,
}) {
  const { num } = useFormatters();
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
              {s.label}: {num(s.value)}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

/**
 * @param {object} props
 * @param {string} props.label
 * @param {string | number} props.value
 * @param {string} [props.sub] Optional caption under the value.
 */
export function StatCard({ label, value, sub }) {
  return (
    <div className="kpi stat-card">
      <div className="label">{label}</div>
      <div className="value">{value}</div>
      {sub && <div className="caption">{sub}</div>}
    </div>
  );
}
