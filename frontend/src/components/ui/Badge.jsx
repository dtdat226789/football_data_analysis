/**
 * @param {{ tone?: string, className?: string, children?: import("react").ReactNode,
 *   [key: string]: any }} props
 */
export default function Badge({ tone, className = "", children, ...rest }) {
  return (
    <span className={["badge", tone, className].filter(Boolean).join(" ")} {...rest}>
      {children}
    </span>
  );
}
