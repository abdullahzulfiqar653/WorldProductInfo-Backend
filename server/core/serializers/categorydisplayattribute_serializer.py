from rest_framework import serializers
from core.models import Categorydisplayattributes

class CategoryDisplayAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorydisplayattributes
        exclude = ['cat_id', 'isactive']

