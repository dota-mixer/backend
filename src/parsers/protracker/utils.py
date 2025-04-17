from typing import List, Dict

from src.api.routes.heroes.schemas import (
    HeroOut,
    PositionStats,
    PrimaryAttribute,
)


def convert_json_to_heroes(json_data: List[Dict]) -> List[HeroOut]:
    heroes = []

    for hero_data in json_data:
        hero_data["name"] = hero_data.pop("displayName")
        hero_data["primary_attribute"] = PrimaryAttribute(
            hero_data["primary_attribute"]
        )

        for position in range(1, 6):
            position_key = f"pos {position}"
            hero_data[f"pos_{position}"] = PositionStats(
                elo=hero_data.get(f"{position_key} elo"),
                matches=hero_data.get(f"{position_key} matches", 0),
                winrate=hero_data.get(f"{position_key} winrate", 0.0),
            )

        keys_to_remove = [
            f"pos {i} {field}"
            for i in range(1, 6)
            for field in ["elo", "matches", "winrate"]
        ]
        keys_to_remove += ["all elo", "all matches", "all winrate"]
        for key in keys_to_remove:
            hero_data.pop(key, None)

        heroes.append(HeroOut(**hero_data))

    return heroes
