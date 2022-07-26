from core.models.productsku_model import Productskus
from django.contrib import admin

class ProductskusAdmin(admin.ModelAdmin):
    list_display= ['productid','name','sku','addeddate','isactive']
admin.site.register(Productskus,ProductskusAdmin)