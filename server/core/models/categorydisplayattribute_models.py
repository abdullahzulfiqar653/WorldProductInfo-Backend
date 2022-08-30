from django.db import models
from .category_model import Category
from viewflow.fields import CompositeKey
from .headername_model import Headernames
from .attributename_model import Attributenames


class Categorydisplayattributes(models.Model):
    id = CompositeKey(columns=['headerid', 'categoryid', 'attributeid'])
    headerid = models.ForeignKey(
        Headernames, on_delete=models.CASCADE, db_column='headerid')
    categoryid = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='categoryid', related_name='categoryDisplayAttributeValue')
    attributeid = models.ForeignKey(
        Attributenames, on_delete=models.CASCADE, blank=True, db_column='attributeid')
    isactive = models.BooleanField()
    templatetype = models.IntegerField()
    displayorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categorydisplayattributes'
        unique_together = ('headerid', 'categoryid', 'attributeid')
