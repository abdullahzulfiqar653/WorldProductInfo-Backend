from core.models.locale_model import Locales
from django.contrib import admin

class LocalesAdmin(admin.ModelAdmin):
    list_display= ['localeid','isactive','languagecode','countrycode','name',]
admin.site.register(Locales,LocalesAdmin)