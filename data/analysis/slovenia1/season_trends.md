# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:08:21+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Prva liga (Slovenia)
- Scope: league `slovenia1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Celje | 74 | Koper | 7 pts |
| 2026-2027 | Maribor | 21 | Bravo | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Maribor beat Bravo by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 7 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025-2026 | 74 | 67 | 55 | 45 | 36 | 12 |
| 2026-2027 | 21 | 19 | 17 | 13 | 12 | 5 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 7 | 36 | 8 | 31 | 5 pts |
| 2026-2027 | 7 | 12 | 8 | 11 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 164 | 501 | 3.055 | 49.4% | 18.3% | 32.3% | 4.9% | 42.0 |
| 2026-2027 | 52 | 134 | 2.577 | 34.6% | 30.8% | 34.6% | 11.5% | 14.0 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 4.600)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.727 | 1.636 |
| 2026-2027 | 1.800 | 4.600 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\slovenia1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\slovenia1\charts\season_trends_avg_goals.png)

