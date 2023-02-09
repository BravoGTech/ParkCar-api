import ipdb
from datetime import datetime, timedelta
from django.db import models
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.
import uuid


class PaymentOptions(models.TextChoices):
    CC = "Cartão de Crédito"
    CD = "Cartão de Débito"
    PIX = "PIX"
    DC = "Dinheiro"


class Sale(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    sale_date = models.DateField(auto_now_add=True)
    start_hour = models.DateTimeField(auto_now_add=True)
    end_hour = models.DateTimeField(null=True)
    brand = models.CharField(max_length=50)
    payment_method = models.CharField(
        max_length=50,
        choices=PaymentOptions.choices,
        default=PaymentOptions.DC,
    )
    car_plate = models.CharField(max_length=7)
    price_by_hour = models.DecimalField(max_digits=10, decimal_places=2)

    # FK
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='sales')

    def final_price(self):
        if self.end_hour:
            duration = self.end_hour - self.start_hour
            duration_str = duration.total_seconds() / 3600 * -1
            return Decimal(duration_str).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP) * self.price_by_hour
        return None
