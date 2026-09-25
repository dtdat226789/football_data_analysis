# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:54:57+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: 2. Liga (Austria)
- Scope: league `austria2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | St. Polten | 56 | A. Lustenau | 1 pts |
| 2026-2027 | BW Linz | 18 | First Vienna | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - St. Polten beat A. Lustenau by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 1 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 56 | 55 | 48 | 47 | 31 | 10 |
| 2026-2027 | 18 | 16 | 12 | 11 | 8 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 31 | 14 | 22 | 9 pts |
| 2026-2027 | 13 | 8 | 14 | 6 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 223 | 599 | 2.686 | 41.3% | 26.0% | 32.7% | 8.1% | 38.19 |
| 2026-2027 | 56 | 185 | 3.304 | 51.8% | 14.3% | 33.9% | 1.8% | 10.0 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.875)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.875 | 6.875 |
| 2026-2027 | 1.125 | 6.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\austria2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\austria2\charts\season_trends_avg_goals.png)

