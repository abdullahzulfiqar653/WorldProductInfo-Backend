from core.models import Locales
from django.contrib import admin


class LocalesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'localeid',
        'isactive',
        'countrycode',
        'languagecode',
    ]


admin.site.register(Locales, LocalesAdmin)
