# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:02:21+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Arezzo | 83 | Ascoli | 3 pts |
| 2026-2027 | Spezia | 16 | Ravenna | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - Spezia beat Ravenna by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 3 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 83 | 80 | 62 | 56 | 36 | 11 |
| 2026-2027 | 16 | 14 | 12 | 10 | 4 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 36 | 18 | 35 | 1 pts |
| 2026-2027 | 17 | 4 | 18 | 3 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 357 | 802 | 2.246 | 37.5% | 31.7% | 30.8% | 9.8% | 47.9 |
| 2026-2027 | 60 | 154 | 2.567 | 48.3% | 30.0% | 21.7% | 8.3% | 8.1 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.600)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.500 | 6.600 |
| 2026-2027 | 1.300 | 6.600 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\italy3b\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\italy3b\charts\season_trends_avg_goals.png)

