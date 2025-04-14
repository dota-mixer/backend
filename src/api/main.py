from fastapi import APIRouter


api_router = APIRouter()


@api_router.get("/healthcheck", include_in_schema=True)
def healthcheck():
    return {"status": "ok"}
