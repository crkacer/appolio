from ninja import Router

router = Router()

@router.get('/profile')
def get_tenant_profile(request):
    return {"ok": True}