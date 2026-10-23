# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:01:15+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Virsliga (Latvia)
- Scope: league `latvia`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Riga FC | 88 | RFS | 1 pts |
| 2026 | RFS | 74 | Riga FC | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025** - Riga FC beat RFS by **1** pts

| season | margin | tight |
|---|---|---|
| 2025 | 1 pts | yes |
| 2026 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025 | 88 | 87 | 48 | 38 | 36 | 31 |
| 2026 | 74 | 73 | 43 | 35 | 32 | 18 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 7 | 36 | 8 | 36 | 0 pts |
| 2026 | 7 | 32 | 8 | 26 | 6 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 182 | 535 | 2.94 | 45.6% | 23.6% | 30.8% | 6.0% | 45.73 |
| 2026 | 154 | 438 | 2.844 | 41.6% | 24.0% | 34.4% | 5.2% | 42.5 |

## 6. View divergence
- Largest divergence: **2026** (goals view, avg abs position diff = 3.200)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 2.909 | 2.182 |
| 2026 | 1.800 | 3.200 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\latvia\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\latvia\charts\season_trends_avg_goals.png)

