from django.contrib import admin
from core.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'isactive',
        'productid',
        'mfgpartno',
        'categoryid',
        'isaccessory',
        'equivalency',
        'lastupdated',
        'creationdate',
        'modifieddate',
        'manufacturerid',
    ]


admin.site.register(Product, ProductAdmin)
