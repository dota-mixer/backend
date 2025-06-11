from httpx import AsyncClient


headers = {
    "Referer": "https://dota2protracker.com/",
}
client = AsyncClient(
    base_url="https://dota2protracker.com/api", headers=headers
)
