from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):

   DATABASE_URL: str
   ALLOWED_ORIGINS: str = ""
   SECRET_KEY: str
   DEBUG: bool = False
   API_PREFIX: str = "/api"

   @field_validator("ALLOWED_ORIGINS")
   @classmethod
   def parse_allowed_origins(cls, v: str) -> List[str]:

      al_or = [origin.strip() for origin in v.split(",")] if v else []

      return al_or

   class Config:
      env_file= ".env"
      env_file_encoding = "utf-8"
      case_sensitive = True

settings = Settings()