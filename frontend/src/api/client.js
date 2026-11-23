import { currentRequestSignal } from "../lib/requestSignal.js";
import { isValidChartName } from "../lib/safeUrl.js";

const BASE = "/api/v1";
const REQUEST_TIMEOUT_MS = 15_000;

function requestSignal(explicit) {
  const timeout = AbortSignal.timeout(REQUEST_TIMEOUT_MS);
  const signal = explicit || currentRequestSignal();
  if (!signal) return timeout;
  return typeof AbortSignal.any === "function"
    ? AbortSignal.any([signal, timeout])
    : signal;
}

const segment = (value) => encodeURIComponent(String(value));

async function request(path, params = {}) {
  const { signal, ...query } = params || {};
  const url = new URL(BASE + path, window.location.origin);
  for (const [key, value] of Object.entries(query)) {
    if (value !== undefined && value !== null && value !== "") {
      url.searchParams.set(key, String(value));
    }
  }
  let res;
  try {
    res = await fetch(url.toString(), { signal: requestSignal(signal) });
  } catch (error) {
    if (error?.name === "TimeoutError") {
      throw new ApiError(504, "The API server took too long to respond.");
    }
    if (error?.name === "AbortError") {
      throw new ApiError(499, "Request cancelled.");
    }
    throw new ApiError(0, "Cannot reach the API server. Is the backend running?");
  }
  if (!res.ok) {
    let detail = res.statusText;
    const body = await res.json().catch(() => null);
    if (body) detail = body.detail || JSON.stringify(body);
    throw new ApiError(res.status, detail);
  }
  return res.json();
}

export class ApiError extends Error {
  constructor(status, message) {
    super(message);
    this.name = "ApiError";
    this.status = status;
  }
}

export const api = {
  health: () => request("/health"),
  listLeagues: () => request("/leagues"),
  league: (league) => request(`/leagues/${segment(league)}`),
  leagueSeasons: (league) => request(`/leagues/${segment(league)}/seasons`),
  standings: (league, { season, view } = /** @type {{ season?: string, view?: string }} */ ({})) =>
    request(`/leagues/${segment(league)}/standings`, { season, view }),
  matches: (league, params = {}) => request(`/leagues/${segment(league)}/matches`, params),
  match: (apiId) => request(`/matches/${segment(apiId)}`),
  matchInsights: (apiId, params = {}) => request(`/matches/${segment(apiId)}/insights`, params),
  matchesRecent: (params = /** @type {Record<string, any>} */ ({})) => request("/matches/recent", params),
  dashboard: () => request("/dashboard"),
  fixtures: (params = /** @type {Record<string, any>} */ ({})) => request("/fixtures", params),
  leagueFixtures: (league) => request(`/fixtures/${segment(league)}`),
  // matchId is the trailing `date-home-vs-away` slug segment, or the full
  // upstream slug when the caller has it; the route accepts either.
  fixtureDetail: (league, matchId) => request(`/fixtures/${segment(league)}/${segment(matchId)}`),
  // The mechanism behind one derived projection: how it is counted and which
  // scorelines count for it. Same route as fixtureDetail, narrowed by query.
  fixtureProjection: (league, matchId, projectionKey) =>
    request(`/fixtures/${segment(league)}/${segment(matchId)}`, { projection: projectionKey }),
  teams: ({ limit, offset, q } = /** @type {{ limit?: number, offset?: number, q?: string }} */ ({})) =>
    request("/teams", { limit, offset, q }),
  team: (slug) => request(`/teams/${segment(slug)}`),
  teamMatches: (slug, params = {}) => request(`/teams/${segment(slug)}/matches`, params),
  teamForm: (slug, params = {}) => request(`/teams/${segment(slug)}/form`, params),
  teamStandings: (slug, params = {}) => request(`/teams/${segment(slug)}/standings`, params),
  teamStats: (slug, params = {}) => request(`/teams/${segment(slug)}/stats`, params),
  teamKpi: (slug, params = {}) => request(`/teams/${segment(slug)}/kpi`, params),
  clubAnalysis: (params = {}) => request("/club-analysis", params),
  analysis: (league) => request(`/analysis/${segment(league)}`),
  chartUrl: (league, chart) =>
    isValidChartName(chart) ? `${BASE}/analysis/${segment(league)}/charts/${chart}` : null,
};

export { request };
