from ninja import Router
from rentoro.tenant.api import router as tenant_router
from rentoro.landlord.api import router as landlord_router
from rentoro.rentoro_auth.api import router as auth_router

router = Router()

router.add_router('/auth/', auth_router)
router.add_router('/landlord/', landlord_router)
router.add_router('/tenant/', tenant_router)
