from rest_framework import serializers
from core.models import Productelements
from core.serializers import ProductElementPropertiesSerializer


class ProductElementsSerializer(serializers.ModelSerializer):
    productElementProperties = ProductElementPropertiesSerializer(many=True)

    class Meta:
        model = Productelements
        fields = ['type', 'status', 'productElementProperties']
