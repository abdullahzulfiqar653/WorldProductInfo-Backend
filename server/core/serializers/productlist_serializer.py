from core.models import Product
from rest_framework import serializers
from .productsku_serializer import ProductSkusSerializer
from .productelement_serializer import ProductElementsSerializer
from .productdescription_serializer import ProductDescriptionsSerializer


class ProductListSerializer(serializers.ModelSerializer):

    """ This serializer is using products Model and including when extra serializer from other models. 
    and also include product skus, product elements and product descriptions. Nested serializers are used.
    for containing product skus, product elements and product descriptions Models data. """

    productSkus = ProductSkusSerializer(many=True)
    productElements = ProductElementsSerializer(many=True)
    productDescription = ProductDescriptionsSerializer(
        many=True, read_only=True)

    class Meta:
        model = Product
        fields = [

            'productid',
            'mfgpartno',
            'categoryid',
            'productSkus',
            'productElements',
            'productDescription',
        ]
