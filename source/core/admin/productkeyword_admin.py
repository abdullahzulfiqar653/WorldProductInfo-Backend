from django.contrib import admin
from core.models import Productkeywords


class ProductkeywordsAdmin(admin.ModelAdmin):
    list_display = [
        'keywords',
        'localeid',
        'isactive',
        'productid',
    ]


admin.site.register(Productkeywords, ProductkeywordsAdmin)
