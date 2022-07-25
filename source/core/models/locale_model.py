from pickle import TRUE
from re import T
from django.db import models


class Locales(models.Model):
    localeid = models.IntegerField(primary_key=True)
    isactive = models.BooleanField()
    languagecode = models.CharField(
        max_length=5)
    countrycode = models.CharField(
        max_length=5)
    name = models.CharField(
        max_length=80)

    class Meta:
        managed = False
        db_table = 'locales'
