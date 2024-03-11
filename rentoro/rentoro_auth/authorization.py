from typing import Any
from django.http import HttpRequest
from ninja.security import APIKeyCookie
from django.contrib.auth.models import User
from ninja.errors import HttpError
from rentoro.rentoro_auth.crypto import decode
import json

class CookieAuth(APIKeyCookie):
    param_name = "api_token"
    def authenticate(self, request, key):
        # decode token 
        if not key:
            raise HttpError(401, "Unauthorized! Please login")
        
        token_decode = decode(key, "implicit_assertion").decode('utf-8')
        payload_decode = json.loads(token_decode.replace("'", '"'))
        user = User.objects.filter(email=payload_decode.get('email')).first()
        if not user:
            raise HttpError(401, "Unauthorized! Please user enter")
        return user
    
class RefreshCookieAuth(APIKeyCookie):
    param_name = "refresh_token"
    def authenticate(self, request: HttpRequest, key: str | None) -> Any | None:
        return key
