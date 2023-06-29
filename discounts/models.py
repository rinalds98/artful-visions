from django.db import models


class DiscountCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
