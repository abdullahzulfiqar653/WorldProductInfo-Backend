from core.models import Units
from django.contrib import admin


class UnitsAdmin(admin.ModelAdmin):
    list_display = [
        'unitid',
        'multiple',
        'baseunitid',
    ]


admin.site.register(Units, UnitsAdmin)
