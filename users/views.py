from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import isAdmin
# Create your views here.


class CreateUserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer
