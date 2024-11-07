from pymongo import mongo_client
from app.config.settings import app_settings

db_client = mongo_client.MongoClient(
	host=app_settings.app_database_url
)
db_database = db_client['jcfadb']

def db_get_collection(collection: str, create_if_not_exist: bool = False):
	if not collection:  
		raise ValueError("Collection name must be a non-empty string")

	if create_if_not_exist and collection not in db_database.list_collection_names():
		db_database.create_collection(collection)

	return db_database[collection]

def db_connect():
	try:
		server_info = db_client.server_info()
		print(f'Connected to server. Server info {server_info}')
	except Exception:
		print('Failed to established connection to mongodb')
