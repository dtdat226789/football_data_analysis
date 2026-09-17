-- 01 Registry
--
-- Reference/registry tables: leagues (catalog), seasons (global dictionary)
-- and league_seasons (our own historical (league, season) registry that the
-- upstream /leagues/ endpoint cannot provide; it only declares current+previous).
--
-- Idempotent; safe to re-run.

CREATE TABLE IF NOT EXISTS leagues (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    api_key     TEXT NOT NULL UNIQUE,           -- upstream league key, e.g. 'premier'
    name        TEXT NOT NULL,                   -- display name, e.g. 'Premier League'
    country     TEXT,                            -- from /leagues/
    url         TEXT,                            -- site URL
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS seasons (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name        TEXT NOT NULL UNIQUE,            -- opaque API season string, e.g. '2020-2021', '2026'
    start_year  SMALLINT,
    end_year    SMALLINT,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    CONSTRAINT seasons_year_order CHECK (end_year IS NULL OR start_year IS NULL OR end_year >= start_year)
);

CREATE TABLE IF NOT EXISTS league_seasons (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    league_id        BIGINT NOT NULL REFERENCES leagues (id),
    season_id        BIGINT NOT NULL REFERENCES seasons (id),
    declared_by_api  BOOLEAN NOT NULL DEFAULT false,   -- SEASON_NOT_DECLARED fact
    season_state     TEXT NOT NULL DEFAULT 'unknown',  -- 'complete' | 'in_progress' | 'unknown'
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    CONSTRAINT league_seasons_pair UNIQUE (league_id, season_id),
    CONSTRAINT league_seasons_state CHECK (season_state IN ('complete', 'in_progress', 'unknown'))
);