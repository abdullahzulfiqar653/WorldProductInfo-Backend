from rest_framework import serializers
from core.models import Productelements


class ProductElementsSerializer(serializers.ModelSerializer):

    """ Productelements model serializer include 2 extra attribute
    propertyKey and PropertyValue. """

    # propertyKey from ProductElementProperties table.
    property_key = serializers.CharField(
        read_only=True, source='productElementProperties.propertykey')
    # propertyValue from ProductElementProperties table.
    property_value = serializers.CharField(
        read_only=True, source='productElementProperties.propertyvalue')

    class Meta:
        model = Productelements
        fields = [
            'productelementid',
            'type',
            'status',
            'property_key',
            'property_value',
        ]
