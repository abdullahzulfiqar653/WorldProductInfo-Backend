from django.contrib import admin
from core.models import Categorynames


class CategorynameAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'localeid',
        'categoryid',
    ]


admin.site.register(Categorynames, CategorynameAdmin)
