import { Link } from "react-router-dom";

/**
 * A consistent way back from a detail page to the list it came from.
 *
 * @param {{ to: string, children: import("react").ReactNode,
 *   [key: string]: any }} props
 */
export default function BackLink({ to, children, ...rest }) {
  return (
    <Link className="back-link" to={to} {...rest}>
      <span aria-hidden="true">←</span>
      {children}
    </Link>
  );
}
