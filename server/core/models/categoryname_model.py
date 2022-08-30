from django.db import models
from .category_model import Category
from .locale_model import Locales


class Categorynames(models.Model):
    categoryid = models.OneToOneField(
        Category, on_delete=models.CASCADE, db_column='categoryid', primary_key=True, related_name='categorylol')
    name = models.CharField(
        max_length=80)
    localeid = models.ForeignKey(
        Locales, on_delete=models.CASCADE, blank=True, db_column='localeid')

    class Meta:
        managed = False
        db_table = 'categorynames'
