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
    # Invitation to apply for a rental property
    pass


@router.delete('/{id}', auth=CookieAuth())
def delete_application(request, id):
    pass


@router.post('/{id}/approve', auth=CookieAuth())
def approve_application(request):
    logger = logging.getLogger('django')
    try:

        return {'ok': True}
    except Exception as e:
        logger.info(str(e))
        return {'error': str(e)} 
    


@router.post('/{id}/reject', auth=CookieAuth())
def reject_application(request):
    logger = logging.getLogger('django')
    try:

        return {'ok': True}
    except Exception as e:
        logger.info(str(e))
        return {'error': str(e)}