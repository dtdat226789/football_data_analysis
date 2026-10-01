# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:08:37+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Worthing | 84 | Hornchurch | 0 pts |
| 2026-2027 | Maidstone | 22 | Truro | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Worthing beat Hornchurch by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 0 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 21 = last safe, 24 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 21 | pos 24 |
|---|---|---|---|---|---|---|
| 2025-2026 | 84 | 84 | 82 | 78 | 48 | 40 |
| 2026-2027 | 22 | 20 | 19 | 17 | 10 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 21 | 48 | 22 | 43 | 5 pts |
| 2026-2027 | 21 | 10 | 22 | 8 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 605 | 1709 | 2.825 | 47.8% | 22.3% | 29.9% | 6.4% | 23.21 |
| 2026-2027 | 123 | 354 | 2.878 | 35.8% | 26.8% | 37.4% | 4.9% | 14.0 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 21.083)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 17.000 | 21.083 |
| 2026-2027 | 3.500 | 8.667 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\south\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\south\charts\season_trends_avg_goals.png)

