import { useEffect } from "react";

export default function ChartLightbox({ src, title, onClose }) {
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
          <button type="button" className="lightbox-close" onClick={onClose} aria-label="Close">
            ×
          </button>
        </div>
        <img src={src} alt={title} />
      </div>
    </div>
  );
}