from django.db import models

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
    payment_method = models.CharField(
        max_length=50,
        choices=PaymentOptions.choices,
        default=PaymentOptions.DC,
    )
    car_plate = models.CharField(max_length=7)

    # FK
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='sales')
