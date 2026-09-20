"""Feature group D: rest days.

rest_days = number of whole days since the team's most recent completed match
(any venue) before the target match. Records are appended in strict
chronological order, so the last record is the most recent prior match.

When a team has no prior match in the collected period (season opener) there
is no observable rest value -> None (NULL), reported by the validation step.
"""
from __future__ import annotations

from datetime import date

from .records import TeamRecord


def rest_days(records: list[TeamRecord], match_date: date) -> int | None:
    if not records:
        return None
    return (match_date - records[-1].match_date).days