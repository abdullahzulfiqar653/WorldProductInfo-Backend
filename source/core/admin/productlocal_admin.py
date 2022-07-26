from django.contrib import admin
from core.models import Productlocales


class ProductlocalesAdmin(admin.ModelAdmin):
    list_display = [
        'status',
        'isactive',
        'localeid',
        'productid',
    ]


admin.site.register(Productlocales, ProductlocalesAdmin)
