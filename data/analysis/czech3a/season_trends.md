# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:47:24+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | SK Kladno | 72 | Domazlice | 3 pts |
| 2026-2027 | Domazlice | 19 | Kraluv Dvur | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - Domazlice beat Kraluv Dvur by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 3 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 72 | 69 | 52 | 48 | 38 | 28 |
| 2026-2027 | 19 | 19 | 16 | 13 | 7 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 38 | 14 | 34 | 4 pts |
| 2026-2027 | 13 | 7 | 14 | 7 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 272 | 869 | 3.195 | 45.6% | 21.0% | 33.5% | 6.2% | 44.65 |
| 2026-2027 | 65 | 216 | 3.323 | 38.5% | 29.2% | 32.3% | 10.8% | 11.0 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.471)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.059 | 4.471 |
| 2026-2027 | 1.875 | 4.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\czech3a\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\czech3a\charts\season_trends_avg_goals.png)

