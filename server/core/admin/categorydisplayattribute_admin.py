from django.contrib import admin
from core.models import Categorydisplayattributes


class categorydisplayattributeAdmin(admin.ModelAdmin):
    list_display = [
        
        'isactive',
        'headerid',
        'categoryid',
        'attributeid',
        'displayorder',
        'templatetype',
    ]


admin.site.register(Categorydisplayattributes, categorydisplayattributeAdmin)
