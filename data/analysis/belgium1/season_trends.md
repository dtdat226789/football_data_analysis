# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:55:17+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Jupiler Pro League (Belgium)
- Scope: league `belgium1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Club Brugge KV | 88 | Royale Union SG | 2 pts |
| 2026-2027 | Royale Union SG | 19 | Gent | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - Royale Union SG beat Gent by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 2 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 88 | 86 | 59 | 55 | 34 | 1 |
| 2026-2027 | 19 | 19 | 18 | 11 | 4 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 34 | 16 | 26 | 8 pts |
| 2026-2027 | 15 | 4 | 16 | 3 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 321 | 864 | 2.692 | 41.1% | 25.2% | 33.6% | 7.8% | 43.8 |
| 2026-2027 | 63 | 185 | 2.937 | 50.8% | 19.0% | 30.2% | 4.8% | 9.83 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.222)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 4.900 | 6.200 |
| 2026-2027 | 1.889 | 6.222 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\belgium1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\belgium1\charts\season_trends_avg_goals.png)

