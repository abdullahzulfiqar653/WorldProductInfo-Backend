from multiprocessing.spawn import import_main_path
from pickle import TRUE
from re import T
from django.db import models
from .product_model import Product
from .locale_model import Locales

class Productkeywords(models.Model):
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
