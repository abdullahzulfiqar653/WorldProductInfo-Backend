from core.models.productelementproperty_model import Productelementproperties
from django.contrib import admin

class ProductelementpropertiesAdmin(admin.ModelAdmin):
    list_display= ['productelementid','propertykey','propertyvalue','isactive',]
admin.site.register(Productelementproperties,ProductelementpropertiesAdmin)