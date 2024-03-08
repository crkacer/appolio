from ninja import Router, Schema
from django.contrib.auth.models import User
from rentoro.models import LandlordProfile, TenantProfile
from django.contrib.auth import authenticate

router = Router()

class UserLoginSchema(Schema):
    email: str
    password: str


class UserRegisterSchema(Schema):
    email: str
    password: str
    user_type: str


@router.post('/login')
def login(request, user_login: UserLoginSchema):
    try:
        user = authenticate(username=user_login.email, password=user_login.password)
        if user:
        
            return {"token": "Login Token"}
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