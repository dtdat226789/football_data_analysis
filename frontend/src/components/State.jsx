export function Loading({ label = "Loading…" }) {
  return <div className="loader">{label}</div>;
}

export function ErrorBox({ error }) {
  return <div className="error-box">{error || "Something went wrong."}</div>;
}

export function Empty({ children }) {
  return <div className="loader">{children}</div>;
}