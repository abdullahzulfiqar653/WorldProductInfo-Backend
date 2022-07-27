from django.contrib import admin
from core.models import Productelements


class ProductelementsAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'status',
        'localeid',
        'isactive',
        'productid',
        'productelementid',
    ]


admin.site.register(Productelements, ProductelementsAdmin)
