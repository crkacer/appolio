from ninja import NinjaAPI
import orjson
from ninja.renderers import BaseRenderer
from rentoro.api import router as rentoro_router
class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)
    
# api = NinjaAPI(renderer=ORJSONRenderer())
api = NinjaAPI()
api.add_router("/rentoro/", rentoro_router)
