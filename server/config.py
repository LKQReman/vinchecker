from pydantic_settings import BaseSettings
# import pyda

class Settings(BaseSettings):
    # db settings
    VIN_USERNAME: str
    VIN_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()