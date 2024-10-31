from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
  app_debug: bool
  app_secret_key: str
  app_database_url: str

  class Config:
    env_file = '.env'


appSettings = AppSettings()
