import { Link } from "react-router-dom";

export function TeamLink({ name, className = "link" }) {
  if (!name) return <span className="muted">—</span>;
  return (
    <Link className={className} to={`/teams/${encodeURIComponent(name)}`}>
      {name}
    </Link>
  );
}