from django.urls import include, path
from . import views
from rentoro.landlord import urls as landlord_urls
from rentoro.tenant import urls as tenant_urls
from rentoro.rentoro_auth import urls as rentoro_auth_urls
urlpatterns = [
    path("index", views.index),
    path("landlord/", include(landlord_urls)),
    path("tenant/", include(tenant_urls)),
    path("rentoro-auth/", include(rentoro_auth_urls))
]