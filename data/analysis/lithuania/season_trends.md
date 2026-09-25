# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:03:27+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Kauno Zalgiris | 75 | Hegelmann | 8 pts |
| 2026 | Kauno Zalgiris | 57 | Suduva | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026** - Kauno Zalgiris beat Suduva by **1** pts

| season | margin | tight |
|---|---|---|
| 2025 | 8 pts |  |
| 2026 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025 | 75 | 67 | 59 | 49 | 46 | 18 |
| 2026 | 57 | 56 | 48 | 44 | 38 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 7 | 46 | 8 | 42 | 4 pts |
| 2026 | 7 | 38 | 8 | 27 | 11 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 180 | 479 | 2.661 | 40.6% | 24.4% | 35.0% | 7.2% | 49.6 |
| 2026 | 144 | 381 | 2.646 | 39.6% | 27.8% | 32.6% | 11.1% | 39.2 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 4.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 1.600 | 4.000 |
| 2026 | 2.200 | 3.200 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\lithuania\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\lithuania\charts\season_trends_avg_goals.png)

