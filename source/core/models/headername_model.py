import imp
from pickle import TRUE
from re import T
from django.db import models
from .locale_model import Locales

class Headernames(models.Model):
    headerid = models.IntegerField(primary_key=True)
    name = models.CharField(
        max_length=80)
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')

    class Meta:
        managed = False
        db_table = 'headernames'
