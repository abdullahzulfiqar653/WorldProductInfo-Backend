from core.models.productdescrition_model import Productdescriptions
from django.contrib import admin

class ProductdescriptionsAdmin(admin.ModelAdmin):
    list_display= ['productid','description','isdefault','type','localeid','isactive',]
admin.site.register(Productdescriptions,ProductdescriptionsAdmin)