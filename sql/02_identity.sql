-- 02 Identity
--
-- Physical club identity. The API exposes no stable team id (teams.json rows
-- carry none; table row ids are season-scoped), so we manage our own surrogate
-- teams.id. API names/slugs are preserved verbatim at the season level via
-- team_seasons; team_aliases is the identity bridge that resolves any observed
-- name/slug spelling back to a single team id.
--
-- Idempotent; safe to re-run.

CREATE TABLE IF NOT EXISTS teams (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    canonical_name  TEXT NOT NULL,               -- current/latest display name
    canonical_slug  TEXT NOT NULL,               -- current/latest slug
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS team_aliases (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    team_id     BIGINT NOT NULL REFERENCES teams (id),
    form        TEXT NOT NULL,                   -- 'name' | 'slug'
    value       TEXT NOT NULL,                   -- observed spelling
    source      TEXT,                            -- 'api_seed' | 'manual' | 'etl_resolution'
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    CONSTRAINT team_aliases_form CHECK (form IN ('name', 'slug')),
    CONSTRAINT team_aliases_value UNIQUE (form, value)
);

CREATE TABLE IF NOT EXISTS team_seasons (
    league_season_id BIGINT NOT NULL REFERENCES league_seasons (id),
    team_id          BIGINT NOT NULL REFERENCES teams (id),
    api_name         TEXT NOT NULL,              -- original API name for this (league, season)
    api_slug         TEXT NOT NULL,              -- original API slug for this (league, season)
    logo_url         TEXT,
    PRIMARY KEY (league_season_id, team_id)
);

CREATE INDEX IF NOT EXISTS team_seasons_team_idx ON team_seasons (team_id);
CREATE INDEX IF NOT EXISTS team_seasons_slug_idx ON team_seasons (api_slug);
CREATE INDEX IF NOT EXISTS team_aliases_team_idx ON team_aliases (team_id);