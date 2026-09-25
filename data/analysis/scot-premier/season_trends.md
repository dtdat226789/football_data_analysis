# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:44:36+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Celtic | 82 | Hearts | 2 pts |
| 2026-2027 | Celtic | 18 | Rangers | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Celtic beat Hearts by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 2 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025-2026 | 82 | 80 | 61 | 49 | 40 | 21 |
| 2026-2027 | 18 | 16 | 10 | 8 | 8 | 5 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 9 | 40 | 10 | 40 | 0 pts |
| 2026-2027 | 9 | 8 | 10 | 7 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 234 | 643 | 2.748 | 44.9% | 27.4% | 27.8% | 7.3% | 42.53 |
| 2026-2027 | 42 | 107 | 2.548 | 38.1% | 21.4% | 40.5% | 4.8% | 9.75 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 4.500)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.800 | 2.933 |
| 2026-2027 | 1.667 | 4.500 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\scot-premier\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\scot-premier\charts\season_trends_avg_goals.png)

