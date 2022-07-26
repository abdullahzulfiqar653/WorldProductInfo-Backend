from core.models import Attributenames
from django.contrib import admin

class AttributenameAdmin(admin.ModelAdmin):
    list_display = ['attributeid','name','localeid',]

admin.site.register(Attributenames,AttributenameAdmin)
