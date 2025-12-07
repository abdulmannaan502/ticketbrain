from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "TicketBrain"

    # ⚠️ In production, override via environment variable
    SECRET_KEY: str = "CHANGE_THIS_SECRET_KEY"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    ALGORITHM: str = "HS256"

    # Local SQLite DB (for dev). In Docker we'll override with Postgres URL via env.
    BASE_DIR: Path = Path(__file__).resolve().parents[2]
    SQLITE_PATH: Path = BASE_DIR / "ticketbrain.db"
    DATABASE_URL: str = f"sqlite:///{SQLITE_PATH}"

    # Pydantic v2 config
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
