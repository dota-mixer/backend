from fastapi import APIRouter, HTTPException

from src.api.routes.heroes.schemas import HeroOut, HeroesOut
from src.parsers.protracker.api import get_heroes_list, get_hero_by_name

heroes_router = APIRouter(prefix="/heroes", tags=["heroes"])


@heroes_router.get("/")
async def read_heroes() -> HeroesOut:
    """
    Get the list of heroes.
    """
    heroes = await get_heroes_list()
    return HeroesOut(data=heroes, count=len(heroes))


@heroes_router.get("/{name}")
async def read_hero_by_name(name: str) -> HeroOut:
    """
    Get the hero by NPC name.
    """
    hero = await get_hero_by_name(name=name)
    if hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero
