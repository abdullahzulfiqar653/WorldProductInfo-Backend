from core.models.manufacturermapping_model import Manufacturermapping
from django.contrib import admin

class ManufacturermappingAdmin(admin.ModelAdmin):
    list_display= ['manufacturername','manufacturerid',]
admin.site.register(Manufacturermapping,ManufacturermappingAdmin)