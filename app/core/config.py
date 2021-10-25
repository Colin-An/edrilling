from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PUBLIC_VERSION: str = "0.001"
    PROJECT_NAME: str = "test_task"
    SECRET_KEY: str = "secret_key"
    WS_HOST = "demo.edrilling.no/wells/3e927eeba131/app/ws?access_token="
    WS_PORT = "4000"

settings = Settings()
