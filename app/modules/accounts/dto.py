from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr, Field


class AccountDTO(BaseModel):
    fullname: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)  
    usertype: str = Field(..., min_length=1, max_length=50)