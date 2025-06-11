from http import HTTPStatus

from fastapi import HTTPException
from httpx import HTTPStatusError

from src.api.routes.heroes.schemas import HeroItemsOut
from src.parsers.protracker.base import client
from src.parsers.protracker.utils import convert_json_to_heroes


async def get_heroes_list() -> dict:
    """Get all heroes from Dota 2 Pro Tracker API.

    Returns:
        dict: A dictionary containing hero data.
    """
    response = await client.get("/heroes/list")

    if response.status_code != HTTPStatus.OK:
        raise HTTPStatusError(
            f"Error: {response.status_code} - {response.text}",
            request=response.request,
            response=response,
        )
    return convert_json_to_heroes(response.json())


async def get_hero_by_name(name: str) -> dict:
    """
    Get a hero by its NPC name from Dota 2 Pro Tracker API.

    Args:
        name: The NPC name of the hero.
    """
    heroes = await get_heroes_list()
    for hero in heroes:
        if hero.npc == name:
            return hero
    return None


async def get_hero_items(hero_id: int, position: str, days: int):
    """
    Get the items for a specific hero and position from Dota 2 Pro Tracker API.

    Args:
        hero_id: The ID of the hero.
        position: The position of the hero (e.g., "pos 1", "pos 2").
        days: The number of days to consider for the data.

    Returns:
        HeroItemsOut: A HeroItemsOut object containing the hero's item data.
    """
    response = await client.get(
        "/hero-items",
        params={"hero_id": hero_id, "position": position, "days": days},
    )
    if response.status_code != HTTPStatus.OK:
        raise HTTPException(
            status_code=response.status_code, detail={"error": response.text}
        )
    if len(response.json()) == 0:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail={"error": "Hero not found"},
        )
    return HeroItemsOut(**response.json()[0])
