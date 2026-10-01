# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:45:58+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Levski Sofia | 81 | Ludogorets | 14 pts |
| 2026-2027 | Levski Sofia | 25 | CSKA Sofia | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Levski Sofia beat CSKA Sofia by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 14 pts |  |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 11 = last safe, 14 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 11 | pos 14 |
|---|---|---|---|---|---|---|
| 2025-2026 | 81 | 67 | 63 | 54 | 46 | 34 |
| 2026-2027 | 25 | 24 | 22 | 16 | 7 | 5 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 11 | 46 | 12 | 39 | 7 pts |
| 2026-2027 | 11 | 7 | 12 | 7 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 294 | 677 | 2.303 | 42.5% | 27.9% | 29.6% | 12.2% | 46.88 |
| 2026-2027 | 69 | 184 | 2.667 | 44.9% | 24.6% | 30.4% | 4.3% | 13.57 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.235)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 4.235 | 6.235 |
| 2026-2027 | 1.000 | 4.429 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\bulgaria1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\bulgaria1\charts\season_trends_avg_goals.png)

