from core.models.categorydisplayattribute_models import Categorydisplayattributes
from django.contrib import admin

class categorydisplayattributeAdmin(admin.ModelAdmin):
    list_display= ['cat_id','headerid','categoryid','attributeid','isactive','templatetype','displayorder',]
admin.site.register(Categorydisplayattributes,categorydisplayattributeAdmin)