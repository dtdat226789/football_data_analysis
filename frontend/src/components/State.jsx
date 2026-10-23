import { useFormatters } from "../i18n/useFormatters.js";

/** @param {{ label?: string }} props Absent falls back to the loading line. */
export function Loading({ label }) {
  const { t } = useFormatters();
  return <div className="loader">{label || t("common.loading")}</div>;
}

/** @param {{ error?: string }} props Absent or blank falls back to a generic line. */
export function ErrorBox({ error }) {
  const { t } = useFormatters();
  return <div className="error-box">{error || t("common.error")}</div>;
}

export function Empty({ children }) {
  return <div className="loader">{children}</div>;
}

/**
 * @param {object} props
 * @param {string | number} [props.width] A CSS length; a bare number is a px value.
 * @param {string | number} [props.height]
 * @param {string} [props.className]
 * @param {object} [props.style] Merged last, so a caller can override width/height.
 */
export function Skeleton({ width = "100%", height = 14, className = "", style = {} }) {
  return (
    <div
      className={"skeleton-block " + className}
      style={{ width, height, ...style }}
      aria-hidden="true"
    />
  );
}

export function TableSkeleton({ rows = 6, cols = 5 }) {
  return (
    <table className="data" aria-hidden="true">
      <thead>
        <tr>
          {Array.from({ length: cols }, (_, i) => (
            <th key={i}>
              <Skeleton width={50 + ((i * 17) % 40)} height={12} />
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {Array.from({ length: rows }, (_, i) => (
          <tr key={i}>
            {Array.from({ length: cols }, (_, j) => (
              <td key={j}>
                <Skeleton width={40 + ((i * 13 + j * 19) % 45)} height={12} />
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export function ListSkeleton({ items = 5, height = 42 }) {
  return (
    <div className="skeleton-list">
      {Array.from({ length: items }, (_, i) => (
        <Skeleton key={i} height={height} />
      ))}
    </div>
  );
}