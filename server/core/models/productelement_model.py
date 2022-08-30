from django.db import models
from .product_model import Product
from .locale_model import Locales


class Productelements(models.Model):
    productelementid = models.BigIntegerField(primary_key=True)
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid', related_name='productElements')
    type = models.CharField(
        max_length=60)
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')
    status = models.CharField(
        max_length=60)
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productelements'
        unique_together = (('productid', 'type', 'localeid'),)
