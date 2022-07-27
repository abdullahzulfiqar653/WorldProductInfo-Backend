from django.contrib import admin
from core.models import Unitnames


class UnitnamesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'unitid',
        'localeid',
    ]


admin.site.register(Unitnames, UnitnamesAdmin)
