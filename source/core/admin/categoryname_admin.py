from core.models.categoryname_model import Categorynames
from django.contrib import admin

class CategorynameAdmin(admin.ModelAdmin):
    list_display= ['categoryid','name','localeid']
admin.site.register(Categorynames,CategorynameAdmin)