from rest_framework import serializers
from core.models import Productelementproperties


class ProductElementPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productelementproperties
        fields = ['propertykey', 'propertyvalue']
