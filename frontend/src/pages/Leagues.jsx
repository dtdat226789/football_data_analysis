import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client.js";
import { useApi } from "../hooks/useApi.js";
import { ErrorBox, ListSkeleton } from "../components/State.jsx";
import { useFormatters } from "../i18n/useFormatters.js";

/** Region headings are translated; the bucket keys themselves are not. */
const REGION_KEYS = {
  europe: "region.europe",
  asia: "region.asia",
  america: "region.america",
  other: "region.other",
};

export default function Leagues() {
  const { t, num } = useFormatters();
  const { data, loading, error } = useApi(() => api.listLeagues(), []);
  const [query, setQuery] = useState("");

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return data || [];
    return (data || []).filter(
      (l) =>
        l.name.toLowerCase().includes(q) ||
        l.country.toLowerCase().includes(q) ||
        (l.region || "").toLowerCase().includes(q),
    );
  }, [data, query]);

  const byRegion = useMemo(() => {
    const buckets = { europe: [], asia: [], america: [], other: [] };
    for (const item of filtered) {
      const region = item.region || "other";
      (buckets[region] || buckets.other).push(item);
    }
    return buckets;
  }, [filtered]);

  const total = filtered.length;

  return (
    <div>
      <div className="page-head">
        <h2>{t("page.leagues.title")}</h2>
        <p>{data ? t("page.leagues.count", { n: data.length }) : "…"}</p>
      </div>

      <div className="filters">
        <input
          type="search"
          aria-label={t("common.searchAria")}
          placeholder={t("page.leagues.search")}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{ minWidth: 260 }}
        />
      </div>

      {loading && <ListSkeleton items={8} />}
      {error && <ErrorBox error={error} />}
      {!loading && !error && total === 0 && (
        <p className="muted">{t("page.leagues.noMatch")}</p>
      )}
      {!loading &&
        !error &&
        Object.entries(byRegion).map(([region, leagues]) =>
          leagues.length === 0 ? null : (
            <section key={region} style={{ marginTop: 24 }}>
              <h3>
                {t(REGION_KEYS[region] ?? "") || region}
                <span className="badge">{leagues.length}</span>
              </h3>
              <div className="mini-grid">
                {leagues.map((item) => (
                  <Link key={item.slug} to={`/leagues/${item.slug}`} className="card mini" style={{ textDecoration: "none" }}>
                    <div className="mini-name">{item.name}</div>
                    <div className="muted" style={{ fontSize: 12 }}>
                      {item.country} · {t("common.teams", { n: num(item.teams) })}
                    </div>
                    {item.has_data && (
                      <div className="badge green" style={{ marginTop: 8 }}>
                        {t("page.leagues.analysis")}
                      </div>
                    )}
                  </Link>
                ))}
              </div>
            </section>
          ),
        )}
    </div>
  );
}