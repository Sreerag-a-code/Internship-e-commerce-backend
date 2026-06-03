from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str = Field("E-Commerce Backend", env="APP_TITLE")
    APP_VERSION: str = Field("1.0.0", env="APP_VERSION")
    APP_SECRET_KEY: str = Field(..., env="APP_SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    SERVER_HOST: str = Field("0.0.0.0", env="SERVER_HOST")
    SERVER_PORT: int = Field(8000, env="SERVER_PORT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
