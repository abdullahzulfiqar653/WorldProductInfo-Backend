from django.db import models
from .unit_model import Units


class SearchAttributeValues(models.Model):
    valueid = models.IntegerField(primary_key=True)
    value = models.CharField(
        max_length=255)
    absolutevalue = models.FloatField()
    unitid = models.ForeignKey(
        Units, on_delete=models.CASCADE, db_column='unitid')
    isabsolute = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'search_attribute_values'
