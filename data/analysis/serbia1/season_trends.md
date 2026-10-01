# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:08:06+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Mozzart Bet Super Liga (Serbia)
- Scope: league `serbia1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Crvena zvezda | 86 | Vojvodina | 10 pts |
| 2026-2027 | Crvena zvezda | 28 | Vojvodina | 6 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2026-2027** - Crvena zvezda beat Vojvodina by **6** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 10 pts |  |
| 2026-2027 | 6 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 11 = last safe, 14 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 11 | pos 14 |
|---|---|---|---|---|---|---|
| 2025-2026 | 86 | 76 | 59 | 50 | 46 | 42 |
| 2026-2027 | 28 | 22 | 16 | 14 | 8 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 11 | 46 | 12 | 45 | 1 pts |
| 2026-2027 | 11 | 8 | 12 | 8 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 297 | 790 | 2.66 | 41.8% | 29.0% | 29.3% | 12.1% | 50.31 |
| 2026-2027 | 68 | 182 | 2.676 | 51.5% | 26.5% | 22.1% | 8.8% | 13.29 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 4.714)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.375 | 4.375 |
| 2026-2027 | 1.857 | 4.714 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\serbia1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\serbia1\charts\season_trends_avg_goals.png)

