# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:55:29+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Serie A Betano (Brazil)
- Scope: league `brazil1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Flamengo RJ | 78 | Palmeiras | 5 pts |
| 2026 | Flamengo RJ | 60 | Palmeiras | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026** - Flamengo RJ beat Palmeiras by **3** pts

| season | margin | tight |
|---|---|---|
| 2025 | 5 pts |  |
| 2026 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025 | 78 | 73 | 67 | 63 | 42 | 17 |
| 2026 | 60 | 57 | 48 | 45 | 29 | 18 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 17 | 42 | 18 | 35 | 7 pts |
| 2026 | 17 | 29 | 18 | 28 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 380 | 959 | 2.524 | 50.3% | 26.1% | 23.7% | 7.1% | 26.02 |
| 2026 | 277 | 739 | 2.668 | 46.9% | 27.8% | 25.3% | 5.8% | 37.7 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 12.550)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 9.750 | 12.550 |
| 2026 | 2.400 | 6.100 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\brazil1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\brazil1\charts\season_trends_avg_goals.png)

