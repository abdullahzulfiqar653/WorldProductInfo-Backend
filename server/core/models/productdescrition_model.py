from django.db import models
from viewflow.fields import CompositeKey
from .product_model import Product
from .locale_model import Locales


class Productdescriptions(models.Model):
    id = CompositeKey(columns=['productid', 'localeid', 'type'])
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid', related_name='productDescription')
    description = models.CharField(
        max_length=1000)
    isdefault = models.BooleanField()
    type = models.IntegerField()
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productdescriptions'
        unique_together = (('productid', 'localeid', 'type'),)
