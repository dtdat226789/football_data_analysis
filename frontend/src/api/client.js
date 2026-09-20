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
    throw new ApiError(0, "Cannot reach the API server. Is uvicorn running on :8000?");
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
  meta: () => request("/meta"),
  listLeagues: () => request("/leagues"),
  league: (league) => request(`/leagues/${league}`),
  seasons: (league) => request(`/leagues/${league}/seasons`),
  standings: (league, { season, view } = {}) =>
    request(`/leagues/${league}/standings`, { season, view }),
  matches: (league, params = {}) => request(`/leagues/${league}/matches`, params),
  match: (apiId) => request(`/matches/${apiId}`),
  teams: ({ limit, offset } = {}) => request("/teams", { limit, offset }),
  team: (slug) => request(`/teams/${slug}`),
  teamMatches: (slug, params = {}) => request(`/teams/${slug}/matches`, params),
  teamForm: (slug, params = {}) => request(`/teams/${slug}/form`, params),
  teamStandings: (slug, params = {}) => request(`/teams/${slug}/standings`, params),
  analysis: (league) => request(`/analysis/${league}`),
  analysisModule: (league, module) => request(`/analysis/${league}/${module}`),
  chartUrl: (league, chart) => `/api/v1/analysis/${league}/charts/${chart}`,
};

export { request };