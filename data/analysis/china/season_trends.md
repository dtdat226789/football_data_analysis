# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:46:35+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Super League (China)
- Scope: league `china`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Shanghai Port | 66 | Shanghai Shenhua | 2 pts |
| 2026 | Chengdu Rongcheng | 52 | Beijing Guoan | 9 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2025** - Shanghai Port beat Shanghai Shenhua by **2** pts

| season | margin | tight |
|---|---|---|
| 2025 | 2 pts | yes |
| 2026 | 9 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025 | 66 | 64 | 57 | 44 | 25 | 19 |
| 2026 | 52 | 43 | 41 | 38 | 28 | 21 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 13 | 25 | 14 | 25 | 0 pts |
| 2026 | 13 | 28 | 14 | 26 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 240 | 771 | 3.212 | 46.7% | 25.8% | 27.5% | 3.8% | 41.12 |
| 2026 | 208 | 643 | 3.091 | 45.7% | 26.9% | 27.4% | 4.8% | 35.5 |

## 6. View divergence
- Largest divergence: **2026** (goals view, avg abs position diff = 5.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 2.500 | 3.625 |
| 2026 | 4.125 | 5.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\china\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\china\charts\season_trends_avg_goals.png)

