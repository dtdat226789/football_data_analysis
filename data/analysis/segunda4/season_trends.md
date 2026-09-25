# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:46:22+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Deportiva Minera | 66 | CD Extremadura | 0 pts |
| 2026-2027 | Sevilla FC B | 7 | Don Benito | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Deportiva Minera beat CD Extremadura by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 0 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 66 | 66 | 62 | 60 | 37 | 21 |
| 2026-2027 | 7 | 7 | 6 | 6 | 2 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 37 | 16 | 37 | 0 pts |
| 2026-2027 | 15 | 2 | 16 | 2 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 323 | 738 | 2.285 | 50.2% | 26.0% | 23.8% | 8.7% | 46.58 |
| 2026-2027 | 27 | 66 | 2.444 | 33.3% | 29.6% | 37.0% | 11.1% | 4.06 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.632)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.211 | 6.632 |
| 2026-2027 | 1.889 | 4.556 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\segunda4\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\segunda4\charts\season_trends_avg_goals.png)

