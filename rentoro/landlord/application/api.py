from ninja import Router
import logging 
from ninja import Schema
from rentoro.rentoro_auth.authorization import CookieAuth

router = Router()

class ApplicationCreateSchema(Schema):
    pass



@router.get('/')
def get_all_applications(request):
    logger = logging.getLogger('django')
    try:
        pass
    except Exception as e:
        logger.info(str(e))


@router.get('/{id}', auth=CookieAuth())
def get_application_details(request, id):
    pass


@router.put('/{id}', auth=CookieAuth())
def update_application_details(request, id):
    pass


@router.post('/')
def create_application(request):
    pass


@router.delete('/{id}', auth=CookieAuth())
def delete_application(request, id):
    pass

