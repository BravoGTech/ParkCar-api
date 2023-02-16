from rest_framework import generics
from .models import User
from .serializers import UserDetailSerializer, UserSerializer, CustomTokenSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import isAdmin, isAdminOrOwner
# Create your views here.


class CreateUserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminOrOwner]

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    lookup_url_kwarg = "user_id"

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer
