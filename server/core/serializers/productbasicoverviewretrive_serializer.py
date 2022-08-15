from core.models import Product
from rest_framework import serializers
from .productattribute_serializer import ProductAttributeSerializer


class ProductBasicOverViewSerializer(serializers.ModelSerializer):
    """ Products Model serializer including child serializers of other models. 
    like Product Attribute this serializer providing related data of product"""

    productAttribute = ProductAttributeSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'productid',
            'productAttribute'
        ]
