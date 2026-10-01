# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:07:36+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Deportiva Minera | 66 | CD Extremadura | 0 pts |
| 2026-2027 | Betis B | 10 | Don Benito | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Deportiva Minera beat CD Extremadura by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 0 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 66 | 66 | 62 | 60 | 37 | 21 |
| 2026-2027 | 10 | 10 | 9 | 7 | 4 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 37 | 16 | 37 | 0 pts |
| 2026-2027 | 15 | 4 | 16 | 2 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 323 | 738 | 2.285 | 50.2% | 26.0% | 23.8% | 8.7% | 46.58 |
| 2026-2027 | 36 | 88 | 2.444 | 41.7% | 27.8% | 30.6% | 13.9% | 5.44 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.632)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.211 | 6.632 |
| 2026-2027 | 1.333 | 5.222 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\segunda4\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\segunda4\charts\season_trends_avg_goals.png)

