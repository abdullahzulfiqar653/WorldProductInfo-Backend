from core.models.searchattribute_model import SearchAttribute
from django.contrib import admin

class SearchAttributeAdmin(admin.ModelAdmin):
    list_display= ['productid','attributeid','valueid','localeid','setnumber','isactive',]
admin.site.register(SearchAttribute,SearchAttributeAdmin)