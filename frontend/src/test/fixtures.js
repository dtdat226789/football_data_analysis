export const leagues = [
  { slug: "premier", name: "Premier League", country: "England", region: "europe", teams: 20, has_data: true },
  { slug: "spain1", name: "La Liga", country: "Spain", region: "europe", teams: 20, has_data: true },
  { slug: "japan1", name: "J-League", country: "Japan", region: "asia", teams: 18, has_data: false },
  { slug: "brazil1", name: "Serie A", country: "Brazil", region: "america", teams: 20, has_data: false },
];

/** Last season has zero matches -> defaults should fall back to 2024-2025. */
export const leagueDetail = {
  name: "Premier League",
  country: "England",
  region: "europe",
  format: "round-robin",
  teams: 20,
  seasons: [
    { season: "2023-2024", start_year: 2023, matches: 380, season_state: "complete" },
    { season: "2024-2025", start_year: 2024, matches: 380, season_state: "complete" },
    { season: "2025-2026", start_year: 2025, matches: 0, season_state: "in_progress" },
  ],
};

export const upcomingFixtures = {
  count: 2,
  total: 2,
  returned: 2,
  limit: 50,
  offset: 0,
  has_more: false,
  sort: "confidence",
  league: null,
  league_name: null,
  min_confidence: null,
  from_date: null,
  to_date: null,
  first_date: "2026-02-01",
  last_date: "2026-02-02",
  dates: ["2026-02-01", "2026-02-02"],
  day_counts: { "2026-02-01": 1, "2026-02-02": 1 },
  matches: [
    {
      slug: "england/premier-league/2026-02-01-arsenal-vs-chelsea",
      league: "premier",
      league_name: "Premier League",
      country: "England",
      home_team: "Arsenal",
      away_team: "Chelsea",
      match_date: "2026-02-01",
      time: "16:00",
      status: "scheduled",
      predictions: {
        home: 0.58, away: 0.18, btts_yes: 0.55, over_1_5: 0.82, over_2_5: 0.61,
        confidence: 0.58, data_through: "2026-01-29",
        selected: [
          { key: "ft.totals.over_1.5", family: "totals", label: "O1.5", scope: "full_time", line: 1.5, selection: "over", probability: 0.8, provenance: "model", promotable: true },
          { key: "ft.asian_handicap.-0.5_away", family: "asian_handicap", label: "Away +0.5", scope: "full_time", line: -0.5, selection: "away", probability: 0.42, provenance: "model", promotable: true },
          { key: "ft.totals.under_2.5", family: "totals", label: "U2.5", scope: "full_time", line: 2.5, selection: "under", probability: 0.41, provenance: "model", promotable: true },
          { key: "ht.result.home", family: "result", label: "1", scope: "half_time", line: null, selection: "home", probability: 0.62, provenance: "modelled", promotable: true },
        ],
      },
    },
    {
      slug: "spain/laliga/2026-02-02-barcelona-vs-madrid",
      league: "spain1",
      league_name: "La Liga",
      country: "Spain",
      home_team: "Barcelona",
      away_team: "Real Madrid",
      match_date: "2026-02-02",
      time: "20:00",
      status: "scheduled",
      predictions: {
        home: 0.44, away: 0.29, btts_yes: 0.68, over_1_5: 0.8, over_2_5: 0.57,
        confidence: 0.44, data_through: "2026-01-29",
        selected: [
          { key: "ft.btts.yes", family: "btts", label: "BTTS yes", scope: "full_time", line: null, selection: "yes", probability: 0.68, provenance: "model", promotable: true },
        ],
      },
    },
  ],
};

export const leagueFixturesPayload = {
  league: "premier",
  league_name: "Premier League",
  count: 1,
  matches: [
    {
      slug: "england/premier-league/2026-02-01-arsenal-vs-chelsea",
      home_team: "Arsenal",
      away_team: "Chelsea",
      match_date: "2026-02-01",
      time: "16:00",
      status: "scheduled",
      country: "England",
      model_predictions: {
        dc_v2: {
          calibrated: { home: 0.58, away: 0.18, btts_yes: 0.55, "over_1.5": 0.82, "over_2.5": 0.61 },
        },
      },
    },
  ],
};

export const recentMatches = {
  count: 2,
  total: 2,
  limit: 50,
  offset: 0,
  matches: [
    {
      api_id: 1001,
      match_date: "2025-01-18",
      season: "2024-2025",
      league: "premier",
      league_name: "Premier League",
      home_team: "Arsenal",
      away_team: "Chelsea",
      home_score: 2,
      away_score: 1,
      home_ht: 1,
      away_ht: 0,
    },
    {
      api_id: 1002,
      match_date: "2025-01-19",
      season: "2024-2025",
      league: "spain1",
      league_name: "La Liga",
      home_team: "Barcelona",
      away_team: "Real Madrid",
      home_score: 0,
      away_score: 0,
      home_ht: 0,
      away_ht: 0,
    },
  ],
};

export const dashboard = {
  meta: { n_leagues: 4, n_upcoming: 2 },
  top_leagues: [
    { slug: "premier", name: "Premier League", country: "England", region: "europe", teams: 20, matches: 2330, has_data: true },
    { slug: "spain1", name: "La Liga", country: "Spain", region: "europe", teams: 20, matches: 2210, has_data: true },
    { slug: "japan1", name: "J-League", country: "Japan", region: "asia", teams: 18, matches: 620, has_data: false },
  ],
  top_clubs: [
    { team: "Arsenal", league: "premier", league_name: "Premier League", season: "2024-2025", position: 1, points: 85, region: "europe" },
    { team: "Barcelona", league: "spain1", league_name: "La Liga", season: "2024-2025", position: 1, points: 82, region: "europe" },
  ],
  recent_matches: recentMatches.matches,
  upcoming_matches: upcomingFixtures.matches,
  leagues_by_region: {
    europe: [
      { slug: "premier", name: "Premier League", country: "England", region: "europe", matches: 2330 },
      { slug: "spain1", name: "La Liga", country: "Spain", region: "europe", matches: 2210 },
    ],
    asia: [{ slug: "japan1", name: "J-League", country: "Japan", region: "asia", matches: 620 }],
    america: [{ slug: "brazil1", name: "Serie A", country: "Brazil", region: "america", matches: 657 }],
    // Non-empty on purpose: the backend buckets algir1/australia/egypt/morocco
    // here, and the dashboard used to drop this bucket entirely.
    other: [{ slug: "australia", name: "A-League", country: "Australia", region: "other", matches: 0 }],
  },
};

export const analysisBundle = {
  has_data: true,
  meta: { name: "Premier League", country: "England", format: "round-robin" },
  reports: {
    matches_analysis: {
      overall: {
        n_matches: 380,
        avg_goals: 2.8,
        home_win_pct: 46.2,
        draw_pct: 23.1,
        away_win_pct: 30.7,
      },
    },
    findings: {
      headline_stats: {
        most_common_scoreline: "1-1",
        dominant_team: "Arsenal",
        champion_most_titles: "Manchester United",
      },
      key_findings: [
        { id: "F-2025-01", finding: "Home advantage is strong", detail: "62% of points scored at home." },
      ],
      anomalies: [{ code: "A-1", message: "February had unusually low scoring." }],
      comparison: [
        { module: "matches_analysis", size_kb: 42.5, sections: ["overall", "home_away"] },
      ],
    },
    season_trends: {
      champions: [{ season: "2024-2025", champion: "Arsenal", champion_pts: 85, margin_pts: 3 }],
    },
  },
  charts: ["avg_goals.png", "home_away.png"],
  missing: [],
};

export function makeStandingsRows(count = 20) {
  const teams = [
    "Arsenal", "Manchester City", "Liverpool", "Chelsea", "Tottenham",
    "Manchester United", "Newcastle United", "Aston Villa", "Brighton & Hove Albion", "West Ham United",
    "Everton", "Wolverhampton Wanderers", "Crystal Palace", "Brentford", "Fulham",
    "Nottingham Forest", "Bournemouth", "Leeds United", "Southampton", "Burnley",
  ];
  return Array.from({ length: count }, (_, i) => ({
    position: i + 1,
    team: teams[i % teams.length],
    played: 38,
    won: 30 - i,
    drawn: 5,
    lost: 3 + i,
    goals_for: 90 - i,
    goals_against: 30 + i,
    goal_difference: 60 - 2 * i,
    points: 95 - 4 * i,
  }));
}

export const standingsClassic = {
  season: "2024-2025",
  view: "classic",
  rows: makeStandingsRows(),
};

export const matchList = {
  season: "2024-2025",
  total: 90,
  matches: [
    {
      api_id: 1001,
      match_date: "2025-01-18",
      home_team: "Arsenal",
      away_team: "Chelsea",
      home_score: 2,
      away_score: 1,
      home_ht: 1,
      away_ht: 0,
    },
    {
      api_id: 1002,
      match_date: "2025-01-19",
      home_team: "Liverpool",
      away_team: "Tottenham",
      home_score: 0,
      away_score: 0,
      home_ht: 0,
      away_ht: 0,
    },
  ],
};

export const matchDetail = {
  api_id: 1001,
  league: "premier",
  league_name: "Premier League",
  season: "2024-2025",
  match_date: "2025-01-18",
  kickoff_time: "15:00",
  game_index: 20,
  home_team: "Arsenal",
  away_team: "Chelsea",
  home_score: 2,
  away_score: 1,
  home_ht: 1,
  away_ht: 0,
  first_goal_time: 20,
};

export const teamsResponse = {
  total: 3,
  teams: [
    { id: 1, canonical_name: "Arsenal", canonical_slug: "arsenal" },
    { id: 2, canonical_name: "Aston Villa", canonical_slug: "aston-villa" },
    { id: 3, canonical_name: "Chelsea", canonical_slug: "chelsea" },
  ],
};

export const teamDetail = {
  team: { id: 1, canonical_name: "Arsenal", canonical_slug: "arsenal" },
  memberships: [
    {
      league: "premier",
      league_name: "Premier League",
      season: "2024-2025",
      start_year: 2024,
      end_year: 2025,
      api_name: "Arsenal",
      api_slug: "arsenal",
      logo_url: "/logos/arsenal.png",
    },
    {
      league: "premier",
      league_name: "Premier League",
      season: "2023-2024",
      start_year: 2023,
      end_year: 2024,
      api_name: "Arsenal",
      api_slug: "arsenal",
    },
  ],
};

export const teamForm = {
  results: [
    { team_result: "W", home_team: "Arsenal", away_team: "Chelsea", home_score: 2, away_score: 1, date: "2025-01-18" },
    { team_result: "D", home_team: "Liverpool", away_team: "Arsenal", home_score: 1, away_score: 1, date: "2025-01-11" },
  ],
};

export const teamStanding = {
  row: { position: 1, won: 22, drawn: 5, lost: 3, goals_for: 70, goals_against: 20, goal_difference: 50, points: 71 },
};

export const teamStatsResponse = {
  team: "arsenal",
  league: "premier",
  league_name: "Premier League",
  view: "classic",
  season: "2024-2025",
  scope: "2024-2025",
  seasons: [
    { season: "2023-2024", position: 2, played: 38, won: 26, drawn: 5, lost: 7, goals_for: 88, goals_against: 36, goal_difference: 52, points: 83 },
    { season: "2024-2025", position: 1, played: 38, won: 27, drawn: 4, lost: 7, goals_for: 91, goals_against: 29, goal_difference: 62, points: 85 },
  ],
  totals: { played: 38, won: 27, drawn: 4, lost: 7, goals_for: 91, goals_against: 29, points: 85, ppg: 2.24, goal_difference: 62 },
  home_away: {
    home: { played: 19, won: 16, drawn: 2, lost: 1, goals_for: 55, goals_against: 14, points: 50, win_pct: 84.2 },
    away: { played: 19, won: 11, drawn: 2, lost: 6, goals_for: 36, goals_against: 15, points: 35, win_pct: 57.9 },
  },
  best: { position: 1, position_season: "2024-2025", points: 85, played: 38 },
};

export function makeModuleBody() {
  return {
    report_name: "matches_analysis",
    script: { name: "analyze_matches", version: "1.0" },
    generated_at: "2025-01-20T10:00:00+00:00",
    league: "premier",
    config: { season: "2024-2025" },
    overall: { n_matches: 380, avg_goals: 2.8 },
    team_rows: [
      { team: "Arsenal", played: 38 },
      { team: "Chelsea", played: 38 },
    ],
  };
}
/** Match insights: pre-match context, model view and head-to-head. */
export const matchInsights = {
  api_id: 1001,
  match: {
    api_id: 1001,
    home_team_id: 1,
    away_team_id: 2,
    home_team: "Arsenal",
    away_team: "Chelsea",
    season: "2024-2025",
    match_date: "2025-01-18",
    game_index: 20,
    home_score: 2,
    away_score: 1,
  },
  pre_match: {
    season: "2024-2025",
    game_index: 20,
    home_team: "Arsenal",
    away_team: "Chelsea",
    home_team_id: 1,
    away_team_id: 2,
    group_labels: {
      form_last_5: "Form (last 5)",
      venue: "Venue split",
      table_before_match: "Table before match",
      rest: "Rest",
    },
    groups: {
      form_last_5: {
        home_team_points_last_5: { label: "Home points (last 5)", value: 10 },
        away_team_points_last_5: { label: "Away points (last 5)", value: 7 },
      },
      venue: {
        home_team_home_win_rate: { label: "Home win rate (home games)", value: 0.7 },
        away_team_away_win_rate: { label: "Away win rate (away games)", value: 0.5 },
      },
      table_before_match: {
        home_position_before_match: { label: "Home position", value: 2 },
        away_position_before_match: { label: "Away position", value: 5 },
      },
      rest: {
        home_rest_days: { label: "Home rest days", value: 4 },
        away_rest_days: { label: "Away rest days", value: 7 },
      },
    },
  },
  model: {
    season: "2024-2025",
    probabilities: { HOME_WIN: 0.55, DRAW: 0.25, AWAY_WIN: 0.2 },
    predicted_match_result: "HOME_WIN",
    confidence: 0.55,
    actual_match_result: "HOME_WIN",
    in_sample: true,
    meta: {
      model_id: "match_result_logistic-v1.1.0",
      feature_version: "1.1.0",
      holdout_seasons: ["2025-2026"],
      in_sample_warning: "Training-season rows are in-sample: the model was fitted on them.",
    },
  },
  head_to_head: {
    limit: 10,
    summary: {
      played: 2,
      home_team_wins: 1,
      draws: 1,
      away_team_wins: 0,
      goals_for: 3,
      goals_against: 1,
    },
    matches: [
      {
        api_id: 900,
        match_date: "2023-12-02",
        season: "2023-2024",
        home_team: "Chelsea",
        away_team: "Arsenal",
        home_score: 2,
        away_score: 2,
      },
      {
        api_id: 901,
        match_date: "2022-08-13",
        season: "2022-2023",
        home_team: "Arsenal",
        away_team: "Chelsea",
        home_score: 1,
        away_score: 0,
      },
    ],
  },
};

/**
/** The markets the backend promoted to chips, as keys into `fixtureMarkets`. */
export const SELECTED_KEYS = [
  "ft.totals.over_1.5",
  "ft.asian_handicap.-0.5_away",
  "ft.totals.under_2.5",
  "ht_ft.home.home",
];

/** A slice of the derived menu, trimmed to what the tests assert on. */
export const fixtureMarkets = [
  { key: "ft.result.home", family: "result", label: "1", scope: "full_time", line: null, selection: "home", probability: 0.58, provenance: "model", promotable: true },
  { key: "ft.result.draw", family: "result", label: "X", scope: "full_time", line: null, selection: "draw", probability: 0.24, provenance: "model", promotable: true },
  { key: "ft.result.away", family: "result", label: "2", scope: "full_time", line: null, selection: "away", probability: 0.18, provenance: "model", promotable: true },
  { key: "ft.double_chance.home_or_draw", family: "double_chance", label: "1X", scope: "full_time", line: null, selection: "home_or_draw", probability: 0.82, provenance: "model", promotable: true },
  { key: "ft.totals.over_1.5", family: "totals", label: "O1.5", scope: "full_time", line: 1.5, selection: "over", probability: 0.8, provenance: "model", promotable: true },
  { key: "ft.totals.under_1.5", family: "totals", label: "U1.5", scope: "full_time", line: 1.5, selection: "under", probability: 0.2, provenance: "model", promotable: true },
  { key: "ft.totals.over_2.5", family: "totals", label: "O2.5", scope: "full_time", line: 2.5, selection: "over", probability: 0.59, provenance: "model", promotable: true },
  { key: "ft.totals.under_2.5", family: "totals", label: "U2.5", scope: "full_time", line: 2.5, selection: "under", probability: 0.41, provenance: "model", promotable: true },
  { key: "ft.btts.yes", family: "btts", label: "BTTS yes", scope: "full_time", line: null, selection: "yes", probability: 0.55, provenance: "model", promotable: true },
  { key: "ft.btts.no", family: "btts", label: "BTTS no", scope: "full_time", line: null, selection: "no", probability: 0.45, provenance: "model", promotable: true },
  { key: "ft.asian_handicap.-0.5_home", family: "asian_handicap", label: "Home -0.5", scope: "full_time", line: -0.5, selection: "home", probability: 0.58, push: 0, provenance: "model", promotable: true },
  { key: "ft.asian_handicap.-0.5_away", family: "asian_handicap", label: "Away +0.5", scope: "full_time", line: -0.5, selection: "away", probability: 0.42, provenance: "model", promotable: true },
  { key: "ft.asian_handicap.-1_home", family: "asian_handicap", label: "Home -1", scope: "full_time", line: -1, selection: "home", probability: 0.31, push: 0.27, provenance: "model", promotable: true },
  { key: "ft.asian_handicap.-1_away", family: "asian_handicap", label: "Away +1", scope: "full_time", line: -1, selection: "away", probability: 0.42, provenance: "model", promotable: true },
  { key: "ft.team_total.home.over_1.5", family: "team_total", label: "Home O1.5", scope: "full_time", line: 1.5, selection: "home", probability: 0.64, provenance: "model", promotable: false },
  { key: "ft.correct_score.2_1", family: "correct_score", label: "2-1", scope: "full_time", line: null, selection: "home_away", probability: 0.09, provenance: "model", promotable: false },
  { key: "ft.correct_score.1_1", family: "correct_score", label: "1-1", scope: "full_time", line: null, selection: "home_away", probability: 0.11, provenance: "model", promotable: false },
  { key: "ht.result.home", family: "result", label: "1", scope: "half_time", line: null, selection: "home", probability: 0.41, provenance: "modelled", promotable: true },
  { key: "ht.totals.over_0.5", family: "totals", label: "O0.5", scope: "half_time", line: 0.5, selection: "over", probability: 0.62, provenance: "modelled", promotable: true },
  { key: "ht_ft.home.home", family: "ht_ft", label: "1/1", scope: "half_to_full", line: null, selection: "home_home", probability: 0.24, provenance: "modelled", promotable: false },
  { key: "ht_ft.draw.draw", family: "ht_ft", label: "X/X", scope: "half_to_full", line: null, selection: "draw_draw", probability: 0.06, provenance: "modelled", promotable: false },
];

/**
 * GET /fixtures/premier/{tail} — an unplayed fixture with everything the detail
 * page renders: full dc_v2 block, kickoff metadata, logos, form, matchday, the
 * pre-match panel and head-to-head.
 */
export const fixtureDetail = {
  league: "premier",
  league_name: "Premier League",
  match_id: "2026-02-01-arsenal-vs-chelsea",
  slug: "england/premier-league/2026-02-01-arsenal-vs-chelsea",
  country: "England",
  real_league_name: "Premier League",
  status: "scheduled",
  match_date: "2026-02-01",
  season: "2025-2026",
  season_state: "in_progress",
  matchday: 25,
  detail_collected: true,
  teams: {
    home: {
      name: "Arsenal",
      team_id: 1,
      logo: "https://cdn.example/arsenal.png",
      form_line: ["W", "D", "W", "W", "L"],
      rest_days: 4,
      games_before: 24,
      venue: { played: 12, wins: 8, draws: 2, losses: 2, goals_for: 22, goals_against: 9, win_rate: 0.6667, goals_avg: 1.833, conceded_avg: 0.75 },
      form: [
        { date: "2026-01-25", home_team: "Arsenal", away_team: "Liverpool", home_score: 2, away_score: 1, team_result: "W", points: 3 },
        { date: "2026-01-18", home_team: "Everton", away_team: "Arsenal", home_score: 1, away_score: 1, team_result: "D", points: 1 },
        { date: "2026-01-11", home_team: "Arsenal", away_team: "Newcastle", home_score: 3, away_score: 0, team_result: "W", points: 3 },
        { date: "2026-01-04", home_team: "Arsenal", away_team: "Brighton", home_score: 2, away_score: 1, team_result: "W", points: 3 },
        { date: "2025-12-28", home_team: "Man City", away_team: "Arsenal", home_score: 3, away_score: 0, team_result: "L", points: 0 },
      ],
    },
    away: {
      name: "Chelsea",
      team_id: 2,
      logo: "https://cdn.example/chelsea.png",
      form_line: ["D", "W", "L", "D", "D"],
      rest_days: 7,
      games_before: 24,
      venue: { played: 12, wins: 6, draws: 3, losses: 3, goals_for: 16, goals_against: 14, win_rate: 0.5, goals_avg: 1.333, conceded_avg: 1.167 },
      form: [
        { date: "2026-01-22", home_team: "Chelsea", away_team: "Wolves", home_score: 1, away_score: 1, team_result: "D", points: 1 },
        { date: "2026-01-15", home_team: "Notts Forest", away_team: "Chelsea", home_score: 0, away_score: 2, team_result: "W", points: 3 },
        { date: "2026-01-08", home_team: "Chelsea", away_team: "Arsenal", home_score: 1, away_score: 3, team_result: "L", points: 0 },
      ],
    },
  },
  standings: {
    home: { position: 2, played: 24, won: 18, drawn: 3, lost: 3, goals_for: 52, goals_against: 21, goal_difference: 31, points: 57 },
    away: { position: 5, played: 24, won: 13, drawn: 5, lost: 6, goals_for: 41, goals_against: 29, goal_difference: 12, points: 44 },
  },
  kickoff: {
    time: "16:00",
    match_datetime: "2026-02-01T16:00:00+00:00",
    label: "Matchday 25",
    league_phase_status: "regular_season",
    portal_link: "https://football-charts.com/england/premier-league/2026-02-01-arsenal-vs-chelsea",
  },
  predictability: {
    model: "dc_v2.0",
    xi: 0.0019,
    sigma: 0.5,
    data_through: "2026-01-29",
    computed_at: "2026-01-30T09:00:00+00:00",
    summary: {
      home: 0.58, away: 0.18, btts_yes: 0.55,
      over_1_5: 0.82, over_2_5: 0.61, over_3_5: 0.3,
      expected_home_goals: 1.82, expected_away_goals: 0.94,
      confidence: 0.58, computed_at: "2026-01-30T09:00:00+00:00", data_through: "2026-01-29",
    },
    probabilities: { home: 0.58, draw: 0.24, away: 0.18 },
    expected_goals: { home: 1.82, away: 0.94, half_time_total: 0.98 },
    lines: [
      { line: "over_1.5", scope: "full_time", threshold: "1.5", raw: 0.8, calibrated: 0.82 },
      { line: "over_2.5", scope: "full_time", threshold: "2.5", raw: 0.59, calibrated: 0.61 },
      { line: "ht_over_0.5", scope: "half_time", threshold: "0.5", raw: 0.5, calibrated: 0.51 },
    ],
    markets: fixtureMarkets,
    selected: fixtureMarkets.filter((m) => SELECTED_KEYS.includes(m.key)),
    ratings: { home: { attack: 0.42, defence: 0.31 }, away: { attack: -0.12, defence: -0.08 } },
    effective_matches: { home: 34.6, away: 15.6 },
    gates: { leans: false, probabilities: true },
    data_status: { stale: false, matches_behind: 0 },
  },
  pre_match: matchInsights.pre_match,
  head_to_head: matchInsights.head_to_head,
};

/** Same fixture before any /matches/{slug}/ payload was collected. */
export const fixtureDetailNoHistory = {
  ...fixtureDetail,
  detail_collected: false,
  season: null,
  season_state: null,
  matchday: null,
  pre_match: null,
  head_to_head: null,
  standings: { home: null, away: null },
  teams: {
    home: { ...fixtureDetail.teams.home, logo: null, form: [], form_line: [], rest_days: null, games_before: null, venue: null },
    away: { ...fixtureDetail.teams.away, logo: null, form: [], form_line: [], rest_days: null, games_before: null, venue: null },
  },
  kickoff: { time: "16:00", match_datetime: null, label: null, league_phase_status: null, portal_link: null },
  predictability: null,
};

/**
 * GET /fixtures/premier/{tail}?market=<key> — the mechanism behind one derived
 * market. Two shapes are represented because they are genuinely different: a
 * scoreline market carries the cells that pay it, and HT/FT carries the two
 * 1X2 splits it multiplies together instead.
 */
export const marketDetail = {
  league: "premier",
  league_name: "Premier League",
  match_id: "2026-02-01-arsenal-vs-chelsea",
  slug: "england/premier-league/2026-02-01-arsenal-vs-chelsea",
  market_key: "ft.asian_handicap.-1_home",
  market: {
    key: "ft.asian_handicap.-1_home",
    family: "asian_handicap",
    label: "Home -1",
    scope: "full_time",
    line: -1,
    selection: "home",
    provenance: "model",
    promotable: true,
    settlement: { win: 0.31, push: 0.27, lose: 0.42 },
    cells: [
      { home_goals: 2, away_goals: 0, score: "2-0", probability: 0.1412, share: 0.4555, outcome: "win" },
      { home_goals: 1, away_goals: 0, score: "1-0", probability: 0.1354, share: 0.4368, outcome: "push" },
      { home_goals: 2, away_goals: 1, score: "2-1", probability: 0.1011, share: 0.3261, outcome: "win" },
      { home_goals: 1, away_goals: 1, score: "1-1", probability: 0.0936, share: 0.3458, outcome: "lose" },
    ],
    grid_cells: 81,
    paying_cells: 4,
    method: "the scorelines that settle this line, splitting any quarter line into its two half-stakes",
  },
};

/** A level Asian handicap: the scorelines that pay it, and the refund. */
export const marketDetailQuarter = {
  ...marketDetail,
  market_key: "ft.asian_handicap.-0.25_home",
  market: {
    ...marketDetail.market,
    key: "ft.asian_handicap.-0.25_home",
    label: "Home -0.25",
    line: -0.25,
    settlement: { win: 0.5, push: 0.1197, lose: 0.3803 },
    cells: [
      { home_goals: 1, away_goals: 0, score: "1-0", probability: 0.1354, share: 0.5, outcome: "win" },
      { home_goals: 1, away_goals: 1, score: "1-1", probability: 0.0936, share: 0.472, outcome: "push+lose" },
    ],
    paying_cells: 2,
  },
};

/** HT/FT has no scorelines: it multiplies the two halves' own 1X2 splits. */
export const marketDetailHalfToFull = {
  ...marketDetail,
  market_key: "ht_ft.home.home",
  market: {
    ...marketDetail.market,
    key: "ht_ft.home.home",
    family: "ht_ft",
    label: "1/1",
    scope: "half_to_full",
    line: null,
    selection: "home_home",
    provenance: "modelled",
    settlement: { win: 0.24, push: 0.0, lose: 0.76 },
    cells: [],
    grid_cells: 0,
    paying_cells: 0,
    factors: {
      half_time: { home: 0.41, draw: 0.34, away: 0.25 },
      full_time: { home: 0.58, draw: 0.24, away: 0.18 },
      half_time_side: "home",
      full_time_side: "home",
    },
    method: "the half-time result and the full-time result, treated as independent",
  },
};
