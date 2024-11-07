from fastapi import APIRouter, Response, status
from .dto import LoginDTO
from .service import sign_jwt


authRouter = APIRouter(
	prefix="/v1/auth",
	tags=["auth"]
)


@authRouter.post('/login')
def login_handler(payload: LoginDTO):
    return sign_jwt(1)


