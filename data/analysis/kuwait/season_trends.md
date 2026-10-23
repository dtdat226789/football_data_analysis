# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:00:56+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Premier League (Kuwait)
- Scope: league `kuwait`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Al Kuwait | 49 | Al Qadisiya | 11 pts |
| 2026-2027 | Kazma SC | 7 | Al Kuwait | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Kazma SC beat Al Kuwait by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 11 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025-2026 | 49 | 38 | 35 | 22 | 15 | - |
| 2026-2027 | 7 | 7 | 6 | 4 | 3 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 9 | 15 | 10 | 8 | 7 pts |
| 2026-2027 | 9 | 3 | 10 | 2 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 98 | 257 | 2.622 | 40.8% | 25.5% | 33.7% | 7.1% | 26.9 |
| 2026-2027 | 18 | 54 | 3.0 | 44.4% | 22.2% | 33.3% | 5.6% | 4.17 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 5.167)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.600 | 3.400 |
| 2026-2027 | 2.333 | 5.167 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\kuwait\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\kuwait\charts\season_trends_avg_goals.png)

