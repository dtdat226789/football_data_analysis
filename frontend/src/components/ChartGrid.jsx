import { useCallback, useState } from "react";

import { api } from "../api/client.js";
import { useFormatters } from "../i18n/useFormatters.js";
import { isValidChartName } from "../lib/safeUrl.js";
import { asRecord } from "../lib/shape.js";
import { interactiveChart } from "./analysis/chartData.js";
import { chartComponent } from "./analysis/registry.js";
import ChartLightbox from "./ChartLightbox.jsx";

export function chartCaption(name, t) {
  const stem = name.replace(/\.png$/, "");
  const key = `analysis.chart.${stem}`;
  const caption = t(key);
  return caption === key ? stem.replace(/_/g, " ") : caption;
}

export default function ChartGrid({ league, charts, reports = {} }) {
  const { t } = useFormatters();
  const [lightbox, setLightbox] = useState(null);
  const closeLightbox = useCallback(() => setLightbox(null), []);
  const safeReports = asRecord(reports);
  const safeCharts = Array.isArray(charts) ? charts.filter(isValidChartName) : [];

  return (
    <>
      <div className="chart-grid">
        {safeCharts.map((c) => {
          const caption = chartCaption(c, t);
          const spec = interactiveChart(c, safeReports, t);
          const Chart = spec ? chartComponent(spec.kind) : null;

          if (Chart) {
            return (
              <article key={c} className="card chart-card chart-card--interactive">
                <h3>{caption}</h3>
                <Chart spec={spec} title={caption} />
                <div className="chart-card-footer">
                  <span className="caption">{t("analysis.chart.snapshot")}</span>
                  <button
                    type="button"
                    className="chart-image-button"
                    aria-label={t("chart.viewFull", { name: caption })}
                    onClick={() => setLightbox(c)}
                  >
                    {t("chart.viewImage")}
                  </button>
                </div>
                <p className="caption chart-card-note">{t("analysis.chart.snapshotNote")}</p>
              </article>
            );
          }

          return (
            <button
              key={c}
              type="button"
              className="card chart-card"
              aria-label={t("chart.viewFull", { name: caption })}
              onClick={() => setLightbox(c)}
            >
              <img
                src={api.chartUrl(league, c)}
                alt=""
                width={640}
                height={320}
                loading="lazy"
                decoding="async"
              />
              <span className="caption">{caption}</span>
            </button>
          );
        })}
      </div>
      {lightbox && (
        <ChartLightbox
          src={api.chartUrl(league, lightbox)}
          title={chartCaption(lightbox, t)}
          onClose={closeLightbox}
        />
      )}
    </>
  );
}
