from ninja import Router, Schema
from rentoro.landlord.rentals.api import router as rentals_router
from rentoro.models import LandlordProfile
import logging

router = Router()

router.add_router('/rentals', rentals_router)

class LandlordUpdateProfileSchema(Schema):

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


@router.get('/profile')
def get_profile(request, user):
    
    try:
        profile = LandlordProfile.objects.filter(user_id=user.id).first()
        if profile:
            return {profile}
        return {"error": "No profile"}
    
    except Exception as e:
        return {"error": str(e)}
    

@router.put("/profile")
def update_profile(request, user, profile: LandlordUpdateProfileSchema):
    logger = logging.getLogger('django')
    try:
        profile = LandlordProfile(
            first_name=profile.first_name,
            last_name=profile.last_name,
            middle_name=profile.middle_name,
            dob=profile.dob,
            address=profile.address,
            city=profile.city,
            province=profile.province,
            postal_code=profile.postal_code,
            phone=profile.phone,
            user_id=user.id
        )
        profile.save()
        return {"ok": True}
    except Exception as e:
        logger.debug(str(e))
        return {"error": "Something went wrong"}