from ninja import Router, Schema
from rentoro.landlord.rentals.api import router as rentals_router

router = Router()

router.add_router('/rentals', rentals_router)

class LandlordCreateProfileSchema(Schema):

    first_name: str
    last_name: str
    middle_name: str
    dob: str
    address: str
    city: str
    province: str
    postal_code: str
    phone: str
    user_id: int


class LandlordUpdateProfileSchema(Schema):
    pass


@router.get('/profile')
def get_profile(request):
    
    return {"msg": "Profile"}


@router.post("/profile")
def create_profile(request, profile: LandlordCreateProfileSchema):

    return profile


@router.put("/profile")
def update_profile(request, profile: LandlordUpdateProfileSchema):

    return profile