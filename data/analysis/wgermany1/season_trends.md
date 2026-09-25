# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:51:14+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Bundesliga Women (Germany)
- Scope: league `wgermany1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Bayern Munich W | 74 | Wolfsburg W | 16 pts |
| 2026-2027 | Bayern Munich W | 15 | Eintracht Frankfurt W | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Bayern Munich W beat Eintracht Frankfurt W by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 16 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 11 = last safe, 14 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 11 | pos 14 |
|---|---|---|---|---|---|---|
| 2025-2026 | 74 | 58 | 46 | 43 | 22 | 11 |
| 2026-2027 | 15 | 13 | 10 | 9 | 3 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 11 | 22 | 12 | 18 | 4 pts |
| 2026-2027 | 11 | 3 | 12 | 3 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 182 | 627 | 3.445 | 44.5% | 17.6% | 37.9% | 3.8% | 36.71 |
| 2026-2027 | 35 | 121 | 3.457 | 48.6% | 14.3% | 37.1% | 0.0% | 7.14 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.286)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.429 | 4.286 |
| 2026-2027 | 1.714 | 3.714 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\wgermany1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\wgermany1\charts\season_trends_avg_goals.png)

