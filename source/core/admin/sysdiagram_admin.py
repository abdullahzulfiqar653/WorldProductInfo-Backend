from core.models.sysdiagram_model import Sysdiagrams
from django.contrib import admin

class SysdiagramsAdmin(admin.ModelAdmin):
    list_display= ['name','principal_id','diagram_id','version','definition']
admin.site.register(Sysdiagrams,SysdiagramsAdmin)