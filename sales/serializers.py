
from .models import PaymentOptions, Sale
from rest_framework import serializers


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale

        fields = ["id",
                  "payment_method",
                  "car_plate",
                  "sale_date",
                  "start_hour",
                  "end_hour",
                  "price_by_hour",
                  "price",
                  "user"
                  ]

        read_only_fields = ["id", "end_hour", "sale_date",
                            "start_hour",
                            "end_hour",
                            "price",
                            "user"
                            ]

    price = serializers.SerializerMethodField(read_only=True)

    def get_price(self, sales: Sale):
        return sales.final_price()


class SaleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"

    price = serializers.SerializerMethodField(read_only=True)

    def get_price(self, sales: Sale):
        return sales.final_price()
