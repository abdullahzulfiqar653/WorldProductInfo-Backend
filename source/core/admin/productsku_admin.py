from django.contrib import admin
from core.models import Productskus


class ProductskusAdmin(admin.ModelAdmin):
    list_display = [
        'sku',
        'name',
        'isactive',
        'addeddate',
        'productid',
    ]


admin.site.register(Productskus, ProductskusAdmin)
