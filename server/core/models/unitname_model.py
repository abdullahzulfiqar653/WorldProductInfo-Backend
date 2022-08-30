from django.db import models
from .locale_model import Locales
from viewflow.fields import CompositeKey
from .unit_model import Units


class Unitnames(models.Model):
    id = CompositeKey(columns=['unitid', 'localeid'])
    unitid = models.ForeignKey(
        Units, on_delete=models.CASCADE, db_column='unitid')
    name = models.CharField(
        max_length=80)
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')

    class Meta:
        managed = False
        db_table = 'unitnames'
