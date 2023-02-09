from .views import SalesView
from django.urls import path


urlpatterns = [
    path('sales/', SalesView.as_view()),
]
