from email.mime import image
import imp
from pickle import TRUE
from re import T
from django.db import models
from .locale_model import Locales
from .unit_model import Units

class Unitnames(models.Model):
    unitid = models.ForeignKey(
        Units, on_delete=models.CASCADE, db_column='unitid')
    name = models.CharField(
        max_length=80)
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')

    class Meta:
        managed = False
        db_table = 'unitnames'
