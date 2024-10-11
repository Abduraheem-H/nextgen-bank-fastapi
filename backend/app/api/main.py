from fastapi import APIRouter
from routes import home

router = APIRouter()
router.include_router(home.router)
