import { useEffect, useId, useRef } from "react";

import { useFormatters } from "../i18n/useFormatters.js";

/** @param {{ src: string, title?: string, onClose?: () => void }} props */
export default function ChartLightbox({ src, title, onClose }) {
  const { t } = useFormatters();
  const titleId = useId();
  const frameRef = useRef(null);
  const closeRef = useRef(null);

  // Move focus into the dialog and hand it back when the dialog goes away, so
  // keyboard users do not land back at the top of the page on close.
  useEffect(() => {
    const previous = document.activeElement;
    closeRef.current?.focus();
    return () => {
      if (previous instanceof HTMLElement) previous.focus();
    };
  }, []);

  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "Escape") {
        onClose?.();
        return;
      }
      if (e.key !== "Tab") return;
      const focusable = frameRef.current?.querySelectorAll(
        "button, a[href], input, select, textarea, [tabindex]:not([tabindex='-1'])",
      );
      if (!focusable?.length) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <div
      className="lightbox-backdrop"
      role="dialog"
      aria-modal="true"
      aria-labelledby={titleId}
      onClick={onClose}
    >
      <div className="lightbox-frame" ref={frameRef} onClick={(e) => e.stopPropagation()}>
        <div className="lightbox-head">
          <span className="caption" id={titleId}>{title}</span>
          <button
            type="button"
            className="lightbox-close"
            ref={closeRef}
            onClick={onClose}
            aria-label={t("common.close")}
          >
            ×
          </button>
        </div>
        <img src={src} alt={title} decoding="async" />
      </div>
    </div>
  );
}
