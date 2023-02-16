from .views import CreateUserView, UserDetailView, MyTokenObtainPairView, UserProfileView
from django.urls import path


urlpatterns = [
    path('users/', CreateUserView.as_view()),
    path('users/dashboard/', UserProfileView.as_view()),
    path('users/<str:user_id>/', UserDetailView.as_view()),
    path('login/', MyTokenObtainPairView.as_view())
]
