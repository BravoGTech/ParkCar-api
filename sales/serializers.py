from .models import PaymentOptions, Sale
from rest_framework import serializers
from users.serializers import UserSerializer


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale

        fields = ["id",
                  "payment_method",
                  "car_plate",
                  "user"]

        read_only_fields = ["id", "user", "end_hour",]

    user = UserSerializer(read_only=True)
