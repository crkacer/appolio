from ninja import Router

router = Router()

@router.post('/request{id}')
def requet_to_sign(request, id):
    return {"ok": True}


@router.get('/request')
def get_all_requests(request):
    return {"ok": True}


@router.get('/request/{id}')
def get_request_details(request, id):
    return {"ok": True}



