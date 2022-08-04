from pickle import TRUE
from re import T
from django.db import models
from .product_model import Product
from .attributename_model import Attributenames
from .unit_model import Units
from .locale_model import Locales


class Productattribute(models.Model):
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid', related_name='productAttribute')
    attributeid = models.ForeignKey(
        Attributenames, on_delete=models.CASCADE, blank=True, db_column='attributeid', related_name='productAttributeName')
    setnumber = models.SmallIntegerField()
    # This field type is a guess.
    displayvalue = models.TextField(
        blank=True, null=True)
    absolutevalue = models.FloatField()
    unitid = models.ForeignKey(
        Units, on_delete=models.CASCADE, db_column='unitid')
    isabsolute = models.BooleanField()
    isactive = models.BooleanField()
    type = models.SmallIntegerField()
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')

    class Meta:
        managed = False
        db_table = 'productattribute'
        unique_together = (
            ('productid', 'localeid', 'attributeid', 'setnumber'),)
