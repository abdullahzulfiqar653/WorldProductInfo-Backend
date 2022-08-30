from django.db import models
from viewflow.fields import CompositeKey


class Sysdiagrams(models.Model):
    id = CompositeKey(columns=['principal_id', 'diagram_id'])
    name = models.CharField(
        max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
