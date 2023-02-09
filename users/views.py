from rest_framework import generics
from .models import User
from .serializers import UserDetailSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import isAdmin
# Create your views here.


class CreateUserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    lookup_field = 'id'
