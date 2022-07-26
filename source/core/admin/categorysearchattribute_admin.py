from django.contrib import admin
from core.models import Categorysearchattributes


class CategorySearchAttributesAdmin(admin.ModelAdmin):
    list_display = [
        'isactive',
        'categoryid',
        'attributeid',
    ]


admin.site.register(Categorysearchattributes, CategorySearchAttributesAdmin)
