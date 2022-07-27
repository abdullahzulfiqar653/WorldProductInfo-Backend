from django.contrib import admin
from core.models import Productfeatures


class ProductfeaturesAdmin(admin.ModelAdmin):
    list_display = [
        'text',
        'localeid',
        'isactive',
        'productid',
        'ordernumber',
        'modifieddate',
        'productfeatureid',
    ]


admin.site.register(Productfeatures, ProductfeaturesAdmin)
