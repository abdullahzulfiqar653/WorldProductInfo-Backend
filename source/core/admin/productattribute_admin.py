from django.contrib import admin
from core.models import Productattribute


class ProductattributeAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'unitid',
        'localeid',
        'isactive',
        'setnumber',
        'productid',
        'isabsolute',
        'attributeid',
        'displayvalue',
        'absolutevalue',
    ]


admin.site.register(Productattribute, ProductattributeAdmin)
