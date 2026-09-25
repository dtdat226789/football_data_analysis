# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:45:44+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | R. Union | 69 | Alaves B | 7 pts |
| 2026-2027 | Osasuna B | 9 | Barcelona B | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Osasuna B beat Barcelona B by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 7 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 69 | 62 | 58 | 50 | 35 | 25 |
| 2026-2027 | 9 | 7 | 6 | 5 | 2 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 35 | 16 | 30 | 5 pts |
| 2026-2027 | 15 | 2 | 16 | 2 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 769 | 2.513 | 42.5% | 29.1% | 28.4% | 9.2% | 46.06 |
| 2026-2027 | 27 | 73 | 2.704 | 44.4% | 25.9% | 29.6% | 11.1% | 4.11 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.778 | 5.556 |
| 2026-2027 | 2.778 | 6.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\segunda2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\segunda2\charts\season_trends_avg_goals.png)

