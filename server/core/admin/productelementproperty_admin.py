from django.contrib import admin
from core.models import Productelementproperties


class ProductelementpropertiesAdmin(admin.ModelAdmin):
    list_display = [
        'isactive',
        'propertykey',
        'propertyvalue',
        'productelementid',
    ]


admin.site.register(Productelementproperties, ProductelementpropertiesAdmin)
