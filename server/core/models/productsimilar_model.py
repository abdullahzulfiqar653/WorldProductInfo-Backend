from django.db import models
from viewflow.fields import CompositeKey
from .product_model import Product

class Productsimilar(models.Model):
    id = CompositeKey(columns=['productid', 'similarproductid'])
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid')
    similarproductid = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='similar_product_id', db_column='similarproductid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productsimilar'
        unique_together = (('productid', 'similarproductid'),)
