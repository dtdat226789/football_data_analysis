export function Loading({ label = "Loading…" }) {
  return <div className="loader">{label}</div>;
}

export function ErrorBox({ error }) {
  return <div className="error-box">{error || "Something went wrong."}</div>;
}

export function Empty({ children }) {
  return <div className="loader">{children}</div>;
}

export function Skeleton({ width = "100%", height = 14, className = "", style }) {
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