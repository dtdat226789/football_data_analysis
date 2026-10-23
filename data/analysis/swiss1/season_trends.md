# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:09:51+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Super League (Switzerland)
- Scope: league `swiss1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Thun | 75 | St. Gallen | 5 pts |
| 2026-2027 | Lugano | 25 | Young Boys | 6 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2025-2026** - Thun beat St. Gallen by **5** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 5 pts |  |
| 2026-2027 | 6 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025-2026 | 75 | 70 | 63 | 55 | 42 | 23 |
| 2026-2027 | 25 | 19 | 13 | 12 | 10 | 6 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 9 | 42 | 10 | 38 | 4 pts |
| 2026-2027 | 9 | 10 | 10 | 8 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 230 | 753 | 3.274 | 40.4% | 24.8% | 34.8% | 4.3% | 48.46 |
| 2026-2027 | 54 | 209 | 3.87 | 38.9% | 18.5% | 42.6% | 1.9% | 12.67 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.769)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 1.846 | 4.769 |
| 2026-2027 | 1.500 | 3.500 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\swiss1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\swiss1\charts\season_trends_avg_goals.png)

