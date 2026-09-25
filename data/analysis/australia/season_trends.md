# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:54:38+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: A-League (Australia)
- Scope: league `australia`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2024-2025 | Auckland FC | 53 | Melbourne City | 5 pts |
| 2025-2026 | Auckland FC | 49 | Newcastle Jets | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2025-2026** - Auckland FC beat Newcastle Jets by **0** pts

| season | margin | tight |
|---|---|---|
| 2024-2025 | 5 pts |  |
| 2025-2026 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2024-2025 | 53 | 48 | 46 | 38 | 30 | 21 |
| 2025-2026 | 49 | 49 | 43 | 38 | 32 | 21 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2024-2025 | 9 | 30 | 10 | 26 | 4 pts |
| 2025-2026 | 9 | 32 | 10 | 31 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2024-2025 | 169 | 556 | 3.29 | 34.9% | 26.0% | 39.1% | 4.7% | 35.62 |
| 2025-2026 | 163 | 462 | 2.834 | 38.0% | 26.4% | 35.6% | 5.5% | 36.67 |

## 6. View divergence
- Largest divergence: **2024-2025** (goals view, avg abs position diff = 4.154)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2024-2025 | 1.846 | 4.154 |
| 2025-2026 | 3.000 | 3.667 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\australia\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\australia\charts\season_trends_avg_goals.png)

