from django.db import models


class Units(models.Model):
    unitid = models.IntegerField(primary_key=True)
    baseunitid = models.IntegerField()
    multiple = models.FloatField()

    class Meta:
        managed = False
        db_table = 'units'
