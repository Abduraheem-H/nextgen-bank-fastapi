from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

CURRENT_FILE = Path(__file__).resolve()
SRC_DIR = CURRENT_FILE.parent.parent.parent.parent
ENV_FILE_PATH = SRC_DIR / ".envs" / ".env.local"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    env: Literal["local", "staging", "production"] = "local"

    API_V1_STR: str
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_DESCRIPTION: str
    SITE_NAME: str
    DEBUG: bool = True
    database_url: str
    database_echo: bool = False
    MAIL_FROM: str
    MAIL_FROM_NAME: str
    SMTP_HOST: str = "mailpit"
    SMTP_PORT: int = 1025
    MAILPIT_UI_PORT: int = 8025

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    RABITMQ_HOST: str = "rabbitmq"
    RABITMQ_PORT: int = 5672
    RABITMQ_USER: str = "guest"
    RABITMQ_PASSWORD: str = "guest"

settings = Settings()
