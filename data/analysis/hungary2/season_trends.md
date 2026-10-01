# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:54:38+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: NB II. (Hungary)
- Scope: league `hungary2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Vasas | 64 | Honved | 5 pts |
| 2026-2027 | Soroksar | 20 | Kecskemeti TE | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Soroksar beat Kecskemeti TE by **3** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 5 pts |  |
| 2026-2027 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 64 | 59 | 48 | 46 | 33 | 28 |
| 2026-2027 | 20 | 17 | 14 | 13 | 6 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 33 | 14 | 33 | 0 pts |
| 2026-2027 | 13 | 6 | 14 | 4 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 602 | 2.508 | 43.8% | 25.0% | 31.2% | 6.2% | 41.25 |
| 2026-2027 | 61 | 172 | 2.82 | 52.5% | 23.0% | 24.6% | 3.3% | 10.56 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.375)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.875 | 4.375 |
| 2026-2027 | 1.500 | 3.750 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\hungary2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\hungary2\charts\season_trends_avg_goals.png)

