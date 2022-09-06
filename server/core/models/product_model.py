from django.db import models
from .manufacturer_model import Manufacturer
from .category_model import Category


class Product(models.Model):
    productid = models.IntegerField(primary_key=True)
    manufacturerid = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, db_column='manufacturerid', related_name='manufacturerproduct')
    isactive = models.BooleanField()
    mfgpartno = models.CharField(
        max_length=70)
    categoryid = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column='categoryid', related_name='categoryproduct')
    isaccessory = models.BooleanField(default=False)
    equivalency = models.FloatField()
    creationdate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now_add=True)

    @property
    def get_description(self):
        try:
            return self.productDescription.filter(type=2).first().description
        except Exception as e:
            return self.productDescription.all().first().description

    class Meta:
        managed = False
        db_table = 'product'
