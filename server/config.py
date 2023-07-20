from pydantic_settings import BaseSettings
# import pyda

class Settings(BaseSettings):
    # db settings
    USERNAME: str
    PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()