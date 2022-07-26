from core.models.product_model import Product
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display= ['productid','manufacturerid','isactive','mfgpartno','categoryid','isaccessory','equivalency','creationdate','modifieddate','lastupdated']
admin.site.register(Product,ProductAdmin)