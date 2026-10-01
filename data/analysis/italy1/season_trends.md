# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:56:37+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Serie A (Italy)
- Scope: league `italy1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Inter | 87 | Napoli | 11 pts |
| 2026-2027 | AS Roma | 13 | Inter | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - AS Roma beat Inter by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 11 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 87 | 76 | 71 | 69 | 38 | 18 |
| 2026-2027 | 13 | 13 | 12 | 10 | 4 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 38 | 18 | 34 | 4 pts |
| 2026-2027 | 17 | 4 | 18 | 2 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 922 | 2.426 | 38.9% | 26.1% | 35.0% | 9.5% | 52.05 |
| 2026-2027 | 50 | 145 | 2.9 | 44.0% | 18.0% | 38.0% | 0.0% | 7.05 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.500)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 4.000 | 5.700 |
| 2026-2027 | 1.800 | 6.500 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\italy1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\italy1\charts\season_trends_avg_goals.png)

