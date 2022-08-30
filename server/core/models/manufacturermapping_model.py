from django.db import models
from viewflow.fields import CompositeKey
from .manufacturer_model import Manufacturer


class Manufacturermapping(models.Model):
    # Field name made lowercase.
    id = CompositeKey(columns=['manufacturerid', 'manufacturername'])
    manufacturername = models.CharField(
        max_length=70)
    manufacturerid = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='mfg_mapping', db_column='manufacturerid')

    class Meta:
        managed = False
        db_table = 'manufacturermapping'
