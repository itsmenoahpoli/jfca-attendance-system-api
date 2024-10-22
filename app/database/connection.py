DATABASE_URL = "mongodb://root:root@localhost:27017/jcfamongodb?retryWrites=true&w=majority"

from pymongo import mongo_client

db_client = mongo_client.MongoClient(
  DATABASE_URL
)

try:
  server_info = db_client.server_info()
  print(f'Connected to server. Server info {server_info}')
except Exception:
  print('Failed to established connection to mongodb')

db_database = db_client.jcfamongodb