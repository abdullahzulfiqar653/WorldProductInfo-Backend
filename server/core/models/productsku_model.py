import imp
from pickle import TRUE
from re import T
from django.db import models
from .product_model import Product


class Productskus(models.Model):
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid', related_name='productSkus')
    name = models.CharField(
        max_length=60)
    sku = models.CharField(
        max_length=60)
    addeddate = models.DateTimeField(blank=True, null=True)
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productskus'
        unique_together = (('productid', 'name', 'sku'),)
