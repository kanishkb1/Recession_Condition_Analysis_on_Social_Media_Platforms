import fastapi
import uvicorn
from api import router
from core import settings
from fastapi import responses

app = fastapi.FastAPI(
    title="Reddit API - Reddit Scrapper",
    version=settings.releaseId,
)

# app.include_router(database.router, prefix=settings.API_V1_STR, tags=["DB"])
app.include_router(router.router, prefix=settings.API_V1_STR, tags=["API"])


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
