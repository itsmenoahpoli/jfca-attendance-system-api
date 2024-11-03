from fastapi import APIRouter, Response, status
from pydantic import BaseModel, constr
from typing import Annotated
from src.libs.sms_lib import SmsLib


smsRouter = APIRouter(
	prefix="/v1/sms",
	tags=["sms"]
)

class SendSmsPayload(BaseModel):
	message: Annotated[str, constr(min_length=1)]
	number: Annotated[str, constr(min_length=11)]

@smsRouter.post('/send-sms')
async def sendSms(payload: SendSmsPayload, response: Response):
	message = await SmsLib.send_message('JFCA SMS Notification', '09620636535')

	if message:
		return Response(
			status_code=status.HTTP_200_OK,
			content={
				message: "SMS notification sent"
			}
		)

	return Response(
		status_code=status.HTTP_400_BAD_REQUEST,
		content={
			message: "Failed to send SMS notification"
		}
	)