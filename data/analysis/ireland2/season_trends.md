# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:01:34+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Dundalk | 79 | Cobh Ramblers | 10 pts |
| 2026 | Cork City | 71 | Bray | 21 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2025** - Dundalk beat Cobh Ramblers by **10** pts

| season | margin | tight |
|---|---|---|
| 2025 | 10 pts |  |
| 2026 | 21 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025 | 79 | 69 | 59 | 45 | 44 | 20 |
| 2026 | 71 | 50 | 45 | 44 | 42 | 25 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 7 | 44 | 8 | 36 | 8 pts |
| 2026 | 7 | 42 | 8 | 40 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 179 | 502 | 2.804 | 45.3% | 23.5% | 31.3% | 5.6% | 49.5 |
| 2026 | 160 | 439 | 2.744 | 50.6% | 23.1% | 26.2% | 5.6% | 44.3 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 2.200)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 1.200 | 2.200 |
| 2026 | 2.000 | 2.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\ireland2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\ireland2\charts\season_trends_avg_goals.png)

