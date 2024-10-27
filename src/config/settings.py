from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
  pass

DATABASE_URL = "mongodb://root:root@localhost:27017/jcfamongodb?retryWrites=true&w=majority"