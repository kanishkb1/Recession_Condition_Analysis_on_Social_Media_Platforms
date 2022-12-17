import fastapi

router = fastapi.APIRouter()


@router.get(
    "/db",
)
async def database_status():
    res = "PASS"
    return {"message": res}
