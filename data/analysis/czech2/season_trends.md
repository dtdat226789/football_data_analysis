# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:56:30+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: ChNL (Czech Republic)
- Scope: league `czech2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Brno | 76 | Taborsko | 23 pts |
| 2026-2027 | Karvina | 18 | Usti nad Labem | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Karvina beat Usti nad Labem by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 23 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 76 | 53 | 48 | 46 | 34 | 25 |
| 2026-2027 | 18 | 18 | 16 | 13 | 9 | 6 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 34 | 14 | 30 | 4 pts |
| 2026-2027 | 13 | 9 | 14 | 8 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 643 | 2.679 | 46.2% | 20.8% | 32.9% | 5.8% | 41.88 |
| 2026-2027 | 72 | 218 | 3.028 | 43.1% | 33.3% | 23.6% | 5.6% | 12.0 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.250)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.250 | 4.250 |
| 2026-2027 | 1.750 | 4.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\czech2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\czech2\charts\season_trends_avg_goals.png)

