from rest_framework import serializers
from .models import User
from sales.serializers import SaleSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ["id", "username", "password",
                  "email", "first_name", "last_name"]
        read_only_fields = ["id", "is_staff", "is_active"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    sales = SaleSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ["id", "username", "email",
                  "first_name", "last_name", "sales"]
        read_only_fields = ['id', "sales"]


class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_superuser'] = user.is_superuser

        return token
