from django.db import models
from viewflow.fields import CompositeKey
from .product_model import Product
from .locale_model import Locales


class Productlocales(models.Model):
    id = CompositeKey(columns=['productid', 'localeid'])
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid', related_name='productLocale')
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')
    isactive = models.BooleanField()
    status = models.CharField(
        max_length=60)

    class Meta:
        managed = False
        db_table = 'productlocales'
        unique_together = (('productid', 'localeid'),)
