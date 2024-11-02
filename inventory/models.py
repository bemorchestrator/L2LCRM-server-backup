# inventory/models.py

from django.db import models
from suppliers.models import Supplier  # Import Supplier from the suppliers app

class Product(models.Model):
    item_name = models.CharField(max_length=255, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    currency_code = models.CharField(max_length=3, null=True, blank=True)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    uom = models.CharField(max_length=10, null=True, blank=True)
    discountable_all = models.BooleanField(null=True, blank=True, default=False)
    discountable_members = models.BooleanField(null=True, blank=True, default=True)
    active = models.BooleanField(null=True, blank=True, default=False)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.item_name
