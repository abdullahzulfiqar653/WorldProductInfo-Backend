from django.contrib import admin
from core.models import Manufacturer


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [
        'url',
        'name',
        'logowidth',
        'logoheight',
        'manufacturerid',
    ]


admin.site.register(Manufacturer, ManufacturerAdmin)
