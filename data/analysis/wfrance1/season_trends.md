# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:11:29+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Premiere Ligue Women (France)
- Scope: league `wfrance1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Lyon W | 66 | Paris FC W | 15 pts |
| 2026-2027 | OL Lyonnes W | 9 | PSG W | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - OL Lyonnes W beat PSG W by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 15 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025-2026 | 66 | 51 | 41 | 33 | 19 | 13 |
| 2026-2027 | 9 | 9 | 6 | 4 | 3 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 9 | 19 | 10 | 15 | 4 pts |
| 2026-2027 | 9 | 3 | 10 | 1 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 135 | 410 | 3.037 | 39.3% | 18.5% | 42.2% | 5.2% | 31.67 |
| 2026-2027 | 18 | 61 | 3.389 | 50.0% | 16.7% | 33.3% | 5.6% | 4.25 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 3.667)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.167 | 3.333 |
| 2026-2027 | 2.333 | 3.667 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\wfrance1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\wfrance1\charts\season_trends_avg_goals.png)

