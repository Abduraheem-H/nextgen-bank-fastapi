from fastapi import APIRouter

router = APIRouter(prefix="/home")


@router.get("/")
async def home():
    return {"message": "Welcome to the NextGen Bank API!"}
