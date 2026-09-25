# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:57:21+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2026-2027 | Bolton U21 | 15 | Fleetwood U21 | 6 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 1 seasons
- Tightest race: **2026-2027** - Bolton U21 beat Fleetwood U21 by **6** pts

| season | margin | tight |
|---|---|---|
| 2026-2027 | 6 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 14 = last safe, 17 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 14 | pos 17 |
|---|---|---|---|---|---|---|
| 2026-2027 | 15 | 9 | 7 | 6 | 3 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2026-2027 | 14 | 3 | 15 | 3 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2026-2027 | 34 | 140 | 4.118 | 41.2% | 26.5% | 32.4% | 2.9% | 5.47 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2026-2027 | 2.235 | 6.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\develop21\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\develop21\charts\season_trends_avg_goals.png)

