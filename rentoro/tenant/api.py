from ninja import Router

router = Router()

@router.get('/{id}')
def get_tenant_profile(request, id):
    return {"ok": True}


@router.get('/')
def get_all_tenants(request):
    return {"ok": True}


@router.post('/')
def create_tenant(request):
    return {"ok": True}


@router.put('/{id}')
def update_tenant(request, id):
    return {"ok": True}


@router.delete('/{id}')
def delete_tenant(request, id):
    return {"ok": True}


