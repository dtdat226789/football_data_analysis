import { useFormatters } from "../../i18n/useFormatters.js";
import { formatTick, labelStep, niceMax } from "./chartMath.js";
import { ChartTooltip, useChartTooltip } from "./useChartTooltip.jsx";

export default function BarChart({ spec, title }) {
  const { t, num, dec } = useFormatters();
  const { frameRef, tooltip, show, hide } = useChartTooltip();
  const series = spec.series?.[0];
  const labels = spec.labels ?? [];
  const values = series?.values ?? [];
  const max = niceMax(values);
  const formatValue = (value) => (Number.isInteger(value) ? num(value) : dec(value, 2));
  const svgLabel = t("analysis.chart.interactive", { title });

  if (!series || !labels.length) return null;

  const handlers = (index, value) => {
    const detail = spec.details?.[index];
    const text = detail
      ? `${detail} · ${series.label}: ${formatValue(value)} ${spec.valueLabel}`
      : `${labels[index]}: ${formatValue(value)} ${spec.valueLabel}`;
    return {
      onMouseEnter: (event) => show(event, text),
      onMouseMove: (event) => show(event, text),
      onMouseLeave: hide,
      onFocus: (event) => show(event, text),
      onBlur: hide,
    };
  };

  if (spec.horizontal) {
    const width = 640;
    const height = Math.max(220, labels.length * 28 + 60);
    const margin = { top: 12, right: 56, bottom: 36, left: 150 };
    const plotWidth = width - margin.left - margin.right;
    const plotHeight = height - margin.top - margin.bottom;
    const slot = plotHeight / labels.length;
    const barHeight = Math.min(18, slot * 0.62);

    return (
      <div className="chart-surface" ref={frameRef}>
        <svg className="chart-svg" viewBox={`0 0 ${width} ${height}`} role="img" aria-label={svgLabel}>
          {[0, 0.5, 1].map((fraction) => {
            const x = margin.left + fraction * plotWidth;
            const y = margin.top + plotHeight + 18;
            return (
              <g key={fraction}>
                <line className="chart-grid-line" x1={x} y1={margin.top} x2={x} y2={margin.top + plotHeight} />
                <text className="chart-axis-label" x={x} y={y} textAnchor="middle">
                  {formatTick(max * fraction, num, dec)}
                </text>
              </g>
            );
          })}
          <line className="chart-axis" x1={margin.left} y1={margin.top} x2={margin.left} y2={margin.top + plotHeight} />
          {labels.map((label, index) => {
            const value = values[index] ?? 0;
            const barWidth = (value / max) * plotWidth;
            const y = margin.top + index * slot + (slot - barHeight) / 2;
            const text = `${label}: ${formatValue(value)} ${spec.valueLabel}`;
            return (
              <g key={`${label}-${index}`} tabIndex={0} aria-label={text} className="chart-mark" {...handlers(index, value)}>
                <title>{text}</title>
                <text
                  className="chart-axis-label chart-axis-label--y"
                  x={margin.left - 8}
                  y={y + barHeight / 2}
                  textAnchor="end"
                  dominantBaseline="middle"
                >
                  {label}
                </text>
                <rect
                  className="chart-bar"
                  x={margin.left}
                  y={y}
                  width={Math.max(barWidth, value > 0 ? 2 : 0)}
                  height={barHeight}
                  rx={3}
                  fill={series.color}
                />
              </g>
            );
          })}
          <text className="chart-axis-title" x={margin.left + plotWidth / 2} y={height - 4} textAnchor="middle">
            {spec.valueLabel}
          </text>
        </svg>
        <ChartTooltip tooltip={tooltip} />
      </div>
    );
  }

  const width = 640;
  const height = 300;
  const margin = { top: 16, right: 16, bottom: 52, left: 48 };
  const plotWidth = width - margin.left - margin.right;
  const plotHeight = height - margin.top - margin.bottom;
  const slot = plotWidth / labels.length;
  const barWidth = Math.max(4, Math.min(48, slot * 0.62));
  const step = labelStep(labels.length, 14);

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
        {labels.map((label, index) => {
          const value = values[index] ?? 0;
          const barHeight = (value / max) * plotHeight;
          const x = margin.left + index * slot + (slot - barWidth) / 2;
          const y = margin.top + plotHeight - barHeight;
          return (
            <g key={`${label}-${index}`}>
              {index % step === 0 && (
                <text
                  className="chart-axis-label"
                  x={x + barWidth / 2}
                  y={margin.top + plotHeight + 18}
                  textAnchor="end"
                  transform={`rotate(-35 ${x + barWidth / 2} ${margin.top + plotHeight + 18})`}
                >
                  {label}
                </text>
              )}
              <g tabIndex={0} aria-label={`${label}: ${formatValue(value)} ${spec.valueLabel}`} className="chart-mark" {...handlers(index, value)}>
                <title>{`${label}: ${formatValue(value)} ${spec.valueLabel}`}</title>
                <rect
                  className="chart-bar"
                  x={x}
                  y={y}
                  width={barWidth}
                  height={Math.max(barHeight, value > 0 ? 2 : 0)}
                  rx={3}
                  fill={series.color}
                />
              </g>
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
