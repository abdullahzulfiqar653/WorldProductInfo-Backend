from pickle import TRUE
from re import T
from django.db import models
from .manufacturer_model import Manufacturer

class Manufacturermapping(models.Model):
    # Field name made lowercase.
    manufacturername = models.CharField(
        max_length=70)
    manufacturerid = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='mfg_mapping', db_column='manufacturerid')

    class Meta:
        managed = False
        db_table = 'manufacturermapping'
