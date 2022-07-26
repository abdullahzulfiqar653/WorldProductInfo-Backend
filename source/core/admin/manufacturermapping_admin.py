from django.contrib import admin
from core.models import Manufacturermapping


class ManufacturermappingAdmin(admin.ModelAdmin):
    list_display = [
        'manufacturerid',
        'manufacturername',
    ]


admin.site.register(Manufacturermapping, ManufacturermappingAdmin)
