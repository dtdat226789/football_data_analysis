# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:02:12+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | L.R. Vicenza | 89 | Brescia | 20 pts |
| 2026-2027 | Cittadella | 18 | Brescia | 4 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2026-2027** - Cittadella beat Brescia by **4** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 20 pts |  |
| 2026-2027 | 4 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 89 | 69 | 64 | 59 | 40 | 23 |
| 2026-2027 | 18 | 14 | 11 | 9 | 5 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 40 | 18 | 36 | 4 pts |
| 2026-2027 | 17 | 5 | 18 | 3 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 889 | 2.339 | 37.9% | 30.3% | 31.8% | 9.7% | 51.25 |
| 2026-2027 | 60 | 137 | 2.283 | 33.3% | 38.3% | 28.3% | 18.3% | 7.85 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 8.100)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.600 | 8.100 |
| 2026-2027 | 1.400 | 7.800 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\italy3a\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\italy3a\charts\season_trends_avg_goals.png)

