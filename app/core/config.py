from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "todo_app"
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
