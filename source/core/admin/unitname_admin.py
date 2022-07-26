from core.models.unitname_model import Unitnames
from django.contrib import admin

class UnitnamesAdmin(admin.ModelAdmin):
    list_display= ['unitid','name','localeid',]
admin.site.register(Unitnames,UnitnamesAdmin)