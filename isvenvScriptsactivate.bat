[1mdiff --git a/.gitattributes b/.gitattributes[m
[1mnew file mode 100644[m
[1mindex 0000000..5248f09[m
[1m--- /dev/null[m
[1m+++ b/.gitattributes[m
[36m@@ -0,0 +1,14 @@[m
[32m+[m[32m# Normalize line endings in the repository.[m
[32m+[m[32m#[m
[32m+[m[32m# Why: the working tree lives on a Windows drive and generated reports[m
[32m+[m[32m# (data/analysis/**, data/validation/**) were written with CRLF. Because the[m
[32m+[m[32m# index stored LF, every one of those files showed as modified even when the[m
[32m+[m[32m# content was byte-identical, which left `git status` permanently dirty with[m
[32m+[m[32m# ~1488 phantom changes and buried real work.[m
[32m+[m[32m#[m
[32m+[m[32m# `text=auto` normalizes to LF in the index; `eol=lf` checks LF back out.[m
[32m+[m[32m# Git auto-detects binaries and leaves them alone, but the png rule is kept[m
[32m+[m[32m# explicitly so image assets can never be mangled by content sniffing.[m
[32m+[m[32m* text=auto eol=lf[m
[32m+[m
[32m+[m[32m*.png binary[m
[1mdiff --git a/backend/scripts/etl_03_matches_standings.py b/backend/scripts/etl_03_matches_standings.py[m
[1mindex 6a1b006..9f6fb4e 100644[m
[1m--- a/backend/scripts/etl_03_matches_standings.py[m
[1m+++ b/backend/scripts/etl_03_matches_standings.py[m
[36m@@ -9,6 +9,12 @@[m [mfirst_goal_time_extra is stored with its validated semantics: NULL when the[m
 match is goalless (no first goal exists), an integer >= 0 otherwise (0 = first[m
 goal in normal time). No NULL->0 conversion.[m
 [m
[32m+[m[32mRe-running refreshes rows: the matches upsert is DO UPDATE (matching the other[m
[32m+[m[32mfive), so a corrected upstream result replaces the stale one. Cancelled and[m
[32m+[m[32mawarded matches are skipped before insert, so a match that *becomes* one is[m
[32m+[m[32mneither updated nor removed - the schema has no status column to represent it.[m
[32m+[m[32mThat is a pre-existing gap, not a consequence of the upsert.[m
[32m+[m
 Usage:[m
     python backend/scripts/etl_03_matches_standings.py[m
     python backend/scripts/etl_03_matches_standings.py --league spain1[m
[36m@@ -135,7 +141,19 @@[m [mdef load_matches(cur, league_season_id: int, season: str, league: str) -> tuple[[m
                 home_score, away_score, home_ht, away_ht,[m
                 first_goal_time, first_goal_time_extra[m
             ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)[m
[31m-            ON CONFLICT (api_id) DO NOTHING[m
[32m+[m[32m            ON CONFLICT (api_id) DO UPDATE SET[m
[32m+[m[32m                league_season_id = EXCLUDED.league_season_id,[m
[32m+[m[32m                game_index = EXCLUDED.game_index,[m
[32m+[m[32m                home_team_id = EXCLUDED.home_team_id,[m
[32m+[m[32m                away_team_id = EXCLUDED.away_team_id,[m
[32m+[m[32m                match_date = EXCLUDED.match_date,[m
[32m+[m[32m                kickoff_time = EXCLUDED.kickoff_time,[m
[32m+[m[32m                home_score = EXCLUDED.home_score,[m
[32m+[m[32m                away_score = EXCLUDED.away_score,[m
[32m+[m[32m                home_ht = EXCLUDED.home_ht,[m
[32m+[m[32m                away_ht = EXCLUDED.away_ht,[m
[32m+[m[32m                first_goal_time = EXCLUDED.first_goal_time,[m
[32m+[m[32m                first_goal_time_extra = EXCLUDED.first_goal_time_extra[m
             """,[m
             ([m
                 m["id"],[m
[1mdiff --git a/backend/scripts/validate_db.py b/backend/scripts/validate_db.py[m
[1mindex a553156..bbbbc51 100644[m
[1m--- a/backend/scripts/validate_db.py[m
[1m+++ b/backend/scripts/validate_db.py[m
[36m@@ -36,7 +36,6 @@[m [mfrom db_common import ([m
     catalog_seasons,[m
     collected_seasons,[m
     get_conn,[m
[31m-    league_meta,[m
     load_json,[m
     raw_file,[m
     score_status,[m
[36m@@ -66,11 +65,47 @@[m [mdef playable_count(raw: dict) -> int:[m
     )[m
 [m
 [m
[32m+[m[32mGAME_INDEX_QUERY = """[m
[32m+[m[32mSELECT s.name AS season,[m
[32m+[m[32m       min(m.game_index) AS gmin,[m
[32m+[m[32m       max(m.game_index) AS gmax,[m
[32m+[m[32m       count(*) AS cnt,[m
[32m+[m[32m       count(DISTINCT m.game_index) AS distinct[m
[32m+[m[32mFROM matches m[m
[32m+[m[32mJOIN league_seasons ls ON ls.id = m.league_season_id[m
[32m+[m[32mJOIN seasons s ON s.id = ls.season_id[m
[32m+[m[32mJOIN leagues l ON l.id = ls.league_id[m
[32m+[m[32mWHERE l.api_key = %s[m
[32m+[m[32mGROUP BY s.name, s.start_year[m
[32m+[m[32mORDER BY s.start_year[m
[32m+[m[32m"""[m
[32m+[m
[32m+[m
[32m+[m[32mdef game_index_problems(cur, league: str, clean_seasons: set[str]) -> list[tuple]:[m
[32m+[m[32m    """Seasons whose game_index is duplicated, or gapped inside a clean season.[m
[32m+[m
[32m+[m[32m    A clean season (every raw match playable) must carry game_index 1..n with no[m
[32m+[m[32m    holes. A season with skipped or awarded matches legitimately has gaps, but[m
[32m+[m[32m    must still never reuse a game_index.[m
[32m+[m[32m    """[m
[32m+[m[32m    cur.execute(GAME_INDEX_QUERY, (league,))[m
[32m+[m[32m    problems: list[tuple] = [][m
[32m+[m[32m    for row in cur.fetchall():[m
[32m+[m[32m        season = row["season"][m
[32m+[m[32m        gmin, gmax, cnt, distinct = ([m
[32m+[m[32m            row["gmin"], row["gmax"], row["cnt"], row["distinct"],[m
[32m+[m[32m        )[m
[32m+[m[32m        duplicate = distinct != cnt[m
[32m+[m[32m        contiguous = gmin == 1 and gmax == cnt == distinct[m
[32m+[m[32m        if duplicate or (season in clean_seasons and not contiguous):[m
[32m+[m[32m            problems.append((season, gmin, gmax, cnt, distinct))[m
[32m+[m[32m    return problems[m
[32m+[m
[32m+[m
 def main(argv: list[str] | None = None) -> int:[m
     args = parse_args(argv)[m
     league = args.league[m
     seasons = collected_seasons(league)[m
[31m-    meta = league_meta(league)[m
     declared = set(catalog_seasons(league))[m
 [m
     conn = get_conn()[m
[36m@@ -127,7 +162,6 @@[m [mdef main(argv: list[str] | None = None) -> int:[m
                 (league,),[m
             )[m
             n_memberships = {r["name"]: r["n"] for r in cur.fetchall()}[m
[31m-            expected_memberships = sum(season_teams[s] for s in seasons)[m
             check("teams table non-empty", n_teams > 0, f"{n_teams} teams")[m
             check([m
                 "team_seasons == league teams per collected season",[m
[36m@@ -200,7 +234,6 @@[m [mdef main(argv: list[str] | None = None) -> int:[m
             dcount, tcount = cur.fetchone()[m
             check("match api_id globally unique (PK)", dcount == tcount, f"{dcount}/{tcount}")[m
 [m
[31m-            per_season = {}[m
             for season in seasons:[m
                 raw_n = raw_counts[season][m
                 cur.execute([m
[36m@@ -214,21 +247,13 @@[m [mdef main(argv: list[str] | None = None) -> int:[m
                     (season, league),[m
                 )[m
                 db_n = cur.fetchone()["count"][m
[31m-                per_season[season] = (raw_n, db_n)[m
                 check([m
                     f"{season}: match count == playable raw",[m
                     raw_n == db_n,[m
                     f"raw={raw_n} db={db_n}",[m
                 )[m
 [m
[31m-            # game_index is contiguous 1..n for clean seasons; otherwise playable[m
[31m-            # matches must not collide on game_index (skips leave legitimate gaps)[m
[31m-            gi_bad = [][m
[31m-            for season, gmin, gmax, cnt, distinct in cur.fetchall():[m
[31m-                duplicate = distinct != cnt[m
[31m-                contiguous = gmin == 1 and gmax == cnt == distinct[m
[31m-                if duplicate or (season in clean_seasons and not contiguous):[m
[31m-                    gi_bad.append((season, gmin, gmax, cnt, distinct))[m
[32m+[m[32m            gi_bad = game_index_problems(cur, league, clean_seasons)[m
             check([m
                 "game_index contiguous 1..n when clean, unique otherwise",[m
                 not gi_bad,[m
[1mdiff --git a/backend/tests/test_validate_db.py b/backend/tests/test_validate_db.py[m
[1mindex ac80e37..6d5167a 100644[m
[1m--- a/backend/tests/test_validate_db.py[m
[1m+++ b/backend/tests/test_validate_db.py[m
[36m@@ -11,10 +11,31 @@[m [mfrom pathlib import Path[m
 [m
 sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))[m
 [m
[31m-from scripts.validate_db import playable_count  # noqa: E402[m
[32m+[m[32mfrom scripts.validate_db import GAME_INDEX_QUERY, game_index_problems, playable_count  # noqa: E402[m
 from scripts.db_common import score_status  # noqa: E402[m
 [m
 [m
[32m+[m[32mclass _StubCursor:[m
[32m+[m[32m    """Records the query it is given and replays canned rows."""[m
[32m+[m
[32m+[m[32m    def __init__(self, rows):[m
[32m+[m[32m        self._rows = rows[m
[32m+[m[32m        self.executed: list[tuple[str, object]] = [][m
[32m+[m
[32m+[m[32m    def execute(self, sql, params=None):[m
[32m+[m[32m        self.executed.append((sql, params))[m
[32m+[m
[32m+[m[32m    def fetchall(self):[m
[32m+[m[32m        return self._rows[m
[32m+[m
[32m+[m
[32m+[m[32mdef _row(season, gmin, gmax, cnt, distinct):[m
[32m+[m[32m    return {[m
[32m+[m[32m        "season": season, "gmin": gmin, "gmax": gmax,[m
[32m+[m[32m        "cnt": cnt, "distinct": distinct,[m
[32m+[m[32m    }[m
[32m+[m
[32m+[m
 # ── playable_count ──────────────────────────────────────────────────────────[m
 def test_playable_count_counts_only_playable_matches():[m
     raw = {[m
[36m@@ -44,4 +65,43 @@[m [mdef test_playable_count_agrees_with_score_status():[m
         1[m
         for m in raw["matches"][m
         if score_status(m["score"]) == "playable"[m
[31m-    )[m
\ No newline at end of file[m
[32m+[m[32m    )[m
[32m+[m
[32m+[m[32m# ── game_index_problems ─────────────────────────────────────────────────────[m
[32m+[m[32mdef test_game_index_check_actually_runs_its_query():[m
[32m+[m[32m    # Regression: the check used to call fetchall() with no execute() before it,[m
[32m+[m[32m    # so psycopg2 returned [] and the check reported PASS while testing nothing.[m
[32m+[m[32m    cur = _StubCursor([_row("2024-2025", 1, 380, 380, 380)])[m
[32m+[m[32m    problems = game_index_problems(cur, "premier", {"2024-2025"})[m
[32m+[m[32m    assert len(cur.executed) == 1[m
[32m+[m[32m    assert cur.executed[0][0] == GAME_INDEX_QUERY[m
[32m+[m[32m    assert cur.executed[0][1] == ("premier",)[m
[32m+[m[32m    assert problems == [][m
[32m+[m
[32m+[m
[32m+[m[32mdef test_game_index_clean_season_must_be_contiguous():[m
[32m+[m[32m    assert game_index_problems([m
[32m+[m[32m        _StubCursor([_row("2024-2025", 1, 380, 380, 380)]), "premier", {"2024-2025"}[m
[32m+[m[32m    ) == [][m
[32m+[m[32m    # a gap: max is 380 but only 379 rows, so it is not 1..n[m
[32m+[m[32m    assert game_index_problems([m
[32m+[m[32m        _StubCursor([_row("2024-2025", 1, 380, 379, 379)]), "premier", {"2024-2025"}[m
[32m+[m[32m    ) == [("2024-2025", 1, 380, 379, 379)][m
[32m+[m[32m    # does not start at 1[m
[32m+[m[32m    assert game_index_problems([m
[32m+[m[32m        _StubCursor([_row("2024-2025", 2, 381, 380, 380)]), "premier", {"2024-2025"}[m
[32m+[m[32m    ) == [("2024-2025", 2, 381, 380, 380)][m
[32m+[m
[32m+[m
[32m+[m[32mdef test_game_index_duplicate_is_always_a_problem():[m
[32m+[m[32m    rows = [_row("2023-2024", 1, 380, 380, 379)][m
[32m+[m[32m    assert game_index_problems(_StubCursor(rows), "premier", {"2023-2024"})[m
[32m+[m[32m    # gaps are legitimate when the season is not clean[m
[32m+[m[32m    assert game_index_problems(_StubCursor(rows), "premier", set()) == [[m
[32m+[m[32m        ("2023-2024", 1, 380, 380, 379)[m
[32m+[m[32m    ][m
[32m+[m
[32m+[m
[32m+[m[32mdef test_game_index_query_counts_distinct_game_index():[m
[32m+[m[32m    assert "count(DISTINCT m.game_index)" in GAME_INDEX_QUERY[m
[32m+[m[32m    assert "GROUP BY s.name" in GAME_INDEX_QUERY[m
[1mdiff --git a/data/validation/skipped_matches/premier.json b/data/validation/skipped_matches/premier.json[m
[1mindex 0fe43fa..e6e2d0d 100644[m
[1m--- a/data/validation/skipped_matches/premier.json[m
[1m+++ b/data/validation/skipped_matches/premier.json[m
[36m@@ -1,6 +1,6 @@[m
 {[m
   "league": "premier",[m
[31m-  "generated_at": "2026-09-23T20:42:03",[m
[32m+[m[32m  "generated_at": "2026-09-26T16:37:09",[m
   "n_skipped": 0,[m
   "skipped": [],[m
   "n_kickoff_time_unknown": 0,[m
[1mdiff --git a/frontend/src/pages/Dashboard.jsx b/frontend/src/pages/Dashboard.jsx[m
[1mindex f01daac..2c24cf4 100644[m
[1m--- a/frontend/src/pages/Dashboard.jsx[m
[1m+++ b/frontend/src/pages/Dashboard.jsx[m
[36m@@ -12,6 +12,16 @@[m [mconst REGION_LABELS = {[m
   other: "Other",[m
 };[m
 [m
[32m+[m[32mexport function regionBuckets(byRegion) {[m
[32m+[m[32m  const buckets = byRegion ?? {};[m
[32m+[m[32m  const known = Object.keys(REGION_LABELS);[m
[32m+[m[32m  const extra = Object.keys(buckets).filter((r) => !known.includes(r));[m
[32m+[m[32m  return [...known, ...extra].map((region) => ({[m
[32m+[m[32m    region,[m
[32m+[m[32m    leagues: Array.isArray(buckets[region]) ? buckets[region] : [],[m
[32m+[m[32m  }));[m
[32m+[m[32m}[m
[32m+[m
 function LeagueCard({ item }) {[m
   return ([m
     <Link to={`/leagues/${item.slug}`} className="card league-card" style={{ textDecoration: "none" }}>[m
[36m@@ -72,7 +82,13 @@[m [mexport default function Dashboard() {[m
   if (error) return <ErrorBox error={error} />;[m
   if (!data) return <ErrorBox error="No dashboard data returned." />;[m
 [m
[31m-  const { top_leagues: topLeagues, top_clubs: topClubs, recent_matches: recent, upcoming_matches: upcoming, leagues_by_region: byRegion } = data;[m
[32m+[m[32m  const {[m
[32m+[m[32m    top_leagues: topLeagues = [],[m
[32m+[m[32m    top_clubs: topClubs = [],[m
[32m+[m[32m    recent_matches: recent = [],[m
[32m+[m[32m    upcoming_matches: upcoming = [],[m
[32m+[m[32m    leagues_by_region: byRegion,[m
[32m+[m[32m  } = data;[m
 [m
   return ([m
     <div>[m
[36m@@ -185,9 +201,9 @@[m [mexport default function Dashboard() {[m
       <section>[m
         <h3>Leagues by region</h3>[m
         <div className="grid regions">[m
[31m-          <RegionSection region="europe" leagues={byRegion?.europe || []} />[m
[31m-          <RegionSection region="asia" leagues={byRegion?.asia || []} />[m
[31m-          <RegionSection region="america" leagues={byRegion?.america || []} />[m
[32m+[m[32m          {regionBuckets(byRegion).map(({ region, leagues }) => ([m
[32m+[m[32m            <RegionSection key={region} region={region} leagues={leagues} />[m
[32m+[m[32m          ))}[m
         </div>[m
       </section>[m
     </div>[m
[1mdiff --git a/frontend/src/pages/Dashboard.test.jsx b/frontend/src/pages/Dashboard.test.jsx[m
[1mindex 3a8e6df..13a1dd0 100644[m
[1m--- a/frontend/src/pages/Dashboard.test.jsx[m
[1m+++ b/frontend/src/pages/Dashboard.test.jsx[m
[36m@@ -4,7 +4,7 @@[m [mimport { beforeEach, describe, expect, it, vi } from "vitest";[m
 import { api } from "../api/client.js";[m
 import { dashboard } from "../test/fixtures.js";[m
 import { renderPage } from "../test/render.jsx";[m
[31m-import Dashboard from "./Dashboard.jsx";[m
[32m+[m[32mimport Dashboard, { regionBuckets } from "./Dashboard.jsx";[m
 [m
 vi.mock("../api/client.js", () => {[m
   const names = [[m
[36m@@ -70,4 +70,57 @@[m [mdescribe("Dashboard", () => {[m
       screen.getAllByRole("link", { name: /J-League/ }).length,[m
     ).toBeGreaterThanOr