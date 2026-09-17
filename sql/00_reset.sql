-- 00 Reset (development) -----------------------------------------------
--
-- Drops every table created by the superseded POC-era schema drafts
-- (sql/01_dims, 02_matches, 03_snapshots, 04_raw_kernel) plus the current
-- design's tables, so the six-step build can run cleanly and repeatedly.
--
-- These legacy tables were empty; drop is safe. Not for use against any
-- environment holding real data.

DROP TABLE IF EXISTS
    countries,
    goal_timing,
    league_seasons,
    leagues,
    match_predictions,
    matches,
    projections,
    raw_payloads,
    seasons,
    standings,
    team_aliases,
    team_league_seasons,
    team_seasons,
    teams,
    track_accuracy,
    track_daily,
    track_market_stats,
    track_picks,
    track_record,
    track_summary
CASCADE;