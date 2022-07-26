from core.models.headername_model import Headernames
from django.contrib import admin

class HeadernamesAdmin(admin.ModelAdmin):
    list_display= ['headerid','name','localeid',]
admin.site.register(Headernames,HeadernamesAdmin)