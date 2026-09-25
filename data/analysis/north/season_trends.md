# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:03:57+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | AFC Fylde | 100 | South Shields | 2 pts |
| 2026-2027 | Hereford | 22 | Oxford City | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - AFC Fylde beat South Shields by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 2 pts | yes |
| 2026-2027 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 21 = last safe, 24 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 21 | pos 24 |
|---|---|---|---|---|---|---|
| 2025-2026 | 100 | 98 | 82 | 76 | 52 | 29 |
| 2026-2027 | 22 | 19 | 18 | 17 | 8 | 6 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 21 | 52 | 22 | 50 | 2 pts |
| 2026-2027 | 21 | 8 | 22 | 6 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 560 | 1707 | 3.048 | 42.7% | 22.5% | 34.8% | 4.1% | 64.75 |
| 2026-2027 | 108 | 290 | 2.685 | 49.1% | 19.4% | 31.5% | 4.6% | 12.62 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 9.333)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.333 | 7.417 |
| 2026-2027 | 2.333 | 9.333 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\north\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\north\charts\season_trends_avg_goals.png)

