from core.models.productattribute_model import Productattribute
from django.contrib import admin

class ProductattributeAdmin(admin.ModelAdmin):
    list_display= ['productid','attributeid','setnumber','displayvalue','absolutevalue','unitid','isabsolute','isactive','type','localeid',]
admin.site.register(Productattribute,ProductattributeAdmin)