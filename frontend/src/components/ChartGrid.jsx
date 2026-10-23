import { useState } from "react";

import { api } from "../api/client.js";
import { useFormatters } from "../i18n/useFormatters.js";
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

  return (
    <>
      <div className="chart-grid">
        {charts.map((c) => (
          <div
            key={c}
            className="card chart-card"
            role="button"
            tabIndex={0}
            aria-label={t("chart.viewFull", { name: chartCaption(c, t) })}
            onClick={() => setLightbox(c)}
            onKeyDown={(e) => {
              if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                setLightbox(c);
              }
            }}
          >
            <img src={api.chartUrl(league, c)} alt={c} loading="lazy" />
            <div className="caption">{chartCaption(c, t)}</div>
          </div>
        ))}
      </div>
      {lightbox && (
        <ChartLightbox
          src={api.chartUrl(league, lightbox)}
          title={chartCaption(lightbox, t)}
          onClose={() => setLightbox(null)}
        />
      )}
    </>
  );
}