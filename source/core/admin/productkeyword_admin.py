from core.models.productkeyword_model import Productkeywords
from django.contrib import admin

class ProductkeywordsAdmin(admin.ModelAdmin):
    list_display= ['productid','keywords','localeid','isactive',]
admin.site.register(Productkeywords,ProductkeywordsAdmin)