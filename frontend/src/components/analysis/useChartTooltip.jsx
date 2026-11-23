import { useCallback, useRef, useState } from "react";

export function useChartTooltip() {
  const frameRef = useRef(null);
  const [tooltip, setTooltip] = useState(null);

  const show = useCallback((event, text) => {
    if (!text) return;
    const frame = frameRef.current;
    if (!frame) return;

    const frameBox = frame.getBoundingClientRect();
    const markBox = event?.currentTarget?.getBoundingClientRect?.();
    const hasPointer = Number.isFinite(event?.clientX) && Number.isFinite(event?.clientY);
    const clientX = hasPointer ? event.clientX : markBox ? markBox.left + markBox.width / 2 : frameBox.left;
    const clientY = hasPointer ? event.clientY : markBox ? markBox.top : frameBox.top;
    const left = Math.min(Math.max(clientX - frameBox.left, 12), Math.max(frameBox.width - 12, 12));
    const top = Math.max(clientY - frameBox.top - 8, 24);

    setTooltip({ text, left, top });
  }, []);

  const hide = useCallback(() => setTooltip(null), []);

  return { frameRef, tooltip, show, hide };
}

export function ChartTooltip({ tooltip }) {
  if (!tooltip) return null;
  return (
    <div className="chart-tooltip" role="status" style={{ left: tooltip.left, top: tooltip.top }}>
      {tooltip.text}
    </div>
  );
}
