import requests, urllib
from src.config.settings import appSettings

class SmsLib:
    __SEMAPHORE_SENDER_NAME=appSettings.app_semaphore_sender_name
    __SEMAPHORE_API_KEY=appSettings.app_semaphore_key
    __SEMAPHORE_API_URL=appSettings.app_semaphore_url

    def __init__(self):
        pass

    @classmethod
    def __createApiUrl(self, params: tuple):
        return self.__SEMAPHORE_API_URL + urllib.parse.urlencode(params)
    
    @classmethod
    def __createParams(self, message: str, number: str):
        return (
                ('apikey', self.__SEMAPHORE_API_KEY),
                ('sendername', self.__SEMAPHORE_SENDER_NAME),
                ('message', message),
                ('number', number)
            )

    @classmethod
    def send_message(self, message: str, number: str):
        try:
            params = self.__createParams(message, number)
            path = self.__createApiUrl(params)
            response = requests.post(path)
            response.raise_for_status()

            print(f"send_message= Send message to {number} success!")
            
            return True
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message: {e}") 
            return False  