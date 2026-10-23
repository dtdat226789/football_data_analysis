"""Unit tests for the upstream phantom-roster detection in db_common.

Phantom rows are teams.json/table entries that never play a match in
results.json and whose name is a hyphen-variant of a real participant
(e.g. 'MG-Bahia' vs 'Bahia', 'PK' vs 'PK-35'). etl_02 skips them; the
rule must never drop an actual participant and must stay inert pre-season.
"""
from __future__ import annotations

from scripts.db_common import phantom_team_names


def teams(*names):
    return [{"team": n, "slug": n.lower().replace(" ", "-")} for n in names]


def matches(home_away):
    return [{"homeTeam": h, "awayTeam": a} for h, a in home_away]


def test_brazil1_style_prefix_junk_is_phantom():
    # MG-Bahia (suffix of a participant), Atletico (dash-prefix of Atletico-MG)
    ph = phantom_team_names(
        teams("Bahia", "MG-Bahia", "Atletico-MG", "Atletico"),
        matches([("Bahia", "Atletico-MG")]),
    )
    assert ph == {"MG-Bahia", "Atletico"}


def test_participants_are_never_phantom():
    ph = phantom_team_names(
        teams("Bahia", "Bahia XI", "Bahia-B"),  # variants of a participant
        matches([("Bahia", "Vitoria")]),
    )
    assert "Bahia" not in ph


def test_junk_concatenating_two_participants_is_phantom():
    # japan1 2026: 'Varen Nagasaki-Avispa Fukuoka' suffix-matches 'Avispa Fukuoka'
    ph = phantom_team_names(
        teams("V-Varen Nagasaki", "Avispa Fukuoka", "Varen Nagasaki-Avispa Fukuoka"),
        matches([("V-Varen Nagasaki", "Avispa Fukuoka")]),
    )
    assert ph == {"Varen Nagasaki-Avispa Fukuoka"}


def test_dash_prefix_variants_of_participants_are_phantom():
    # 'PK' vs 'PK-35'; 'V' vs 'V-Varen Nagasaki'; 'Shimizu S' vs 'Shimizu S-Pulse'
    ph = phantom_team_names(
        teams("PK-35", "PK", "V-Varen Nagasaki", "V", "Shimizu S-Pulse", "Shimizu S"),
        matches([("PK-35", "V-Varen Nagasaki"), ("Shimizu S-Pulse", "PK-35")]),
    )
    assert ph == {"PK", "V", "Shimizu S"}


def test_space_variant_is_not_phantom():
    # kuwait 2026-2027: duplicate spelling 'Al Fahaheel' vs 'Al-Fahaheel' shares
    # no dash boundary, so it is NOT filtered - the slug merge in etl_02 owns it
    ph = phantom_team_names(
        teams("Al-Fahaheel", "Al Fahaheel"),
        matches([("Al-Fahaheel", "Al Qadisiya")]),
    )
    assert ph == set()


def test_unrelated_unreferenced_team_is_kept():
    ph = phantom_team_names(
        teams("Bahia", "Vitoria", "Mystery FC"),
        matches([("Bahia", "Vitoria")]),
    )
    assert "Mystery FC" not in ph


def test_empty_matches_never_filters():
    # pre-season: no participants yet, so nothing is dropped
    ph = phantom_team_names(teams("Bahia", "MG-Bahia"), [])
    assert ph == set()
    ph = phantom_team_names(teams("Bahia", "MG-Bahia"), matches([]))
    assert ph == set()


def test_non_dict_teams_and_matches_are_ignored():
    ph = phantom_team_names(
        ["Bahia", {"team": "MG-Bahia", "slug": "mg-bahia"}],
        [{"homeTeam": 7}, {"homeTeam": "Bahia", "awayTeam": "Vitoria", "score": 0}],
    )
    assert ph == {"MG-Bahia"}
