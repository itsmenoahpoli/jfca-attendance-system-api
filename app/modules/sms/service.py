from app.libs.sms_lib import SmsLib



def send_sms(message: str, phone_number: str):
    if SmsLib.validate_phonenumber(phone_number) is False:
        return False

    return SmsLib.send_message(message, phone_number)