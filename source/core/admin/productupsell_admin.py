from core.models.productupsell_model import Productupsell
from django.contrib import admin

class ProductupsellAdmin(admin.ModelAdmin):
    list_display= ['productid','upsellproductid','isactive',]
admin.site.register(Productupsell,ProductupsellAdmin)