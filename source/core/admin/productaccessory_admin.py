from django.contrib import admin
from core.models import Productaccessories


class ProductaccessoriesAdmin(admin.ModelAdmin):
    list_display = [
        'localeid',
        'isactive',
        'productid',
        'accessoryproductid',
    ]


admin.site.register(Productaccessories, ProductaccessoriesAdmin)
