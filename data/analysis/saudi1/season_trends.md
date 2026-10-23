# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:05:20+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Saudi Professional League (Saudi Arabia)
- Scope: league `saudi1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Al Nassr | 86 | Al Hilal | 1 pts |
| 2026-2027 | Al Hilal | 18 | Al Ittihad | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Al Nassr beat Al Hilal by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 1 pts | yes |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 86 | 85 | 77 | 55 | 30 | 17 |
| 2026-2027 | 18 | 17 | 16 | 12 | 3 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 30 | 16 | 29 | 1 pts |
| 2026-2027 | 15 | 3 | 16 | 3 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 314 | 943 | 3.003 | 44.3% | 22.9% | 32.8% | 5.1% | 45.79 |
| 2026-2027 | 63 | 174 | 2.762 | 38.1% | 30.2% | 31.7% | 15.9% | 9.44 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.105)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 4.000 | 4.105 |
| 2026-2027 | 3.111 | 3.333 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\saudi1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\saudi1\charts\season_trends_avg_goals.png)

