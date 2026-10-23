"""Feature-engineering modules.

Each module is pure: given a team's list of *prior* TeamRecords it returns the
feature value. The temporal ordering/leakage guarantees are enforced by the
orchestrator in build_features.py (match groups are processed so that a match
only ever observes strictly-earlier matches).
"""
