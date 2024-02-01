from django.urls import include, path
from . import views
from .investor import urls as investor_urls
from .manager import urls as manager_urls
from .auth import urls as auth_urls
urlpatterns = [
    path("index", views.index),
    path("auth/", include(auth_urls)),
    path("investor/", include(investor_urls)),
    path("manager/", include(manager_urls)),

]