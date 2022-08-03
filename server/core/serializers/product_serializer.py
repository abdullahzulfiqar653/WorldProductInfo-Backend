from rest_framework import serializers
from core.models import Product
from core.serializers import (ManufacturerSerializer,
                              ProductDescriptionsSerializer,
                              ProductElementsSerializer,
                              ProductSkusSerializer,
                              ProductAttributeSerializer,
                              ProductFeaturesSerializer,
                              ProductLocalesSerializer,
                              CategorySerializer

                              )


class ProductSerializer(serializers.ModelSerializer):
    manufacturerid = ManufacturerSerializer(read_only=True)
    productDescription = ProductDescriptionsSerializer(
        many=True, read_only=True)
    productElements = ProductElementsSerializer(many=True)
    productAttribute = ProductAttributeSerializer(many=True)
    productFeatures = ProductFeaturesSerializer(many=True)
    productSkus = ProductSkusSerializer(many=True)
    productLocale = ProductLocalesSerializer(many=True)
    categoryid = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'categoryid',
            'manufacturerid',
            'mfgpartno',
            'isaccessory',
            'productDescription',
            'productElements',
            'productAttribute',
            'productFeatures',
            'productSkus',
            'productLocale',
        ]
