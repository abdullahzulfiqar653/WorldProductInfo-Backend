from pickle import TRUE
from re import T
from django.db import models


class Category(models.Model):
    categoryid = models.IntegerField(primary_key=True)
    parentcategoryid = models.ForeignKey(
        'self', on_delete=models.CASCADE, db_column='parentcategoryid', null=True, blank=True)
    isactive = models.BooleanField()
    ordernumber = models.IntegerField()
    catlevel = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'category'
