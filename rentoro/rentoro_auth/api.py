from ninja import Router, Schema
from django.contrib.auth.models import User
from rentoro.models import LandlordProfile, TenantProfile
from django.contrib.auth import authenticate
from datetime import datetime, date
from rentoro.rentoro_auth.crypto import encode, decode
from django.http import HttpResponse, HttpRequest
from rentoro.rentoro_auth.authorization import CookieAuth, RefreshCookieAuth
import json 
import ast

router = Router()
cookie_auth = CookieAuth()

class UserLoginSchema(Schema):
    email: str
    password: str


class UserRegisterSchema(Schema):
    email: str
    password: str
    user_type: str

class UserTokenSchema(Schema):
    token: str

@router.post('/login')
def login(request, user_login: UserLoginSchema, response: HttpResponse):
    try:
        user = authenticate(username=user_login.email, password=user_login.password)
        if user:
            time_now = datetime.now()
            payload = {
                "email": user_login.email,
                "timestamp": int(time_now.timestamp())
            }
            token = encode(payload, "random_footer", "implicit_assertion" )
            token_str = token.decode("utf-8")
            # Update last login time
            user.last_login = time_now
            user.save()
            # Set response cookies
            response.set_cookie("refresh_token", token_str)
            response.set_cookie("api_token", token_str)

            return {"token": token_str}
        else:
            return {"error": "Invalid email or password"}
    except Exception as e:
        return {"error": str(e)}


@router.post('/register')
def register(request, user_register: UserRegisterSchema):
    try:
        # Check if email already existed
        if User.objects.filter(email=user_register.email).exists():
            return {"error": "Email already existed"}
        
        # Create a new user
        user = User.objects.create_user(
            user_register.email,
            user_register.email,
            user_register.password
        )
        # Create a new user profile
        if user_register.user_type == "landlord":
            new_landlord_profile = LandlordProfile(
                email=user_register.email,
                user=user
            )
            new_landlord_profile.save()
        elif user_register.user_type == "tenant":
            new_tenant_profile = TenantProfile(
                email=user_register.email,
                user=user
            )
            new_tenant_profile.save()
        else:
            return {'error': 'Invalid User Type'}
        
        return {"ok": True}
    
    except Exception as e:
        return {"error": str(e)}
    

@router.get('/validate-token', auth=CookieAuth())
def validate_token(request):
    try:
        user = request.auth
        return {"email": user.email}
    except Exception as e:
        return {"error": str(e)}
    

@router.post('/delegate', auth=RefreshCookieAuth())
def delegate(request):
    try:
        pass
    except Exception as e:
        return {"error": str(e)}