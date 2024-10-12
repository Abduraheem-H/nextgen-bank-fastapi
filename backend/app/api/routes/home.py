from fastapi import APIRouter
from app.core.logging import get_logger

logger = get_logger()

router = APIRouter(prefix="/home")


@router.get("/")
async def home():
    # Log various levels of messages
    logger.info("Home endpoint accessed")
    logger.debug("Debugging home endpoint access")
    logger.warning("This is a warning from the home endpoint")
    logger.error("This is an error from the home endpoint")
    logger.critical("This is a critical message from the home endpoint")
    return {"message": "Welcome to the NextGen Bank API!"}
