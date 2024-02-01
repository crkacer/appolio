from django.urls import path
from investo.auth import views

urlpatterns = [
    path('login', views.login),
    path('test-token', views.test_token)
]