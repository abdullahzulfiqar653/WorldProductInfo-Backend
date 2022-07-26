from core.models.productsimilar_model import Productsimilar
from django.contrib import admin

class ProductsimilarAdmin(admin.ModelAdmin):
    list_display= ['productid','similarproductid','isactive',]
admin.site.register(Productsimilar,ProductsimilarAdmin)