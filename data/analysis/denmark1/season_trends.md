# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:57:02+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Superliga (Denmark)
- Scope: league `denmark1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Aarhus | 67 | Midtjylland | 7 pts |
| 2026-2027 | FC Copenhagen | 24 | Midtjylland | 5 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2026-2027** - FC Copenhagen beat Midtjylland by **5** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 7 pts |  |
| 2026-2027 | 5 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025-2026 | 67 | 60 | 50 | 44 | 36 | 24 |
| 2026-2027 | 24 | 19 | 17 | 11 | 9 | 5 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 9 | 36 | 10 | 35 | 1 pts |
| 2026-2027 | 9 | 9 | 10 | 7 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 193 | 599 | 3.104 | 41.5% | 23.3% | 35.2% | 5.7% | 44.25 |
| 2026-2027 | 55 | 164 | 2.982 | 43.6% | 29.1% | 27.3% | 1.8% | 12.42 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 4.167)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.833 | 4.000 |
| 2026-2027 | 1.833 | 4.167 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\denmark1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\denmark1\charts\season_trends_avg_goals.png)

