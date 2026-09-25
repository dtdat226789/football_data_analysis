# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:01:53+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Primavera 1 (Italy)
- Scope: league `italy19`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Cesena U20 | 70 | Fiorentina U20 | 2 pts |
| 2026-2027 | Inter U20 | 13 | Parma U20 | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Cesena U20 beat Fiorentina U20 by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 2 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 70 | 68 | 65 | 59 | 40 | 24 |
| 2026-2027 | 13 | 11 | 11 | 9 | 4 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 40 | 18 | 39 | 1 pts |
| 2026-2027 | 17 | 4 | 18 | 3 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 382 | 1051 | 2.751 | 39.8% | 30.6% | 29.6% | 7.6% | 51.45 |
| 2026-2027 | 50 | 161 | 3.22 | 28.0% | 32.0% | 40.0% | 4.0% | 6.7 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.600)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.600 | 5.500 |
| 2026-2027 | 2.200 | 6.600 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\italy19\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\italy19\charts\season_trends_avg_goals.png)

