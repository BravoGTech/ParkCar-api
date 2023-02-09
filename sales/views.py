from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, isAdminOrOwner
from .models import Sale
from .serializers import SaleDetailsSerializer, SaleSerializer
# Create your views here.


class SalesView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SaleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminOrOwner]

    queryset = Sale.objects.all()
    serializer_class = SaleDetailsSerializer

    lookup_url_kwarg = 'sale_id'
