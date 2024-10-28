from pymongo import mongo_client
from src.config import settings

db_client = mongo_client.MongoClient(
  settings.DATABASE_URL
)
db_database = db_client.jcfamongodb

try:
  server_info = db_client.server_info()
  print(f'Connected to server. Server info {server_info}')
except Exception:
  print('Failed to established connection to mongodb')

