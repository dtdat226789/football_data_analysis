# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:00:03+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Super League (Greece)
- Scope: league `greece1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | AEK Athens | 72 | Olympiacos Piraeus | 3 pts |
| 2026-2027 | Panathinaikos | 15 | PAOK | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - AEK Athens beat Olympiacos Piraeus by **3** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 3 pts | yes |
| 2026-2027 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 11 = last safe, 14 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 11 | pos 14 |
|---|---|---|---|---|---|---|
| 2025-2026 | 72 | 69 | 52 | 46 | 36 | 29 |
| 2026-2027 | 15 | 12 | 10 | 9 | 2 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 11 | 36 | 12 | 32 | 4 pts |
| 2026-2027 | 11 | 2 | 12 | 2 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 246 | 624 | 2.537 | 41.5% | 27.6% | 30.9% | 8.9% | 44.67 |
| 2026-2027 | 35 | 88 | 2.514 | 40.0% | 25.7% | 34.3% | 5.7% | 6.86 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.667)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.600 | 4.667 |
| 2026-2027 | 2.429 | 3.286 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\greece1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\greece1\charts\season_trends_avg_goals.png)

