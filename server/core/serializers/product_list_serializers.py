from rest_framework import serializers
from core.models import *
from core.serializers.product_serializers import *


class ProductListSerializer(serializers.ModelSerializer):
    productElements = ProductElementsSerializer(many=True)
    productSkus = ProductSkusSerializer(many=True)
    productDescription = ProductDescriptionsSerializer(
        many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['productid', 'mfgpartno', 'productSkus',
                  'productDescription', 'productElements', ]
