from django.contrib import admin
from core.models import SearchAttribute


class SearchAttributeAdmin(admin.ModelAdmin):
    list_display = [
        'valueid',
        'localeid',
        'isactive',
        'setnumber',
        'productid',
        'attributeid',
    ]


admin.site.register(SearchAttribute, SearchAttributeAdmin)
