from ninja import Router

router = Router()

@router.get('/')
def root_get(request):
    
    return {"msg": "Tenant root route"}
