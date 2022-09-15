from itertools import product
from core.models import Product
from rest_framework import serializers
from .category_serializer import CategorySerializer
from .productsepecificationattribute_serializer import ProductSpecificationAttributeSerializer


class ProductSpecificationSerializer(serializers.ModelSerializer):
    """ Products Model serializer including child serializers of other models. 
    like categoryserializer, productAttributeserializer. these serializers
    providing related data of product"""

    categoryid = CategorySerializer(read_only=True)
    productAttribute = ProductSpecificationAttributeSerializer(
        many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'categoryid',
            'productAttribute'
        ]
