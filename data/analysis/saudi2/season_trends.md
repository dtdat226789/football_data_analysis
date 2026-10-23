# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:05:35+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Division 1 (Saudi Arabia)
- Scope: league `saudi2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Abha | 77 | Al Diriyah | 2 pts |
| 2026-2027 | Al-Ula | 15 | Al Zulfi | 5 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2025-2026** - Abha beat Al Diriyah by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 2 pts | yes |
| 2026-2027 | 5 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 77 | 75 | 71 | 59 | 32 | 14 |
| 2026-2027 | 15 | 10 | 9 | 9 | 6 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 32 | 16 | 22 | 10 pts |
| 2026-2027 | 15 | 6 | 16 | 5 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 309 | 917 | 2.968 | 41.4% | 23.3% | 35.3% | 5.2% | 47.17 |
| 2026-2027 | 53 | 112 | 2.113 | 30.2% | 45.3% | 24.5% | 20.8% | 7.5 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.222)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.333 | 5.444 |
| 2026-2027 | 2.889 | 6.222 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\saudi2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\saudi2\charts\season_trends_avg_goals.png)

