from django.contrib import admin
from core.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'catlevel',
        'isactive',
        'categoryid',
        'ordernumber',
        'parentcategoryid',
    ]


admin.site.register(Category, CategoryAdmin)
