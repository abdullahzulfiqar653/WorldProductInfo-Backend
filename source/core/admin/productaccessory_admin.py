from core.models.productaccessory_model import Productaccessories
from django.contrib import admin

class ProductaccessoriesAdmin(admin.ModelAdmin):
    list_display= ['productid','accessoryproductid','isactive','localeid',]
admin.site.register(Productaccessories,ProductaccessoriesAdmin)