from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from backend.app.core.config import settings
from backend.app.core.logging import get_logger

logger = get_logger()

engine = create_async_engine(
    settings.database_url,
    future=True,
)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"An error occurred while using database session: {e}")
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db():
    pass
