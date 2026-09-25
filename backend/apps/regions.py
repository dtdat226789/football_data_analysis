"""Country → continent (region) mapping for league grouping.

Groups the catalog's leagues into the dashboard buckets
``europe | asia | america | other``. Unknown or unlisted countries fall back
to ``other`` so the dashboard never breaks on a new league.
"""
from __future__ import annotations

EUROPE = {
    "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia-Herzegovina",
    "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "England",
    "Estonia", "Faroe Islands", "Finland", "France", "Georgia", "Germany",
    "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo",
    "Latvia", "Lithuania", "Luxembourg", "Macedonia", "Malta", "Moldova",
    "Montenegro", "Netherlands", "North Macedonia", "Northern Ireland",
    "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia",
    "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey",
    "Ukraine", "Wales",
}

ASIA = {
    "Azerbaijan", "Bahrain", "China", "India", "Indonesia", "Iran", "Iraq",
    "Israel", "Japan", "Jordan", "Kuwait", "Malaysia", "Mongolia", "Oman",
    "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore",
    "South Korea", "Syria", "Thailand", "United Arab Emirates", "Uzbekistan",
    "Vietnam",
}

AMERICA = {
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Costa Rica",
    "Ecuador", "Mexico", "Paraguay", "Peru", "Uruguay", "USA", "Venezuela",
}

OTHER = {
    "Algeria", "Australia", "Egypt", "Ghana", "Morocco", "Nigeria",
    "South Africa", "Tunisia",
}

_REGIONS = (EUROPE, ASIA, AMERICA, OTHER)
_REGION_NAMES = ("europe", "asia", "america", "other")


def league_region(country: str) -> str:
    """Bucket a league's country into a dashboard region."""
    for region, name in zip(_REGIONS, _REGION_NAMES, strict=True):
        if country in region:
            return name
    return "other"