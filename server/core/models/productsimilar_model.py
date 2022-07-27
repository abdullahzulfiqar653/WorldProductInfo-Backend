import imp
from pickle import TRUE
from re import T
from django.db import models
from .product_model import Product

class Productsimilar(models.Model):
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid')
    similarproductid = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='similar_product_id', db_column='similarproductid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productsimilar'
        unique_together = (('productid', 'similarproductid'),)
