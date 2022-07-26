from core.models.manufacturer_model import Manufacturer
from django.contrib import admin

class ManufacturerAdmin(admin.ModelAdmin):
    list_display= ['manufacturerid','name','url','logowidth','logoheight',]
admin.site.register(Manufacturer,ManufacturerAdmin)