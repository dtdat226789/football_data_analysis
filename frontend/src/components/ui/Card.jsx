/**
 * @param {{ as?: any, className?: string, children?: import("react").ReactNode,
 *   [key: string]: any }} props
 */
export function Card({ as: Component = "section", className = "", children, ...rest }) {
  return (
    <Component className={["card", className].filter(Boolean).join(" ")} {...rest}>
      {children}
    </Component>
  );
}

/**
 * @param {{ title?: import("react").ReactNode, actions?: import("react").ReactNode,
 *   children?: import("react").ReactNode }} props
 */
export function CardHeader({ title, actions, children }) {
  return (
    <div className="card-head">
      {title != null && title !== false && <h3>{title}</h3>}
      {actions != null && actions !== false && <div className="card-actions">{actions}</div>}
      {children}
    </div>
  );
}
