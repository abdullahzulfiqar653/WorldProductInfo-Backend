from django.db import models
from viewflow.fields import CompositeKey
from .productelement_model import Productelements


class Productelementproperties(models.Model):
    id = CompositeKey(columns=['productelementid', 'propertyid'])
    productelementid = models.ForeignKey(
        Productelements, on_delete=models.CASCADE, db_column='productelementid', related_name='productElementProperties')
    propertykey = models.CharField(
        max_length=60)
    propertyvalue = models.CharField(
        max_length=250)
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productelementproperties'
        unique_together = (('productelementid', 'propertykey'),)
