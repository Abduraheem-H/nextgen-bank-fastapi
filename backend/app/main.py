from fastapi import FastAPI
from backend.app.api.main import router as api_router
from backend.app.core.config import settings
from contextlib import asynccontextmanager
from backend.app.core.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    await init_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    lifespan=lifespan,
)

app.include_router(api_router, prefix=settings.API_V1_STR)
