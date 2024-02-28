from django.urls import include, path
from . import views
urlpatterns = [
    path("index", views.index),
    path("rentals", views.RentalView.as_view()),
    path("leasings", views.LeasingView.as_view())
]