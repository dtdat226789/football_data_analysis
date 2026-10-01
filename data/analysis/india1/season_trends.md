# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:55:08+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: ISL (India)
- Scope: league `india1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2024-2025 | Mohun Bagan | 56 | Goa | 8 pts |
| 2025-2026 | East Bengal | 26 | Mohun Bagan | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2025-2026** - East Bengal beat Mohun Bagan by **0** pts

| season | margin | tight |
|---|---|---|
| 2024-2025 | 8 pts |  |
| 2025-2026 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 11 = last safe, 14 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 11 | pos 14 |
|---|---|---|---|---|---|---|
| 2024-2025 | 56 | 48 | 38 | 36 | 27 | - |
| 2025-2026 | 26 | 26 | 23 | 22 | 11 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2024-2025 | 11 | 27 | 12 | 18 | 9 pts |
| 2025-2026 | 11 | 11 | 12 | 11 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2024-2025 | 156 | 448 | 2.872 | 42.3% | 24.4% | 33.3% | 7.1% | 33.08 |
| 2025-2026 | 91 | 221 | 2.429 | 38.5% | 31.9% | 29.7% | 11.0% | 17.43 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.714)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2024-2025 | 1.692 | 3.538 |
| 2025-2026 | 2.714 | 4.714 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\india1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\india1\charts\season_trends_avg_goals.png)

