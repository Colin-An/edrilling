from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PUBLIC_VERSION: str = '0.001'
    PROJECT_NAME: str = "test_task"
    SECRET_KEY: str = 'secret_key'

settings = Settings()
