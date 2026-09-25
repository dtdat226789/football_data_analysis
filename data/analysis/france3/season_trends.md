# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:59:05+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Dijon | 65 | Sochaux | 7 pts |
| 2026-2027 | Rouen | 17 | La Roche | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Rouen beat La Roche by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 7 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 65 | 58 | 54 | 51 | 31 | 25 |
| 2026-2027 | 17 | 15 | 14 | 12 | 5 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 31 | 16 | 31 | 0 pts |
| 2026-2027 | 15 | 5 | 16 | 5 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 303 | 738 | 2.436 | 36.0% | 33.0% | 31.0% | 10.6% | 16.18 |
| 2026-2027 | 68 | 161 | 2.368 | 38.2% | 29.4% | 32.4% | 11.8% | 10.22 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 17.800)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 13.040 | 17.800 |
| 2026-2027 | 1.333 | 6.222 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\france3\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\france3\charts\season_trends_avg_goals.png)

