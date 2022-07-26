from core.models.unit_model import Units
from django.contrib import admin

class UnitsAdmin(admin.ModelAdmin):
    list_display= ['unitid','baseunitid','multiple',]
admin.site.register(Units,UnitsAdmin)