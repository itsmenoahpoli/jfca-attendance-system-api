from fastapi import APIRouter, HTTPException, status
from app.modules.sms.dto import SendSmsDTO
from app.modules.sms import service as sms_service
from app.utils.response_utils import HTTPResponse


smsRouter = APIRouter(
	prefix="/v1/sms",
	tags=["SMS API"]
)



@smsRouter.post('/send-sms')
def send_sms_handler(payload: SendSmsDTO):
	message = sms_service.send_sms(payload.message, payload.number)

	if message:
		return HTTPResponse(
			status_code=status.HTTP_200_OK,
			detail={
				"message": "SMS notification sent"
			}
		)
	
	raise HTTPException(
		status_code=status.HTTP_400_BAD_REQUEST,
		detail="SMS failed to sent"
	)