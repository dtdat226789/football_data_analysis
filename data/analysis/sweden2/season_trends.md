# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:09:36+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Superettan (Sweden)
- Scope: league `sweden2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Vasteras SK | 65 | Kalmar | 1 pts |
| 2026 | Norrkoping | 55 | Falkenberg | 10 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2025** - Vasteras SK beat Kalmar by **1** pts

| season | margin | tight |
|---|---|---|
| 2025 | 1 pts | yes |
| 2026 | 10 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025 | 65 | 64 | 48 | 43 | 30 | 19 |
| 2026 | 55 | 45 | 43 | 37 | 24 | 19 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 13 | 30 | 14 | 22 | 8 pts |
| 2026 | 13 | 24 | 14 | 24 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 240 | 686 | 2.858 | 42.1% | 27.1% | 30.8% | 7.5% | 40.94 |
| 2026 | 200 | 580 | 2.9 | 38.5% | 27.0% | 34.5% | 6.5% | 34.12 |

## 6. View divergence
- Largest divergence: **2026** (goals view, avg abs position diff = 5.250)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 1.750 | 4.875 |
| 2026 | 0.875 | 5.250 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\sweden2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\sweden2\charts\season_trends_avg_goals.png)

