from .views import CreateUserView, UserDetailView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('users/', CreateUserView.as_view()),
    path('users/<str:id>/', UserDetailView.as_view()),
    path('login/', TokenObtainPairView.as_view())
]
