from ninja import NinjaAPI

api = NinjaAPI()
api.add_router("/rentoro/", "rentoro.api.router")
