from fastapi import APIRouter

from src.parsers.protracker.api import get_heroes_list

heroes_router = APIRouter(prefix="/heroes", tags=["heroes"])


@heroes_router.get("/")
async def get_heroes():
    """
    Get the list of heroes.
    """
    heroes = await get_heroes_list()
    return heroes
