import { useFormatters } from "../../i18n/useFormatters.js";
import { formatTick, labelStep, niceMax } from "./chartMath.js";
import { ChartTooltip, useChartTooltip } from "./useChartTooltip.jsx";

export default function LineChart({ spec, title }) {
  const { t, num, dec } = useFormatters();
  const { frameRef, tooltip, show, hide } = useChartTooltip();
  const labels = spec.labels ?? [];
  const series = spec.series?.[0];
  const values = series?.values ?? [];
  const max = niceMax(values);
  const formatValue = (value) => (Number.isInteger(value) ? num(value) : dec(value, 2));
  const svgLabel = t("analysis.chart.interactive", { title });

  if (!series || !labels.length) return null;

  const tooltipText = (point) => {
    const detail = spec.details?.[point.index];
    return `${detail ? `${detail} · ` : ""}${series.label}: ${formatValue(point.value)} ${spec.valueLabel}`;
  };

  const width = 640;
  const height = 300;
  const margin = { top: 16, right: 20, bottom: 52, left: 48 };
  const plotWidth = width - margin.left - margin.right;
  const plotHeight = height - margin.top - margin.bottom;
  const step = labelStep(labels.length, 12);
  const points = labels.map((_, index) => {
    const value = values[index];
    if (typeof value !== "number" || !Number.isFinite(value)) return null;
    return {
      index,
      value,
      x: labels.length === 1 ? margin.left + plotWidth / 2 : margin.left + (index * plotWidth) / (labels.length - 1),
      y: margin.top + plotHeight - (value / max) * plotHeight,
    };
  }).filter(Boolean);
  const line = points.map((point, index) => `${index === 0 ? "M" : "L"} ${point.x} ${point.y}`).join(" ");
  const area = points.length
    ? `${line} L ${points[points.length - 1].x} ${margin.top + plotHeight} L ${points[0].x} ${margin.top + plotHeight} Z`
    : "";

  return (
    <div className="chart-surface" ref={frameRef}>
      <svg className="chart-svg" viewBox={`0 0 ${width} ${height}`} role="img" aria-label={svgLabel}>
        {[0, 0.25, 0.5, 0.75, 1].map((fraction) => {
          const y = margin.top + plotHeight - fraction * plotHeight;
          return (
            <g key={fraction}>
              <line className="chart-grid-line" x1={margin.left} y1={y} x2={margin.left + plotWidth} y2={y} />
              <text className="chart-axis-label" x={margin.left - 8} y={y + 4} textAnchor="end">
                {formatTick(max * fraction, num, dec)}
              </text>
            </g>
          );
        })}
        <line className="chart-axis" x1={margin.left} y1={margin.top} x2={margin.left} y2={margin.top + plotHeight} />
        <line
          className="chart-axis"
          x1={margin.left}
          y1={margin.top + plotHeight}
          x2={margin.left + plotWidth}
          y2={margin.top + plotHeight}
        />
        {points.length > 1 && <path className="chart-area" d={area} />}
        {points.length > 1 && <path className="chart-line-path" d={line} stroke={series.color} />}
        {labels.map((label, index) => {
          const point = points.find((item) => item.index === index);
          return (
            <g key={`${label}-${index}`}>
              {index % step === 0 && (
                <text
                  className="chart-axis-label"
                  x={point?.x ?? margin.left + (index * plotWidth) / Math.max(labels.length - 1, 1)}
                  y={margin.top + plotHeight + 18}
                  textAnchor="end"
                  transform={`rotate(-35 ${point?.x ?? margin.left} ${margin.top + plotHeight + 18})`}
                >
                  {label}
                </text>
              )}
              {point && (
                <g
                  tabIndex={0}
                  aria-label={`${label}: ${formatValue(point.value)} ${spec.valueLabel}`}
                  className="chart-mark"
                  onMouseEnter={(event) => show(event, tooltipText(point))}
                  onMouseMove={(event) => show(event, tooltipText(point))}
                  onMouseLeave={hide}
                  onFocus={(event) => show(event, tooltipText(point))}
                  onBlur={hide}
                >
                  <title>{`${label}: ${formatValue(point.value)} ${spec.valueLabel}`}</title>
                  <circle className="chart-line-point" cx={point.x} cy={point.y} r={4} fill={series.color} />
                </g>
              )}
            </g>
          );
        })}
        <text className="chart-axis-title" x={width / 2} y={height - 4} textAnchor="middle">
          {spec.categoryLabel ?? t("analysis.chart.axis.season")}
        </text>
      </svg>
      <ChartTooltip tooltip={tooltip} />
    </div>
  );
}
