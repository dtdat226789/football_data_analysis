import { useFormatters } from "../../i18n/useFormatters.js";

/**
 * A keyboard-reachable, labelled scroll region for wide tables.
 *
 * `tabIndex` matters here: a horizontally scrollable div is otherwise locked
 * behind a mouse, so keyboard and switch users cannot reach the clipped columns.
 *
 * @param {{ className?: string, label?: string, children?: import("react").ReactNode,
 *   [key: string]: any }} props
 */
export default function TableShell({ className = "", label, children, ...rest }) {
  const { t } = useFormatters();
  return (
    <div
      className={["table-shell", className].filter(Boolean).join(" ")}
      role="region"
      aria-label={label || t("table.scrollable")}
      tabIndex={0}
      {...rest}
    >
      {children}
    </div>
  );
}
