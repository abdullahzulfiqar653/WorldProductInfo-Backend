from core.models import Attributenames
from django.contrib import admin


class AttributenameAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'localeid',
        'attributeid',
    ]


admin.site.register(Attributenames, AttributenameAdmin)
