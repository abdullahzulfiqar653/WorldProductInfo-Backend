from pickle import TRUE
from re import T
from django.db import models
from .headername_model import Headernames
from .category_model import Category


class Categoryheader(models.Model):
    headerid = models.ForeignKey(
        Headernames, on_delete=models.CASCADE, db_column='headerid')
    categoryid = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='categoryid', related_name='categoryHeader')
    isactive = models.BooleanField()
    templatetype = models.IntegerField()
    displayorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categoryheader'
