from fastapi import HTTPException, status
from app.libs.sms_lib import SmsLib



def send_sms(message: str, phone_number: str):
    if SmsLib.validate_phonenumber(phone_number) is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid phone number format"
        )

    return SmsLib.send_message(message, phone_number)