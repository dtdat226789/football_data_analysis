import { useState } from "react";
import { api } from "../api/client.js";
import ChartLightbox from "./ChartLightbox.jsx";

export function chartCaption(name) {
  return name.replace(/\.png$/, "").replace(/_/g, " ");
}

export default function ChartGrid({ league, charts }) {
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
            aria-label={`View ${chartCaption(c)} full screen`}
            onClick={() => setLightbox(c)}
            onKeyDown={(e) => {
              if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                setLightbox(c);
              }
            }}
          >
            <img src={api.chartUrl(league, c)} alt={c} loading="lazy" />
            <div className="caption">{chartCaption(c)}</div>
          </div>
        ))}
      </div>
      {lightbox && (
        <ChartLightbox
          src={api.chartUrl(league, lightbox)}
          title={chartCaption(lightbox)}
          onClose={() => setLightbox(null)}
        />
      )}
    </>
  );
}