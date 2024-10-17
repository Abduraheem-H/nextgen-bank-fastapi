from fastapi import APIRouter
from backend.app.api.routes import home

router = APIRouter()
router.include_router(home.router)
