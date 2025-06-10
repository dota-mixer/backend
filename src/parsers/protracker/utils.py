from typing import List, Dict

from src.api.routes.heroes.schemas import (
    HeroOut,
    PositionStats,
    PrimaryAttribute,
)


def _convert_single_hero_json_to_hero_out(hero_data: Dict) -> HeroOut:
    """Converts a single hero's JSON data to a HeroOut object."""
    data = hero_data.copy()

    data["name"] = data.pop("displayName")
    data["primary_attribute"] = PrimaryAttribute(data["primary_attribute"])
    data["all_elo"] = data.pop("all elo", None)
    data["all_matches"] = data.pop("all matches", 0)
    data["all_winrate"] = data.pop("all winrate", 0.0)

    for position in range(1, 6):
        position_key = f"pos {position}"
        data[f"pos_{position}"] = PositionStats(
            elo=data.pop(f"{position_key} elo", None),
            matches=data.pop(f"{position_key} matches", 0),
            winrate=data.pop(f"{position_key} winrate", 0.0),
        )
    return HeroOut(**data)


def convert_json_to_heroes(json_data: List[Dict]) -> List[HeroOut]:
    """Converts a list of hero JSON data to a list of HeroOut objects."""
    heroes = [
        _convert_single_hero_json_to_hero_out(hero_data)
        for hero_data in json_data
    ]
    return heroes
