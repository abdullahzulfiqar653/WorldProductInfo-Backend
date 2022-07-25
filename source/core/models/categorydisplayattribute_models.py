from pickle import TRUE
from re import T
from django.db import models
from .headername_model import Headernames
from .category_model import Category
from .attributename_model import Attributenames

class Categorydisplayattributes(models.Model):
    cat_id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    headerid = models.ForeignKey(
        Headernames, on_delete=models.CASCADE, db_column='headerid')
    categoryid = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='categoryid')
    attributeid = models.ForeignKey(
        Attributenames, on_delete=models.CASCADE, blank=True, db_column='attributeid')
    isactive = models.BooleanField()
    templatetype = models.IntegerField()
    displayorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categorydisplayattributes'
