from fastapi import APIRouter, HTTPException, status
from typing import List
from .dto import AccountDTO
from .service import UsersService
from app.utils.response_utils import HTTPResponse

accountsRouter = APIRouter(
	prefix="/v1/accounts",
	tags=["accounts"]
)

@accountsRouter.post('/')
def create_account_handler(payload: AccountDTO):
    UsersService.create_account(payload)
    
    return HTTPResponse(
		status_code=status.HTTP_201_CREATED,
		body="Account created"
	)

@accountsRouter.get('/', response_model=List[AccountDTO])
def list_accounts_handler():
    accounts = UsersService.list_accounts()
    
    return accounts

@accountsRouter.get('/{account_id}', response_model=AccountDTO)
def get_account_handler(account_id: str):
    account = UsersService.get_account_by_id(account_id)
    
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    return account

@accountsRouter.put('/{account_id}')
def update_account_handler(account_id: str, payload: AccountDTO):
    updated = UsersService.update_account_by_id(account_id, payload)
    
    if not updated:
        raise HTTPException(status_code=404, detail="Account not found")
    
    return HTTPResponse(
        status_code=status.HTTP_200_OK,
        body={"message": "Account updated successfully"}
    )

@accountsRouter.delete('/{account_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_account_handler(account_id: str):
    deleted = UsersService.delete_account_by_id(account_id)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="Account not found")
    
    return {"message": "Account deleted successfully"}