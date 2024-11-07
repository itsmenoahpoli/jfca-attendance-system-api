import datetime
from fastapi import HTTPException, status
from bson.objectid import ObjectId
from app.database.connection import db_get_collection
from app.utils.password_utils import hash_password
from .dto import AccountDTO

users_collection = db_get_collection(collection='users', create_if_not_exist=True)

class UsersService:
    @classmethod
    def create_account(data: AccountDTO):
        existing_account = users_collection.find_one({"email": data.email})
        if existing_account:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email is already in use"
            )

        account_data = {
            "fullname": data.fullname,
            "email": data.email,
            "password": hash_password(data.password), 
            "usertype": data.usertype,
            "created_at": datetime.datetime.now()
        }

        return users_collection.insert_one(account_data)
    

    @classmethod
    def list_accounts():
        accounts = users_collection.find()

        return [{**account, "_id": str(account["_id"])} for account in accounts]

    
    @classmethod
    def get_account_by_id(account_id: str):
        account = users_collection.find_one({"_id": ObjectId(account_id)})
        if account:
            account["_id"] = str(account["_id"])

        return account

    
    @classmethod
    def update_account_by_id(account_id: str, data: AccountDTO):
        update_data = {
            "fullname": data.fullname,
            "email": data.email,
            "password": data.password,
            "usertype": data.usertype,
            "updated_at": datetime.datetime.now()
        }

        result = users_collection.update_one(
            {"_id": ObjectId(account_id)},
            {"$set": update_data}
        )
        
        return result.modified_count > 0

    
    @classmethod
    def delete_account_by_id(account_id: str):
        result = users_collection.delete_one({"_id": ObjectId(account_id)})

        return result.deleted_count > 0