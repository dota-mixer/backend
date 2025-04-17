from fastapi import APIRouter

from src.api.routes.heroes.schemas import HeroesOut
from src.parsers.protracker.api import get_heroes_list

heroes_router = APIRouter(prefix="/heroes", tags=["heroes"])


@heroes_router.get("/")
async def get_heroes() -> HeroesOut:
    """
    Get the list of heroes.
    """
    heroes = await get_heroes_list()
    return HeroesOut(data=heroes, count=len(heroes))
