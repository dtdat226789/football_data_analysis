export const leagues = [
  { slug: "premier", name: "Premier League", country: "England", region: "europe", teams: 20, has_data: true },
  { slug: "spain1", name: "La Liga", country: "Spain", region: "europe", teams: 20, has_data: true },
  { slug: "japan1", name: "J-League", country: "Japan", region: "asia", teams: 18, has_data: false },
  { slug: "brazil1", name: "Serie A", country: "Brazil", region: "america", teams: 20, has_data: false },
];

export const meta = { default_league: "premier" };

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
  matches: [
    {
      slug: "england/premier-league/2026-02-01-arsenal-vs-chelsea",
      league: "premier",
      country: "England",
      home_team: "Arsenal",
      away_team: "Chelsea",
      match_date: "2026-02-01",
      time: "16:00",
      status: "scheduled",
      predictions: { home: 0.58, away: 0.18, btts_yes: 0.55, over_1_5: 0.82, over_2_5: 0.61, confidence: 0.58, data_through: "2026-01-29" },
    },
    {
      slug: "spain/laliga/2026-02-02-barcelona-vs-madrid",
      league: "spain1",
      country: "Spain",
      home_team: "Barcelona",
      away_team: "Real Madrid",
      match_date: "2026-02-02",
      time: "20:00",
      status: "scheduled",
      predictions: { home: 0.44, away: 0.29, btts_yes: 0.68, over_1_5: 0.8, over_2_5: 0.57, confidence: 0.44, data_through: "2026-01-29" },
    },
  ],
};

export const leagueFixturesPayload = {
  league: "premier",
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
    other: [],
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
  view: "classic",
  seasons: [
    { season: "2023-2024", position: 2, played: 38, won: 26, drawn: 5, lost: 7, goals_for: 88, goals_against: 36, goal_difference: 52, points: 83 },
    { season: "2024-2025", position: 1, played: 38, won: 27, drawn: 4, lost: 7, goals_for: 91, goals_against: 29, goal_difference: 62, points: 85 },
  ],
  totals: { played: 76, won: 53, drawn: 9, lost: 14, goals_for: 179, goals_against: 65, points: 168, ppg: 2.21, goal_difference: 114 },
  home_away: {
    home: { played: 38, won: 30, drawn: 4, lost: 4, goals_for: 103, goals_against: 25, points: 94, win_pct: 78.9 },
    away: { played: 38, won: 23, drawn: 5, lost: 10, goals_for: 76, goals_against: 40, points: 74, win_pct: 60.5 },
  },
  best: { position: 1, position_season: "2024-2025", points: 85 },
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