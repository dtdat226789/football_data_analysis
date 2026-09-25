# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:58:18+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Veikkausliiga (Finland)
- Scope: league `finland1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Inter Turku | 46 | Ilves | 1 pts |
| 2026 | KuPS | 48 | Inter Turku | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026** - KuPS beat Inter Turku by **0** pts

| season | margin | tight |
|---|---|---|
| 2025 | 1 pts | yes |
| 2026 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025 | 46 | 45 | 44 | 28 | 21 | 14 |
| 2026 | 48 | 48 | 41 | 34 | 25 | 14 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 9 | 21 | 10 | 18 | 3 pts |
| 2026 | 9 | 25 | 10 | 19 | 6 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 132 | 433 | 3.28 | 42.4% | 22.0% | 35.6% | 6.1% | 30.58 |
| 2026 | 141 | 356 | 2.525 | 44.7% | 27.0% | 28.4% | 7.1% | 32.08 |

## 6. View divergence
- Largest divergence: **2026** (goals view, avg abs position diff = 5.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 2.167 | 4.167 |
| 2026 | 2.167 | 5.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\finland1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\finland1\charts\season_trends_avg_goals.png)

