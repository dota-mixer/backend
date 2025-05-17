from fastapi import FastAPI
from fastapi.routing import APIRoute

from src.api.main import api_router

API_V1_STR = "/api/v1"


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags}-{route.name}"


app = FastAPI(
    title="Dota Mixer API",
    openapi_url=f"{API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

app.include_router(api_router, prefix=API_V1_STR)
