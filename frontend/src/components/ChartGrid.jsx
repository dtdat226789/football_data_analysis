import { useCallback, useState } from "react";

import { api } from "../api/client.js";
import { useFormatters } from "../i18n/useFormatters.js";
import { isValidChartName } from "../lib/safeUrl.js";
import ChartLightbox from "./ChartLightbox.jsx";

export function chartCaption(name, t) {
  const stem = name.replace(/\.png$/, "");
  const key = `analysis.chart.${stem}`;
  // Unknown keys fall back to the key name itself, so an unmapped chart keeps
  // its readable English rendering instead of showing the dotted key.
  const caption = t(key);
  return caption === key ? stem.replace(/_/g, " ") : caption;
}

export default function ChartGrid({ league, charts }) {
  const { t } = useFormatters();
  const [lightbox, setLightbox] = useState(null);
  const closeLightbox = useCallback(() => setLightbox(null), []);
  const safeCharts = Array.isArray(charts) ? charts.filter(isValidChartName) : [];

  return (
    <>
      <div className="chart-grid">
        {safeCharts.map((c) => {
          const caption = chartCaption(c, t);
          return (
            <button
              key={c}
              type="button"
              className="card chart-card"
              aria-label={t("chart.viewFull", { name: caption })}
              onClick={() => setLightbox(c)}
            >
              {/* The button's accessible name and the caption below already
                  describe the chart, so the image itself stays decorative. */}
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
