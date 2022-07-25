import imp
from pickle import TRUE
from re import T
from django.db import models
from .product_model import Product

class Productupsell(models.Model):
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid')
    upsellproductid = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='upsell_product_id', db_column='upsellproductid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productupsell'
        unique_together = (('productid', 'upsellproductid'),)
