from . import views
from django.urls import path, include
urlpatterns = [
    path("accounts/:id", views.AccountDetailView.as_view()),
    path("accounts", views.AccountView.as_view()),
]