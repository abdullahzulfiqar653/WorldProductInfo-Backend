from django.contrib import admin
from core.models import Categoryheader


class CategoryHeaderAdmin(admin.ModelAdmin):
    list_display = [
        'headerid',
        'isactive',
        'categoryid',
        'displayorder',
        'templatetype',
    ]


admin.site.register(Categoryheader, CategoryHeaderAdmin)
