from django.contrib import admin
from core.models import Productdescriptions


class ProductdescriptionsAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'localeid',
        'isactive',
        'productid',
        'isdefault',
        'description',
    ]


admin.site.register(Productdescriptions, ProductdescriptionsAdmin)
