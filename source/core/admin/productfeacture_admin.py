from core.models.productfeature_model import Productfeatures
from django.contrib import admin

class ProductfeaturesAdmin(admin.ModelAdmin):
    list_display= ['productfeatureid','productid','localeid','ordernumber','text','modifieddate','isactive',]
admin.site.register(Productfeatures,ProductfeaturesAdmin)