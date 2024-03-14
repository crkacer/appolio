from ninja import Router
from django.contrib.auth.models import User
from rentoro.models import RentalProperty, RentalPropertyUnit, LandlordProfile
from ninja import Schema
from uuid import uuid4
from rentoro.rentoro_auth.authorization import CookieAuth, RefreshCookieAuth
from rentoro.utils.property_code import generate_unique_property_code
from rentoro.models import RentalPropertyShare
import logging
from datetime import datetime
from rentoro.landlord.rentals.utils import fetch_rental_share_code
from rentoro.landlord.application.api import router as application_router

router = Router()

class RentalCreateSchema(Schema):
    address: str
    city: str
    province: str
    postal_code: str
    property_type: int
    status: str


class RentalUnitCreateSchema(Schema):
    pass

class RentalIDSchema(Schema):
    id: str



@router.post('/share')
def share_rental(request, rental_id: RentalIDSchema):
    try:    
        rental = RentalProperty.objects.filter(rental_id=rental_id).first()
        if rental:
            # generate rental_id and look-up for the same id if exists
            code = fetch_rental_share_code(rental)
            return {'code': code}
        return {''}
    except Exception as e:
        return {'error': str(e)}


@router.get('/')
def get_rentals(request):

    try:
        user = request.auth
        if user:
            rentals = RentalProperty.objects.filter(user=user).all().values()
            return rentals
    except Exception as e:
        return {"error": str(e)}


@router.post('/', auth=CookieAuth())
def create_rental(request, rental: RentalCreateSchema):
    try:
        user = request.auth
        if user:
            new_rental = RentalProperty(
                address=rental.address,
                city=rental.city,
                province=rental.province,
                rental_id=str(uuid4()),
                property_type_id=rental.property_type,
                status=rental.status,
                owner=user
            )
            new_rental.save()
            return {"ok": True}
    except Exception as e:
        return {"ok": False}

@router.get('/{id}', auth=CookieAuth())
def get_rental_details(request, id):
    try:
        user = request.auth
        landlord = LandlordProfile.objects.filter(user=user).first()
        if landlord:
            rental = RentalProperty.objects.filter(owner=landlord, id=id).first()
            if rental:
                return rental.values()
            return {'error': 'Cannot get rental'}
        return {'error': 'User not found'}
    except Exception as e:
        return {'error': str(e)}

@router.put('/{id}', auth=CookieAuth())
def update_rental(request, id):
    try:
        user = request.auth
        landlord = LandlordProfile.objects.filter(user=user).first()

    except Exception as e:
        return {'error': str(e)}

@router.delete('/{id}')
def delete_rental(request, id):

    return {"id": id}
