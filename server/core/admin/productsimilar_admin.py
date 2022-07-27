from django.contrib import admin
from core.models import Productsimilar


class ProductsimilarAdmin(admin.ModelAdmin):
    list_display = [
        'isactive',
        'productid',
        'similarproductid',
    ]


admin.site.register(Productsimilar, ProductsimilarAdmin)
