import { useFormatters } from "../../i18n/useFormatters.js";
import { formatTick, labelStep, niceMax } from "./chartMath.js";
import { ChartTooltip, useChartTooltip } from "./useChartTooltip.jsx";

export default function StackedBarChart({ spec, title }) {
  const { t, num, dec } = useFormatters();
  const { frameRef, tooltip, show, hide } = useChartTooltip();
  const labels = spec.labels ?? [];
  const series = spec.series ?? [];
  const totals = labels.map((_, index) =>
    series.reduce((sum, item) => sum + (item.values?.[index] ?? 0), 0),
  );
  const max = niceMax(totals);
  const formatValue = (value) => (Number.isInteger(value) ? num(value) : dec(value, 2));
  const svgLabel = t("analysis.chart.interactive", { title });

  if (!series.length || !labels.length) return null;

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
          const x = margin.left + index * slot + (slot - barWidth) / 2;
          let segmentBottom = margin.top + plotHeight;
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
              {series.map((item, seriesIndex) => {
                const value = item.values?.[index] ?? 0;
                const segmentHeight = (value / max) * plotHeight;
                segmentBottom -= segmentHeight;
                const text = `${label} · ${item.label}: ${formatValue(value)} ${spec.valueLabel}`;
                return (
                  <g
                    key={`${item.label}-${seriesIndex}`}
                    tabIndex={0}
                    aria-label={text}
                    className="chart-mark"
                    onMouseEnter={(event) => show(event, text)}
                    onMouseMove={(event) => show(event, text)}
                    onMouseLeave={hide}
                    onFocus={(event) => show(event, text)}
                    onBlur={hide}
                  >
                    <title>{text}</title>
                    <rect
                      className="chart-bar"
                      x={x}
                      y={segmentBottom}
                      width={barWidth}
                      height={Math.max(segmentHeight, value > 0 ? 2 : 0)}
                      fill={item.color}
                    />
                  </g>
                );
              })}
            </g>
          );
        })}
        <text className="chart-axis-title" x={width / 2} y={height - 4} textAnchor="middle">
          {spec.categoryLabel ?? t("analysis.chart.axis.season")}
        </text>
      </svg>
      <ul className="chart-legend">
        {series.map((item) => (
          <li key={item.label}>
            <span className="chart-swatch" style={{ background: item.color }} />
            {item.label}
          </li>
        ))}
      </ul>
      <ChartTooltip tooltip={tooltip} />
    </div>
  );
}
