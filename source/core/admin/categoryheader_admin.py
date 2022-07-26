from core.models.categoryheader_model import Categoryheader
from django.contrib import admin

class CategoryHeaderAdmin(admin.ModelAdmin):
    list_display= ['headerid','categoryid','isactive','templatetype','displayorder',]
admin.site.register(Categoryheader,CategoryHeaderAdmin)