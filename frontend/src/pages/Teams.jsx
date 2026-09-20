import { useMemo, useState } from "react";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, Loading } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";

const PAGE_SIZE = 50;

export default function Teams() {
  const [offset, setOffset] = useState(0);
  const [query, setQuery] = useState("");

  const { data, loading, error } = useApi(
    () => api.teams({ limit: PAGE_SIZE, offset }),
    [offset],
  );

  const filtered = useMemo(() => {
    const all = data?.teams || [];
    const q = query.trim().toLowerCase();
    if (!q) return all;
    return all.filter(
      (t) => t.canonical_name.toLowerCase().includes(q) || t.canonical_slug.toLowerCase().includes(q),
    );
  }, [data, query]);

  return (
    <div>
      <div className="page-head">
        <h2>Teams</h2>
        <p>{data ? `${data.total} teams in the canonical registry` : "…"}</p>
      </div>

      <div className="filters">
        <input
          type="search"
          placeholder="Filter by name or slug…"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{ minWidth: 260 }}
        />
      </div>

      {loading && <Loading label="Loading teams…" />}
      {error && <ErrorBox error={error} />}
      {!loading && !error && (
        <>
          <div className="card">
            <table className="data">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Team</th>
                  <th>Slug</th>
                </tr>
              </thead>
              <tbody>
                {filtered.map((t, i) => (
                  <tr key={t.id}>
                    <td className="muted">{offset + i + 1}</td>
                    <td>
                      <TeamLink name={t.canonical_name} />
                    </td>
                    <td className="muted">{t.canonical_slug}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            {filtered.length === 0 && <p className="muted">No teams match the filter.</p>}
          </div>

          <div className="pagination">
            <button disabled={offset === 0} onClick={() => setOffset(Math.max(0, offset - PAGE_SIZE))}>
              ‹ Prev
            </button>
            <span className="muted">
              {data.total === 0 ? 0 : offset + 1}–{Math.min(offset + PAGE_SIZE, data.total)} of{" "}
              {data.total}
            </span>
            <button disabled={offset + PAGE_SIZE >= data.total} onClick={() => setOffset(offset + PAGE_SIZE)}>
              Next ›
            </button>
          </div>
        </>
      )}
    </div>
  );
}