# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:55:39+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Coritiba | 62 | Criciuma | 1 pts |
| 2026 | Vila Nova FC | 51 | Fortaleza | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026** - Vila Nova FC beat Fortaleza by **0** pts

| season | margin | tight |
|---|---|---|
| 2025 | 1 pts | yes |
| 2026 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025 | 62 | 61 | 58 | 52 | 34 | 31 |
| 2026 | 51 | 51 | 50 | 46 | 30 | 13 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 17 | 34 | 18 | 33 | 1 pts |
| 2026 | 17 | 30 | 18 | 28 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 380 | 843 | 2.218 | 45.8% | 30.5% | 23.7% | 8.7% | 17.96 |
| 2026 | 289 | 677 | 2.343 | 45.0% | 27.3% | 27.7% | 8.7% | 39.4 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 19.333)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 16.281 | 19.333 |
| 2026 | 2.400 | 7.700 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\brazil2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\brazil2\charts\season_trends_avg_goals.png)

