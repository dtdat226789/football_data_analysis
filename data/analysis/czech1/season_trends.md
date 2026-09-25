# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:56:19+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Chance Liga (Czech Republic)
- Scope: league `czech1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Slavia Prague | 80 | Sparta Prague | 4 pts |
| 2026-2027 | Slavia Prague | 23 | Liberec | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Slavia Prague beat Liberec by **3** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 4 pts |  |
| 2026-2027 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 80 | 76 | 56 | 52 | 36 | 26 |
| 2026-2027 | 23 | 20 | 16 | 16 | 8 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 36 | 14 | 36 | 0 pts |
| 2026-2027 | 13 | 8 | 14 | 5 | 3 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 280 | 740 | 2.643 | 42.1% | 23.9% | 33.9% | 8.2% | 42.61 |
| 2026-2027 | 71 | 201 | 2.831 | 45.1% | 21.1% | 33.8% | 5.6% | 12.38 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 5.889)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.333 | 5.889 |
| 2026-2027 | 1.875 | 4.500 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\czech1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\czech1\charts\season_trends_avg_goals.png)

