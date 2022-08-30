from django.db import models
from viewflow.fields import CompositeKey
from .product_model import Product


class Productupsell(models.Model):
    id = CompositeKey(columns=['productid', 'upsellproductid'])
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='productid')
    upsellproductid = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='upsell_product_id', db_column='upsellproductid')
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productupsell'
        unique_together = (('productid', 'upsellproductid'),)
