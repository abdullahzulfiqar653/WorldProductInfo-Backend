from django.contrib import admin
from core.models import Sysdiagrams


class SysdiagramsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'version',
        'definition',
        'diagram_id',
        'principal_id',
    ]


admin.site.register(Sysdiagrams, SysdiagramsAdmin)
