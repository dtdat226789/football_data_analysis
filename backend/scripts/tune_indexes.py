"""Step 06 - Index tuning.

Applies sql/06_index_tuning.sql (analytical indexes) and verifies the planner
uses them on representative analytical queries via EXPLAIN (ANALYZE, BUFFERS).

Usage:
    python backend/scripts/tune_indexes.py
"""
from __future__ import annotations

import sys

from db_common import LEAGUE, apply_sql, get_conn

QUERIES = [
    (
        "form window: home + away legs of one club (Arsenal)",
        """
        SELECT m.match_date, m.home_score, m.away_score, m.first_goal_time
        FROM matches m
        JOIN team_seasons ts_h ON ts_h.league_season_id = m.league_season_id AND ts_h.team_id = m.home_team_id
        JOIN team_seasons ts_a ON ts_a.league_season_id = m.league_season_id AND ts_a.team_id = m.away_team_id
        WHERE ts_h.api_name = 'Arsenal' OR ts_a.api_name = 'Arsenal'
        ORDER BY m.match_date
        """,
    ),
    (
        "chronological season listing: 2024-2025",
        """
        SELECT m.game_index, m.match_date, m.home_score, m.away_score
        FROM matches m
        JOIN league_seasons ls ON ls.id = m.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        WHERE s.name = '2024-2025'
          AND ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
        ORDER BY m.match_date, m.game_index
        """,
    ),
    (
        "standings lookup: classic table 2024-2025 in position order",
        """
        SELECT st.position, st.points, st.goal_difference
        FROM standings st
        JOIN league_seasons ls ON ls.id = st.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        WHERE s.name = '2024-2025'
          AND ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
          AND st.view = 'classic'
        ORDER BY st.position
        """,
    ),
    (
        "club standings across seasons (ML feature join)",
        """
        SELECT s.name, st.view, st.position, st.points
        FROM standings st
        JOIN team_seasons ts ON ts.league_season_id = st.league_season_id AND ts.team_id = st.team_id
        JOIN league_seasons ls ON ls.id = st.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        WHERE ts.api_name = 'Arsenal'
        ORDER BY s.start_year, st.view
        """,
    ),
]


def main() -> int:
    conn = get_conn()
    try:
        apply_sql(conn, "06_index_tuning.sql")
        with conn.cursor() as cur:
            cur.execute(
                "SELECT indexname FROM pg_indexes WHERE schemaname = 'public' ORDER BY indexname"
            )
            indexes = [r[0] for r in cur.fetchall()]
            print(f"[06] indexes present ({len(indexes)}): {', '.join(indexes)}")

            for label, sql in QUERIES:
                n_params = sql.count("%s")
                plan = f"EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) {sql}"
                cur.execute(plan, (LEAGUE,) * n_params)
                lines = [row[0] for row in cur.fetchall()]
                plan_line = lines[0] if lines else ""
                joined = "\n".join(lines)
                if "Index Only Scan" in joined:
                    scan_type = "Index Only Scan"
                elif "Index Scan" in joined:
                    scan_type = "Index Scan"
                elif "Bitmap Heap Scan" in joined:
                    scan_type = "Bitmap Heap Scan"
                elif "Seq Scan" in joined:
                    scan_type = "Seq Scan"
                else:
                    scan_type = "other"
                n_index = joined.count("Index Scan") + joined.count("Index Only Scan")
                n_seq = joined.count("Seq Scan")
                print(f"[06] {label}")
                print(f"       {plan_line}")
                print(f"       plan nodes -> {scan_type} (index scans={n_index}, seq scans={n_seq})")
        conn.rollback()
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())