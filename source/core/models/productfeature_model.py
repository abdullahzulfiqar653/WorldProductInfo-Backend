import imp
from pickle import TRUE
from re import T
from django.db import models
from .locale_model import Locales
from .product_model import Product

class Productfeatures(models.Model):
    productfeatureid = models.DecimalField(
        primary_key=True, max_digits=24, decimal_places=0)
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid')
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')
    ordernumber = models.SmallIntegerField()
    text = models.CharField(
        max_length=1000)
    modifieddate = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productfeatures'
