# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:04:07+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Eliteserien (Norway)
- Scope: league `norway`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Viking | 71 | Bodo/Glimt | 1 pts |
| 2026 | Viking | 50 | Bodo/Glimt | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026** - Viking beat Bodo/Glimt by **0** pts

| season | margin | tight |
|---|---|---|
| 2025 | 1 pts | yes |
| 2026 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025 | 71 | 70 | 56 | 43 | 34 | 9 |
| 2026 | 50 | 50 | 36 | 32 | 23 | 16 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 13 | 34 | 14 | 31 | 3 pts |
| 2026 | 13 | 23 | 14 | 21 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 240 | 762 | 3.175 | 49.2% | 18.8% | 32.1% | 4.6% | 42.19 |
| 2026 | 168 | 531 | 3.161 | 51.2% | 19.6% | 29.2% | 3.6% | 29.44 |

## 6. View divergence
- Largest divergence: **2026** (goals view, avg abs position diff = 5.250)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 2.750 | 4.250 |
| 2026 | 2.875 | 5.250 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\norway\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\norway\charts\season_trends_avg_goals.png)

