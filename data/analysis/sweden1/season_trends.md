# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:09:21+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Allsvenskan (Sweden)
- Scope: league `sweden1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Mjallby | 75 | Hammarby | 13 pts |
| 2026 | Sirius | 51 | Hammarby | 8 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2026** - Sirius beat Hammarby by **8** pts

| season | margin | tight |
|---|---|---|
| 2025 | 13 pts |  |
| 2026 | 8 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025 | 75 | 62 | 51 | 49 | 30 | 16 |
| 2026 | 51 | 43 | 37 | 35 | 19 | 14 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 13 | 30 | 14 | 29 | 1 pts |
| 2026 | 13 | 19 | 14 | 19 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 240 | 683 | 2.846 | 40.0% | 22.1% | 37.9% | 5.8% | 41.69 |
| 2026 | 176 | 517 | 2.938 | 41.5% | 23.3% | 35.2% | 4.0% | 30.44 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 7.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 2.750 | 7.000 |
| 2026 | 2.875 | 3.625 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\sweden1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\sweden1\charts\season_trends_avg_goals.png)

