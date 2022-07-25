from pickle import TRUE
from re import T
from django.db import models

class Manufacturer(models.Model):
    manufacturerid = models.IntegerField(primary_key=True)
    name = models.CharField(
        max_length=60)
    url = models.CharField(
        max_length=100, blank=True, null=True)
    logowidth = models.IntegerField()
    logoheight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manufacturer'
