from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
from typing import Any, Dict, List, Optional, Union

class Settings(BaseSettings):
    SERVER_NAME: str
    SERVER_HOST: str
    SQLALCHEMY_DATABASE_URI: str
    DEPLOYMENT_LEVEL: str
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str

    class Config:
        case_sensitive = True

settings = Settings()