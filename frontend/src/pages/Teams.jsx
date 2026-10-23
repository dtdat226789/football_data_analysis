import { useState } from "react";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { useDebounced } from "../hooks/useDebounced.js";
import { ErrorBox, TableSkeleton } from "../components/State.jsx";
import { TeamLink } from "../components/TeamLink.jsx";
import { pageLabel } from "../lib/pagination.js";
import { useFormatters } from "../i18n/useFormatters.js";

const PAGE_SIZE = 50;

export default function Teams() {
  const { t } = useFormatters();
  const [offset, setOffset] = useState(0);
  const [query, setQuery] = useState("");
  // The registry holds every league at once, so the search runs server-side
  // against all of it. Debounced to keep a request per keystroke from becoming
  // a request per character.
  const q = useDebounced(query.trim(), 250);

  const { data, loading, error } = useApi(
    () => api.teams({ limit: PAGE_SIZE, offset, q: q || undefined }),
    [q, offset],
  );

  const teams = data?.teams || [];
  const total = data?.total ?? 0;
  const searching = q.length > 0;

  // Rewind on every keystroke rather than on the settled query: resetting with
  // the debounced value would leave one request asking for the new term at the
  // old page offset first.
  const onQueryChange = (value) => {
    setQuery(value);
    setOffset(0);
  };

  return (
    <div>
      <div className="page-head">
        <h2>{t("page.teams.title")}</h2>
        <p>
          {data
            ? searching
              ? t("page.teams.matching", { n: total, q })
              : t("page.teams.count", { n: total })
            : "…"}
        </p>
      </div>

      <div className="filters">
        <input
          type="search"
          placeholder={t("page.teams.search")}
          aria-label={t("common.searchAria")}
          value={query}
          onChange={(e) => onQueryChange(e.target.value)}
          style={{ minWidth: 260 }}
        />
      </div>

      {loading && <div className="card"><TableSkeleton rows={10} cols={3} /></div>}
      {error && <ErrorBox error={error} />}
      {!loading && !error && (
        <>
          <div className="card">
            <table className="data">
              <thead>
                <tr>
                  <th>{t("table.rank")}</th>
                  <th>{t("table.team")}</th>
                </tr>
              </thead>
              <tbody>
                {teams.map((t, i) => (
                  <tr key={t.id}>
                    <td className="muted">{offset + i + 1}</td>
                    <td>
                      <TeamLink name={t.canonical_name} />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            {teams.length === 0 && (
              <p className="muted">
                {searching ? t("page.teams.noMatch", { q }) : t("page.teams.empty")}
              </p>
            )}
          </div>

          <div className="pagination">
            <button disabled={offset === 0} onClick={() => setOffset(Math.max(0, offset - PAGE_SIZE))}>
              {t("common.prev")}
            </button>
            <span className="muted">
              {pageLabel(PAGE_SIZE, offset, total, {
                empty: t("pagination.zero"),
                past: t("pagination.past"),
              })}
            </span>
            <button disabled={offset + PAGE_SIZE >= total} onClick={() => setOffset(offset + PAGE_SIZE)}>
              {t("common.next")}
            </button>
          </div>
        </>
      )}
    </div>
  );
}
