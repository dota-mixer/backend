from http import HTTPStatus

from httpx import HTTPStatusError

from src.parsers.protracker.base import client


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

    return response.json()
