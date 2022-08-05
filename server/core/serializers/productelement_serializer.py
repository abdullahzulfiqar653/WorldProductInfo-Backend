from rest_framework import serializers
from core.models import Productelements


class ProductElementsSerializer(serializers.ModelSerializer):

    """ This serializer is using Productelements model and including
    when extra attribute which contain propertyKey and PropertyValue. """

    #propertyKey contain the propertyKey getting from ProductElementProperties table by using related name.
    property_key = serializers.CharField(
        read_only=True, source='productElementProperties.propertykey')
    #propertyValue contain the propertyValue getting from ProductElementProperties table by using related name.
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
