from core.models.searchattributevalue_model import SearchAttributeValues
from django.contrib import admin

class SearchAttributeValuesAdmin(admin.ModelAdmin):
    list_display= ['valueid','value','absolutevalue','unitid','isabsolute',]
admin.site.register(SearchAttributeValues,SearchAttributeValuesAdmin)