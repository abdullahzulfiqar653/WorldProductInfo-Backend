from core.models.productlocal_model import Productlocales
from django.contrib import admin

class ProductlocalesAdmin(admin.ModelAdmin):
    list_display= ['productid','localeid','isactive','status',]
admin.site.register(Productlocales,ProductlocalesAdmin)