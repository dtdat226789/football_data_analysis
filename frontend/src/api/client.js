const BASE = "/api/v1";

export class ApiError extends Error {
  constructor(status, message) {
    super(message);
    this.name = "ApiError";
    this.status = status;
  }
}

async function request(path, params = {}) {
  const url = new URL(BASE + path, window.location.origin);
  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined && value !== null && value !== "") {
      url.searchParams.set(key, String(value));
    }
  }
  let res;
  try {
    res = await fetch(url.toString());
  } catch {
    throw new ApiError(0, "Cannot reach the API server. Is the backend running?");
  }
  if (!res.ok) {
    let detail = res.statusText;
    try {
      const body = await res.json();
      detail = body.detail || JSON.stringify(body);
    } catch {
      /* keep statusText */
    }
    throw new ApiError(res.status, detail);
  }
  return res.json();
}

export const api = {
  health: () => request("/health"),
  listLeagues: () => request("/leagues"),
  league: (league) => request(`/leagues/${league}`),
  standings: (league, { season, view } = /** @type {{ season?: string, view?: string }} */ ({})) =>
    request(`/leagues/${league}/standings`, { season, view }),
  matches: (league, params = {}) => request(`/leagues/${league}/matches`, params),
  match: (apiId) => request(`/matches/${apiId}`),
  matchInsights: (apiId, params = {}) => request(`/matches/${apiId}/insights`, params),
  matchesRecent: (params = /** @type {Record<string, any>} */ ({})) => request("/matches/recent", params),
  dashboard: () => request("/dashboard"),
  fixtures: (params = /** @type {Record<string, any>} */ ({})) => request("/fixtures", params),
  leagueFixtures: (league) => request(`/fixtures/${league}`),
  // matchId is the trailing `date-home-vs-away` slug segment, or the full
  // upstream slug when the caller has it; the route accepts either.
  fixtureDetail: (league, matchId) => request(`/fixtures/${league}/${matchId}`),
  // The mechanism behind one derived market: how it settles and which scorelines
  // pay it. Same route as fixtureDetail, so `market` keys off the fixture rather
  // than adding a second path that could collide with the `:path` match id.
  fixtureMarket: (league, matchId, marketKey) =>
    request(`/fixtures/${league}/${matchId}`, { market: marketKey }),
  teams: ({ limit, offset, q } = /** @type {{ limit?: number, offset?: number, q?: string }} */ ({})) =>
    request("/teams", { limit, offset, q }),
  team: (slug) => request(`/teams/${slug}`),
  teamMatches: (slug, params = {}) => request(`/teams/${slug}/matches`, params),
  teamForm: (slug, params = {}) => request(`/teams/${slug}/form`, params),
  teamStandings: (slug, params = {}) => request(`/teams/${slug}/standings`, params),
  teamStats: (slug, params = {}) => request(`/teams/${slug}/stats`, params),
  analysis: (league) => request(`/analysis/${league}`),
  chartUrl: (league, chart) => `/api/v1/analysis/${league}/charts/${chart}`,
};

export { request };