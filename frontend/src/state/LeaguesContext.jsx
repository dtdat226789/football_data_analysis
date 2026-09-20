import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { api } from "../api/client.js";

const LeaguesContext = createContext(null);

export function LeaguesProvider({ children }) {
  const [leagues, setLeagues] = useState([]);
  const [meta, setMeta] = useState(null);
  const [selectedLeague, setSelectedLeague] = useState(null);
  const [selectedSeason, setSelectedSeason] = useState(null);
  const [detail, setDetail] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    let alive = true;
    Promise.all([api.listLeagues(), api.meta()])
      .then(([list, m]) => {
        if (!alive) return;
        setLeagues(list);
        setMeta(m);
        const preferred = m?.default_league && list.some((l) => l.slug === m.default_league)
          ? m.default_league
          : list[0]?.slug;
        setSelectedLeague((cur) => cur || preferred || null);
      })
      .catch((e) => alive && setError(e.message));
    return () => {
      alive = false;
    };
  }, []);

  useEffect(() => {
    if (!selectedLeague) return;
    setDetail(null);
    let alive = true;
    api
      .league(selectedLeague)
      .then((d) => {
        if (!alive) return;
        setDetail(d);
        setSelectedSeason((cur) => {
          const seasons = d.seasons || [];
          if (seasons.length === 0) return cur;
          if (cur && seasons.some((s) => s.season === cur)) return cur;
          const withMatches = seasons.filter((s) => s.matches > 0);
          const pool = withMatches.length ? withMatches : seasons;
          return pool[pool.length - 1].season;
        });
      })
      .catch((e) => alive && setError(e.message));
    return () => {
      alive = false;
    };
  }, [selectedLeague]);

  const seasons = useMemo(
    () => (detail?.seasons ? [...detail.seasons].sort((a, b) => a.start_year - b.start_year) : []),
    [detail],
  );
  const latestSeason = useMemo(() => {
    const withMatches = seasons.filter((s) => s.matches > 0);
    const pool = withMatches.length ? withMatches : seasons;
    return pool.length ? pool[pool.length - 1].season : null;
  }, [seasons]);

  const value = {
    leagues,
    meta,
    league: selectedLeague,
    setLeague: setSelectedLeague,
    season: selectedSeason,
    setSeason: setSelectedSeason,
    seasons,
    latestSeason,
    detail,
    error,
  };
  return <LeaguesContext.Provider value={value}>{children}</LeaguesContext.Provider>;
}

export function useLeagues() {
  return useContext(LeaguesContext);
}