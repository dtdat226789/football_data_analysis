-- 06 Index tuning
--
-- Analytical indexes for SQL analysis and ML feature generation
-- (chronological windows, form/streak joins, standings lookups).
-- Idempotent; safe to re-run.

CREATE INDEX IF NOT EXISTS matches_date_idx        ON matches (match_date);
CREATE INDEX IF NOT EXISTS matches_season_date_idx ON matches (league_season_id, match_date);
CREATE INDEX IF NOT EXISTS matches_home_form_idx   ON matches (home_team_id, match_date);
CREATE INDEX IF NOT EXISTS matches_away_form_idx   ON matches (away_team_id, match_date);
CREATE INDEX IF NOT EXISTS standings_view_pos_idx  ON standings (league_season_id, view, position);
CREATE INDEX IF NOT EXISTS standings_team_idx      ON standings (team_id);