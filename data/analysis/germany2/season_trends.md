# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:59:38+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: 2. Bundesliga (Germany)
- Scope: league `germany2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Schalke | 70 | Paderborn | 7 pts |
| 2026-2027 | Hertha Berlin | 18 | Nurnberg | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Hertha Berlin beat Nurnberg by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 7 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 70 | 63 | 60 | 52 | 39 | 30 |
| 2026-2027 | 18 | 16 | 11 | 10 | 4 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 39 | 16 | 37 | 2 pts |
| 2026-2027 | 15 | 4 | 16 | 4 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 903 | 2.913 | 46.5% | 24.2% | 29.4% | 5.5% | 42.6 |
| 2026-2027 | 54 | 179 | 3.315 | 38.9% | 27.8% | 33.3% | 3.7% | 8.17 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 5.400)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.600 | 5.400 |
| 2026-2027 | 1.778 | 5.111 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\germany2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\germany2\charts\season_trends_avg_goals.png)

