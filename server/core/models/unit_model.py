from pickle import TRUE
from re import T
from django.db import models

class Units(models.Model):
    unitid = models.IntegerField(primary_key=True)
    baseunitid = models.IntegerField()
    multiple = models.FloatField()

    class Meta:
        managed = False
        db_table = 'units'
