from core.models.category_model import Category
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['categoryid','parentcategoryid','isactive','ordernumber','catlevel',]
admin.site.register(Category,CategoryAdmin)
