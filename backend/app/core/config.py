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


settings = Settings()
