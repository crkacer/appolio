from ninja import Router
import logging 
from ninja import Schema

router = Router()

class RentalUnitCreateSchema(Schema):
    pass

class RentalUnitUpdateSchema(Schema):
    pass

class RentalUnitGetSchema(Schema):
    pass


@router.get('/')
def get_rental_units(request):
    logger = logging.getLogger('django')
    try:
        pass
    except Exception as e:
        logger.info(str(e))


@router.post('/')
def create_rental_unit(request, rental_unit: RentalUnitCreateSchema):
    logger = logging.getLogger('django')
    try:
        pass
    except Exception as e:
        logger.info(str(e))


@router.delete('/')
def delete_rental_unit(request):
    logger = logging.getLogger('django')
    try:
        pass
    except Exception as e:
        logger.info(str(e))


@router.put('/')
def update_rental_unit(request):
    logger = logging.getLogger('django')
    try:
        pass
    except Exception as e:
        logger.info(str(e))


