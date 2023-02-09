from .views import CreateUserView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('users/', CreateUserView.as_view()),
    path('login/', TokenObtainPairView.as_view())
]
