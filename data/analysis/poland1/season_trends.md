# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:02:59+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Ekstraklasa (Poland)
- Scope: league `poland1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 0 seasons

| season | margin | tight |
|---|---|---|

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._


## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|

## 6. View divergence

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\poland1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\poland1\charts\season_trends_avg_goals.png)

