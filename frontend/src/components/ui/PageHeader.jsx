/**
 * @param {{ title: import("react").ReactNode, subtitle?: import("react").ReactNode,
 *   actions?: import("react").ReactNode, children?: import("react").ReactNode }} props
 */
export default function PageHeader({ title, subtitle, actions, children }) {
  return (
    <div className="page-head">
      <div className="page-heading">
        <h2>{title}</h2>
        {subtitle != null && subtitle !== false && <p>{subtitle}</p>}
      </div>
      {actions != null && actions !== false && <div className="page-head-actions">{actions}</div>}
      {children}
    </div>
  );
}
