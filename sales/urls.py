from .views import SaleDetailsView, SalesView
from django.urls import path


urlpatterns = [
    path('sales/', SalesView.as_view()),
    path('sales/<str:sale_id>/', SaleDetailsView.as_view()),
]
