# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:49:19+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Flora | 82 | Levadia | 3 pts |
| 2026 | Levadia | 72 | Flora | 17 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2025** - Flora beat Levadia by **3** pts

| season | margin | tight |
|---|---|---|
| 2025 | 3 pts | yes |
| 2026 | 17 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025 | 82 | 79 | 70 | 49 | 36 | 17 |
| 2026 | 72 | 55 | 50 | 35 | 34 | 19 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 7 | 36 | 8 | 30 | 6 pts |
| 2026 | 7 | 34 | 8 | 29 | 5 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 180 | 572 | 3.178 | 46.7% | 13.3% | 40.0% | 2.2% | 51.6 |
| 2026 | 145 | 456 | 3.145 | 46.2% | 12.4% | 41.4% | 3.4% | 41.7 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 3.600)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 1.400 | 3.600 |
| 2026 | 2.600 | 3.200 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\estonia\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\estonia\charts\season_trends_avg_goals.png)

