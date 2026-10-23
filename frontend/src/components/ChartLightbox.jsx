import { useEffect } from "react";

import { useFormatters } from "../i18n/useFormatters.js";

/** @param {{ src: string, title?: string, onClose?: () => void }} props */
export default function ChartLightbox({ src, title, onClose }) {
  const { t } = useFormatters();

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "Escape") onClose?.();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <div
      className="lightbox-backdrop"
      role="dialog"
      aria-modal="true"
      aria-label={title}
      onClick={onClose}
    >
      <div className="lightbox-frame" onClick={(e) => e.stopPropagation()}>
        <div className="lightbox-head">
          <span className="caption">{title}</span>
          <button type="button" className="lightbox-close" onClick={onClose} aria-label={t("common.close")}>
            ×
          </button>
        </div>
        <img src={src} alt={title} />
      </div>
    </div>
  );
}