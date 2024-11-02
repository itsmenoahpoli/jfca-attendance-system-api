from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
  app_debug: bool = False
  app_secret_key: str
  app_database_url: str
  app_semaphore_url: str
  app_semaphore_key: str
  app_semaphore_sender_name: str

  class Config:
    env_file = '.env'


appSettings = AppSettings()
