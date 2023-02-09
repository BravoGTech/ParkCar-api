from rest_framework import serializers
from .models import User


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
