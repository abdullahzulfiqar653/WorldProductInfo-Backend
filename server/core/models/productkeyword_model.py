from django.db import models
from viewflow.fields import CompositeKey
from .product_model import Product
from .locale_model import Locales


class Productkeywords(models.Model):
    id = CompositeKey(columns=['productid', 'keyword', 'localeid'])
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid')
    keywords = models.CharField(
        max_length=900)
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productkeywords'
        unique_together = (('productid', 'localeid'),)
