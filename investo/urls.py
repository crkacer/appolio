from django.urls import include, path
from . import views
from .investor import urls as investor_urls
urlpatterns = [
    path("index", views.index),
    path("investor/", include(investor_urls))
]