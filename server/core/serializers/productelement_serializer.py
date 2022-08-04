from rest_framework import serializers
from core.models import Productelements


class ProductElementsSerializer(serializers.ModelSerializer):

    property_key = serializers.CharField(
        read_only=True, source='productElementProperties.propertykey')
    property_value = serializers.CharField(
        read_only=True, source='productElementProperties.propertyvalue')

    class Meta:
        model = Productelements
        fields = [
            'type',
            'status',
            'property_key',
            'property_value',
        ]
