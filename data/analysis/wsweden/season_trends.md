# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:51:32+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Hacken W | 64 | Hammarby W | 4 pts |
| 2026 | Hacken W | 52 | Hammarby W | 5 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2025** - Hacken W beat Hammarby W by **4** pts

| season | margin | tight |
|---|---|---|
| 2025 | 4 pts |  |
| 2026 | 5 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 11 = last safe, 14 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 11 | pos 14 |
|---|---|---|---|---|---|---|
| 2025 | 64 | 60 | 50 | 41 | 25 | 9 |
| 2026 | 52 | 47 | 31 | 27 | 18 | 6 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 11 | 25 | 12 | 23 | 2 pts |
| 2026 | 11 | 18 | 12 | 17 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 182 | 606 | 3.33 | 46.7% | 13.7% | 39.6% | 2.2% | 37.21 |
| 2026 | 133 | 381 | 2.865 | 45.1% | 20.3% | 34.6% | 3.0% | 26.57 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 5.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 2.714 | 5.000 |
| 2026 | 2.429 | 4.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\wsweden\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\wsweden\charts\season_trends_avg_goals.png)

