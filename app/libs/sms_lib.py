import re
import requests, urllib
from app.config.settings import app_settings

class SmsLib:
    __SEMAPHORE_SENDER_NAME=app_settings.app_semaphore_sender_name
    __SEMAPHORE_API_KEY=app_settings.app_semaphore_key
    __SEMAPHORE_API_URL=app_settings.app_semaphore_url

    def __init__(self):
        pass

    @classmethod
    def __create_api_url(self, params: tuple):
        return self.__SEMAPHORE_API_URL + urllib.parse.urlencode(params)
    
    @classmethod
    def __create_params(self, message: str, phone_number: str):
        return (
                ('apikey', self.__SEMAPHORE_API_KEY),
                ('sendername', self.__SEMAPHORE_SENDER_NAME),
                ('message', message),
                ('number', phone_number)
            )
    
    @classmethod
    def __create_attendance_sms_template(self, contents: dict):
        template = '''
        Attendance sms
        '''

        pass

    @classmethod
    def __create_otp_sms_template(self, phone_number: str):
        template = '''
        OTP sms
        '''
        pass
    
    @classmethod
    def validate_phonenumber(self, phone_number: str):
        accepted_pattern = r"^096\d{8}$"

        if re.match(accepted_pattern, phone_number):
            return True
        
        return False


    @classmethod
    def send_message(self, message: str, phone_number: str):
        params = self.__create_params(message, phone_number)
        path = self.__create_api_url(params)
        response = requests.post(path)
        response.raise_for_status()
        response_data = response.json()

        print(response_data)

        if response_data and type(response_data) is list and response_data[0]['message_id'] is not None:
            return True
        
        return False