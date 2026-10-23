import { useMemo } from "react";

import { useFormatters } from "../i18n/useFormatters.js";

const MAX_DEPTH = 5;

function isPlainObject(v) {
  return typeof v === "object" && v !== null && !Array.isArray(v);
}

/**
 * One leaf value.
 *
 * `yes`/`no` are translated because they are words on screen; the object keys
 * above them are not, because they are the API's own field names and a
 * translated key would not match anything the reader could look up.
 *
 * @param {object} props
 * @param {any} props.value
 * @param {number} [props.depth]
 * @param {Function} props.t A translation function, passed down by `Tree`.
 */
function Cell({ value, depth, t }) {
  if (value === null || value === undefined) return <span className="muted">—</span>;
  if (typeof value === "boolean") return <span className="badge">{value ? t("tree.yes") : t("tree.no")}</span>;
  if (typeof value === "number") return <span className="num">{Number.isInteger(value) ? value : value.toFixed(2)}</span>;
  if (typeof value === "string") return <span>{value}</span>;
  return <Tree value={value} depth={depth} />;
}

export default function Tree({ value, depth = 0 }) {
  const { t } = useFormatters();
  const flat = useMemo(
    () => (isPlainObject(value) ? Object.entries(value) : null),
    [value],
  );

  if (value === null || value === undefined) return <span className="muted">—</span>;

  if (typeof value === "string" || typeof value === "number" || typeof value === "boolean") {
    return <Cell value={value} depth={depth} t={t} />;
  }

  if (Array.isArray(value)) {
    if (value.length === 0) return <span className="muted">{t("common.none")}</span>;
    const allObjects = value.every((v) => isPlainObject(v));
    if (allObjects) {
      const cols = Array.from(new Set(value.flatMap((v) => Object.keys(v))));
      return (
        <table className="data" style={{ width: "100%" }}>
          <thead>
            <tr>
              {cols.map((c) => (
                <th key={c}>{c}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {value.map((row, i) => (
              <tr key={i}>
                {cols.map((c) => (
                  <td key={c}>
                    <Cell value={row[c]} depth={depth + 1} t={t} />
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      );
    }
    if (depth >= MAX_DEPTH) {
      return (
        <ul style={{ margin: 0, paddingLeft: 18 }}>
          {value.map((v, i) => (
            <li key={i}>
              <Cell value={v} depth={depth + 1} t={t} />
            </li>
          ))}
        </ul>
      );
    }
    return (
      <div className="event-list">
        {value.map((v, i) => (
          <div key={i} className="event" style={{ display: "block" }}>
            <Cell value={v} depth={depth + 1} t={t} />
          </div>
        ))}
      </div>
    );
  }

  if (flat) {
    if (depth >= MAX_DEPTH) {
      return (
        <span className="muted">
          {flat.map(([k, v]) => `${k}: ${typeof v === "object" ? "…" : v}`).join(" · ")}
        </span>
      );
    }
    return (
      <table className="data" style={{ width: "100%" }}>
        <tbody>
          {flat.map(([k, v]) => (
            <tr key={k}>
              <th style={{ width: "38%", verticalAlign: "top" }}>{k}</th>
              <td>
                <Cell value={v} depth={depth + 1} t={t} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  }

  return <span className="muted">—</span>;
}