from ninja import Router
from django.contrib.auth.models import User
from rentoro.models import RentalProperty, RentalPropertyUnit
from ninja import Schema
from uuid import uuid4

class RentalCreateSchema(Schema):
    address: str
    city: str
    province: str
    postal_code: str
    property_type: int
    status: str


router = Router()

@router.get('/')
def get_rentals(request):

    return {"ok": True}


@router.post('/')
def create_rental(request, rental: RentalCreateSchema):
    user = User.objects.filter(id=2).first()

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
    return {"ok": False}

@router.get('/{id}')
def get_rental_details(request, id):

    return {"id": id}

@router.put('/{id}')
def update_rental(request, id):

    return {"id": id}

@router.delete('/{id}')
def delete_rental(request, id):

    return {"id": id}
