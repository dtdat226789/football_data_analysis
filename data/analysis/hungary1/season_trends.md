# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:00:57+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: NB I. (Hungary)
- Scope: league `hungary1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Gyor | 69 | Ferencvaros | 1 pts |
| 2026-2027 | Gyor | 15 | Puskas Academy | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - Gyor beat Puskas Academy by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 1 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025-2026 | 69 | 68 | 53 | 46 | 40 | 22 |
| 2026-2027 | 15 | 15 | 14 | 11 | 9 | 6 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 9 | 40 | 10 | 38 | 2 pts |
| 2026-2027 | 9 | 9 | 10 | 8 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 198 | 594 | 3.0 | 39.4% | 24.7% | 35.9% | 4.0% | 45.42 |
| 2026-2027 | 47 | 153 | 3.255 | 42.6% | 27.7% | 29.8% | 4.3% | 10.67 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 5.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.000 | 5.000 |
| 2026-2027 | 1.333 | 4.167 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\hungary1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\hungary1\charts\season_trends_avg_goals.png)

