# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:59:07+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: J1 League (Japan)
- Scope: league `japan1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2026 | Kashima Antlers | 33 | FC Tokyo | 6 pts |
| 2026-2027 | Vissel Kobe | 19 | Kashiwa Reysol | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Vissel Kobe beat Kashiwa Reysol by **1** pts

| season | margin | tight |
|---|---|---|
| 2026 | 6 pts |  |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2026 | 33 | 27 | 21 | 18 | 9 | 6 |
| 2026-2027 | 19 | 18 | 17 | 14 | 6 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2026 | 17 | 9 | 18 | 9 | 0 pts |
| 2026-2027 | 17 | 6 | 18 | 4 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2026 | 161 | 462 | 2.87 | 58.4% | 0.0% | 41.6% | 0.0% | 9.42 |
| 2026-2027 | 80 | 237 | 2.962 | 46.2% | 21.2% | 32.5% | 3.8% | 11.15 |

## 6. View divergence
- Largest divergence: **2026** (luck view, avg abs position diff = 13.889)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2026 | 13.889 | 8.889 |
| 2026-2027 | 2.000 | 5.100 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\japan1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\japan1\charts\season_trends_avg_goals.png)

