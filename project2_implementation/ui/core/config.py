import pydantic


class Settings(pydantic.BaseSettings):
    version: str = "1.0"
    releaseId: str = "1.1"
    API_V1_STR: str = "/api/v1"


settings = Settings()
