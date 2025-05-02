from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Pick up from .env or Kubernetes secrets
    MYSQL_HOST: str = "surveys.cg3bzfpbc7p1.us-east-1.rds.amazonaws.com"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "admin"
    MYSQL_PASSWORD: str = "Shashi_123"
    MYSQL_DB: str = "surveyforms"

    @property
    def sqlalchemy_database_uri(self) -> str:
        return (
            f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
