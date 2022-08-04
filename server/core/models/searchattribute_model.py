from pickle import TRUE
from re import T
from django.db import models
from .product_model import Product
from .attributename_model import Attributenames
from .searchattributevalue_model import SearchAttributeValues
from .locale_model import Locales

class SearchAttribute(models.Model):
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid')
    attributeid = models.ForeignKey(
        Attributenames, on_delete=models.CASCADE, db_column='attributeid',related_name='searchAttributeName')
    valueid = models.ForeignKey(
        SearchAttributeValues, on_delete=models.CASCADE, db_column='valueid')
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')
    setnumber = models.SmallIntegerField()
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'search_attribute'
        unique_together = (
            ('productid', 'localeid', 'attributeid', 'setnumber'),)
