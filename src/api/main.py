from fastapi import APIRouter

from src.api.routes.heroes.router import heroes_router


api_router = APIRouter()

api_router.include_router(heroes_router)


@api_router.get("/healthcheck", include_in_schema=True)
def healthcheck():
    return {"status": "ok"}
