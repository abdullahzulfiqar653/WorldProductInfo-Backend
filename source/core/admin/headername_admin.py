from django.contrib import admin
from core.models import Headernames


class HeadernamesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'headerid',
        'localeid',
    ]


admin.site.register(Headernames, HeadernamesAdmin)
