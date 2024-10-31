
from fastapi import Depends
from typing import List
from app.database.connection import db_get_collection
from app.database.utils import format_document

# @app.get("/app-settings", response_model=List[dict])
# async def get_app_settings(collection=Depends(lambda: db_get_collection("app_settings"))):
#   documents = collection.find()
#   return [format_document(doc) for doc in documents]