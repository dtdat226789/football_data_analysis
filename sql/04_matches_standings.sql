-- 04 Matches + Standings
--
-- matches: upstream match.id treated as the natural PK (validated globally
-- unique and stable across 6 premiere seasons). Home/away reference season
-- memberships via composite FKs (league_season_id, team_id) -> team_seasons,
-- which also pins both legs to the *same* league+season as the match,
-- declaratively and trigger-free.
--
-- standings: the published league table per team/season/view. Classic core
-- analytical fields are real columns; everything else from the upstream row
-- is preserved verbatim in metrics (JSONB) for reproducibility.
--
-- first_goal_time_extra keeps NULL semantics verified against the data:
-- NULL = goalless (no first goal exists); 0 = first goal in normal time.
-- No NULL->0 conversion is applied.
--
-- Idempotent; safe to re-run.

CREATE TABLE IF NOT EXISTS matches (
    api_id                BIGINT PRIMARY KEY,    -- upstream match id (natural key)
    league_season_id      BIGINT  NOT NULL REFERENCES league_seasons (id),
    game_index            INTEGER NOT NULL,      -- season-local ordinal (NOT globally unique)
    home_team_id          BIGINT  NOT NULL,
    away_team_id          BIGINT  NOT NULL,
    match_date            DATE    NOT NULL,
    kickoff_time          TIME    NOT NULL,
    home_score            SMALLINT NOT NULL,     -- FT goals (parsed 'score')
    away_score            SMALLINT NOT NULL,
    home_ht               SMALLINT,              -- HT goals (parsed 'ht_result'); null together
    away_ht               SMALLINT,
    first_goal_time       SMALLINT,              -- minute of first goal; null iff goalless
    first_goal_time_extra SMALLINT,              -- stoppage-time beyond first_goal_time; null iff goalless
    created_at            TIMESTAMPTZ NOT NULL DEFAULT now(),
    CONSTRAINT matches_game_index UNIQUE (league_season_id, game_index),
    CONSTRAINT matches_no_self CHECK (home_team_id <> away_team_id),
    CONSTRAINT matches_scores_nonneg CHECK (home_score >= 0 AND away_score >= 0),
    CONSTRAINT matches_ht_pairs CHECK ((home_ht IS NULL) = (away_ht IS NULL)),
    CONSTRAINT matches_ht_le_ft CHECK (home_ht IS NULL OR home_ht <= home_score),
    CONSTRAINT matches_at_le_ft CHECK (away_ht IS NULL OR away_ht <= away_score),
    CONSTRAINT matches_fgt_goalless CHECK ((first_goal_time IS NULL) = (home_score = 0 AND away_score = 0)),
    CONSTRAINT matches_fgt_range CHECK (first_goal_time IS NULL OR first_goal_time BETWEEN 1 AND 120),
    CONSTRAINT matches_fgte_mirrors_fgt CHECK ((first_goal_time IS NULL) = (first_goal_time_extra IS NULL)),
    CONSTRAINT matches_fgte_range CHECK (first_goal_time_extra IS NULL OR first_goal_time_extra >= 0),
    CONSTRAINT matches_home_membership FOREIGN KEY (league_season_id, home_team_id)
        REFERENCES team_seasons (league_season_id, team_id),
    CONSTRAINT matches_away_membership FOREIGN KEY (league_season_id, away_team_id)
        REFERENCES team_seasons (league_season_id, team_id)
);

-- FK-support indexes on the composite membership columns.
CREATE INDEX IF NOT EXISTS matches_season_home_idx ON matches (league_season_id, home_team_id);
CREATE INDEX IF NOT EXISTS matches_season_away_idx ON matches (league_season_id, away_team_id);

CREATE TABLE IF NOT EXISTS standings (
    league_season_id  BIGINT    NOT NULL,
    team_id           BIGINT    NOT NULL,
    view              TEXT      NOT NULL,
    position          SMALLINT  NOT NULL,        -- view-specific ranking (only field that varies per view)
    played            SMALLINT  NOT NULL,
    won               SMALLINT  NOT NULL,
    drawn             SMALLINT  NOT NULL,
    lost              SMALLINT  NOT NULL,
    goals_for         SMALLINT  NOT NULL,
    goals_against     SMALLINT  NOT NULL,
    goal_difference   SMALLINT  NOT NULL,
    points            SMALLINT  NOT NULL,
    metrics           JSONB     NOT NULL,         -- specialized API metrics + upstream meta, verbatim
    captured_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (league_season_id, team_id, view),
    CONSTRAINT standings_view CHECK (view IN ('classic', 'luck', 'goals')),
    CONSTRAINT standings_position CHECK (position >= 1),
    CONSTRAINT standings_counts CHECK (played >= 0 AND won >= 0 AND drawn >= 0 AND lost >= 0),
    CONSTRAINT standings_goals CHECK (goals_for >= 0 AND goals_against >= 0),
    CONSTRAINT standings_gd CHECK (goal_difference = goals_for - goals_against),
    CONSTRAINT standings_points CHECK (points = 3 * won + drawn),
    CONSTRAINT standings_metrics CHECK (jsonb_typeof(metrics) = 'object'),
    CONSTRAINT standings_membership FOREIGN KEY (league_season_id, team_id)
        REFERENCES team_seasons (league_season_id, team_id)
);