# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:00:25+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Eredivisie (Netherlands)
- Scope: league `holland1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | PSV | 84 | Feyenoord | 19 pts |
| 2026-2027 | AZ Alkmaar | 19 | Feyenoord | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - AZ Alkmaar beat Feyenoord by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 19 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 84 | 65 | 59 | 56 | 37 | 19 |
| 2026-2027 | 19 | 17 | 16 | 13 | 5 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 37 | 16 | 35 | 2 pts |
| 2026-2027 | 15 | 5 | 16 | 4 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 321 | 1016 | 3.165 | 44.5% | 25.9% | 29.6% | 3.1% | 36.29 |
| 2026-2027 | 63 | 240 | 3.81 | 30.2% | 27.0% | 42.9% | 1.6% | 9.56 |

## 6. View divergence
- Largest divergence: **2025-2026** (luck view, avg abs position diff = 6.833)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 6.833 | 6.250 |
| 2026-2027 | 2.556 | 5.222 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\holland1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\holland1\charts\season_trends_avg_goals.png)

