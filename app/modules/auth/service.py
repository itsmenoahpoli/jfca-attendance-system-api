import time
import jwt 
from app.config.settings import app_settings

JWT_SECRET_KEY = app_settings.app_secret_key
JWT_ALGORITHM = 'HS256'

def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + 5 * 3600  # 5 hours
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

        if decoded_token["expires"] >= time.time():
            return decoded_token
        
        return None
    except:
        return {}