from fastapi import APIRouter, Response, status
from pydantic import BaseModel, constr
from typing import Annotated
from app.libs.sms_lib import SmsLib


smsRouter = APIRouter(
	prefix="/v1/sms",
	tags=["sms"]
)

class SendSmsPayload(BaseModel):
	message: Annotated[str, constr(min_length=1)]
	number: Annotated[str, constr(min_length=11)]

@smsRouter.post('/send-sms')
def sendSms(payload: SendSmsPayload, response: Response):
	message = SmsLib.send_message


	return payload