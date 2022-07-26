from core.models.productelement_model import Productelements
from django.contrib import admin

class ProductelementsAdmin(admin.ModelAdmin):
    list_display= ['productelementid','productid','type','localeid','status','isactive',]
admin.site.register(Productelements,ProductelementsAdmin)