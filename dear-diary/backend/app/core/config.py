from pydantic import BaseSettings

class Settings(BaseSettings):
    AI_API_KEY: str
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
