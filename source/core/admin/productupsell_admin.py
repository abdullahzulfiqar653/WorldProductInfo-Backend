from django.contrib import admin
from core.models import Productupsell


class ProductupsellAdmin(admin.ModelAdmin):
    list_display = [
        'isactive',
        'productid',
        'upsellproductid',
    ]


admin.site.register(Productupsell, ProductupsellAdmin)
