# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:44:10+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Bundesliga (Austria)
- Scope: league `austria1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | LASK | 58 | Sturm Graz | 2 pts |
| 2026-2027 | SK Rapid | 18 | Salzburg | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - SK Rapid beat Salzburg by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 2 pts | yes |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025-2026 | 58 | 56 | 48 | 47 | 41 | 29 |
| 2026-2027 | 18 | 17 | 11 | 8 | 8 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 9 | 41 | 10 | 40 | 1 pts |
| 2026-2027 | 9 | 8 | 10 | 7 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 195 | 527 | 2.703 | 43.1% | 25.6% | 31.3% | 6.2% | 44.58 |
| 2026-2027 | 42 | 129 | 3.071 | 52.4% | 21.4% | 26.2% | 2.4% | 9.75 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 3.667)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.167 | 3.667 |
| 2026-2027 | 1.333 | 2.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\austria1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\austria1\charts\season_trends_avg_goals.png)

