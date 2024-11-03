from fastapi import APIRouter, Request, Response


smsRouter = APIRouter()

@smsRouter.post(
  prefix="/v1",
  tags=["sms"]
)
def sendSms(request: Request, response: Response):
  return request.body