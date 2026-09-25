# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:50:03+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Super Lig (Turkey)
- Scope: league `turkey1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Galatasaray | 77 | Fenerbahce | 3 pts |
| 2026-2027 | Amedspor | 13 | Galatasaray | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - Amedspor beat Galatasaray by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 3 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 77 | 74 | 60 | 55 | 33 | 30 |
| 2026-2027 | 13 | 13 | 12 | 10 | 4 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 33 | 16 | 32 | 1 pts |
| 2026-2027 | 15 | 4 | 16 | 4 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 812 | 2.654 | 42.2% | 29.1% | 28.8% | 9.2% | 46.06 |
| 2026-2027 | 54 | 161 | 2.981 | 48.1% | 20.4% | 31.5% | 3.7% | 8.39 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 5.333)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.667 | 3.556 |
| 2026-2027 | 3.778 | 5.333 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\turkey1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\turkey1\charts\season_trends_avg_goals.png)

