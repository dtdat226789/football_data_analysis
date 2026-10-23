"""Shared data records for the feature layer.

Match   - one completed match as read from PostgreSQL.
TeamRecord - one team's participation in a match (a "leg"), i.e. the same
             match viewed from the home and from the away side. These are the
             atomic units the feature functions consume, so a team's "prior
             matches" are just its prior TeamRecords regardless of venue.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, time


@dataclass(frozen=True)
class Match:
    api_id: int
    league_season_id: int
    season: str
    game_index: int
    home_team_id: int
    away_team_id: int
    home_team: str
    away_team: str
    match_date: date
    kickoff_time: time
    home_score: int
    away_score: int

    def as_records(self) -> tuple["TeamRecord", "TeamRecord"]:
        """Split into the home-side and away-side TeamRecords of this match."""
        if self.home_score > self.away_score:
            home_points, home_win = 3, 1
            away_points, away_win = 0, 0
        elif self.home_score == self.away_score:
            home_points, home_win = 1, 0
            away_points, away_win = 1, 0
        else:
            home_points, home_win = 0, 0
            away_points, away_win = 3, 1
        home = TeamRecord(
            api_id=self.api_id,
            match_date=self.match_date,
            kickoff_time=self.kickoff_time,
            points=home_points,
            is_win=home_win,
            goals_for=self.home_score,
            goals_against=self.away_score,
            is_home=True,
        )
        away = TeamRecord(
            api_id=self.api_id,
            match_date=self.match_date,
            kickoff_time=self.kickoff_time,
            points=away_points,
            is_win=away_win,
            goals_for=self.away_score,
            goals_against=self.home_score,
            is_home=False,
        )
        return home, away


@dataclass(frozen=True)
class TeamRecord:
    api_id: int
    match_date: date
    kickoff_time: time
    points: int
    is_win: int
    goals_for: int
    goals_against: int
    is_home: bool
