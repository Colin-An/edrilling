from pydantic import BaseSettings

# default settings if there are nothing in environment
class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PUBLIC_VERSION: str = "0.001"
    PROJECT_NAME: str = "test_task"
    SECRET_KEY: str = "secret_key"
    WS_HOST: str = "demo.edrilling.no"
    WS_PORT:str = ""
    WS_PATH: str = "wells/3e927eeba131/app/ws"
    STR_MAX_LEN: int = 500
    TOKEN_MAX_LEN: int = 5000
    TIMEOUT: int = 20

settings = Settings()
