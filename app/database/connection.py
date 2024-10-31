from pymongo import mongo_client
from app.config.settings import appSettings

db_client = mongo_client.MongoClient(
  appSettings.app_database_url
)
db_database = db_client.jcfamongodb

def db_get_collection(collection: str):
  if not collection:  
    raise ValueError("Collection name must be a non-empty string")

  return db_database[collection]

def db_connect():
  try:
    server_info = db_client.server_info()
    print(f'Connected to server. Server info {server_info}')
  except Exception:
    print('Failed to established connection to mongodb')


print('db_get_collection=', db_get_collection('app_settings'))
