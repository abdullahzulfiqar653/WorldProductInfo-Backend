from django.db import models
from .product_model import Product
from viewflow.fields import CompositeKey
from .locale_model import Locales


class Productaccessories(models.Model):
    id = CompositeKey(columns=['productid', 'accessoryid'])
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid')
    accessoryproductid = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='accessory_product_id', db_column='accessoryproductid')
    isactive = models.BooleanField(default=True)
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')

    class Meta:
        managed = False
        db_table = 'productaccessories'
        unique_together = (('productid', 'accessoryproductid', 'localeid'),)
