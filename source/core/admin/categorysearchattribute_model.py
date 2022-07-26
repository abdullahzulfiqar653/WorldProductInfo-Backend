from core.models.categorysearchattribute_model import Categorysearchattributes
from django.contrib import admin

class CategorySearchAttributesAdmin(admin.ModelAdmin):
    list_display= ['categoryid','attributeid','isactive',]
admin.site.register(Categorysearchattributes,CategorySearchAttributesAdmin)