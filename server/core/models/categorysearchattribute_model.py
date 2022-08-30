from django.db import models
from viewflow.fields import CompositeKey
from .category_model import Category
from .attributename_model import Attributenames


class Categorysearchattributes(models.Model):
    id = CompositeKey(columns=['categoryid', 'attributeid'])
    categoryid = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='categoryid')
    attributeid = models.ForeignKey(
        Attributenames, on_delete=models.CASCADE, blank=True, db_column='attributeid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'categorysearchattributes'
        unique_together = ('categoryid', 'attributeid')
