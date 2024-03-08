from django.urls import include, path
from . import views

urlpatterns = [
    path("transaction-types", views.TransactionTypeView.as_view()),
    path("transactions", views.TransactionView.as_view()),
    path("transactions/:id", views.get_transaction_detail),
    path("transactions/units/:id", views.get_all_unit_transactions),
    path("units", views.UnitView.as_view())
]