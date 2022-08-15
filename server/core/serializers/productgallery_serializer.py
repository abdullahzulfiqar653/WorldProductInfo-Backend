from core.models import Product
from rest_framework import serializers
from .productelement_serializer import ProductElementsSerializer


class ProductGallerySerializer(serializers.ModelSerializer):
    """ Products Model serializer including child serializers of other models. 
    like  product elements, product element property . these serializers
    providing related data of product"""
    productElements = ProductElementsSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'productid',
            'productElements'
        ]
