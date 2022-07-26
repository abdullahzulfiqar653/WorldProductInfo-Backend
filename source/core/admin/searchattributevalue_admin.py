from django.contrib import admin
from core.models import SearchAttributeValues


class SearchAttributeValuesAdmin(admin.ModelAdmin):
    list_display = [
        'value',
        'unitid',
        'valueid',
        'isabsolute',
        'absolutevalue',
    ]


admin.site.register(SearchAttributeValues, SearchAttributeValuesAdmin)
