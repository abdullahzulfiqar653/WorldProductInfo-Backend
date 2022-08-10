from core.models import Product
from rest_framework import serializers
from .productsku_serializer import ProductSkusSerializer
from .productelement_serializer import ProductElementsSerializer
from .productfeature_serializer import ProductFeaturesSerializer
from .productdescription_serializer import ProductDescriptionsSerializer


class ProductRetrieveSerializer(serializers.ModelSerializer):

    """ Products Model serializer including child serializers of other models. 
    like product skus, product elements, productfeatures and product descriptions. these serializers
    providing related data of product"""

    productSkus = ProductSkusSerializer(many=True)
    productElements = ProductElementsSerializer(many=True)
    productFeatures = ProductFeaturesSerializer(many=True)
    productDescription = ProductDescriptionsSerializer(
        many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'productid',
            'mfgpartno',
            'isaccessory',
            'productSkus',
            'manufacturerid',
            'productFeatures',
            'productElements',
            'productDescription',
        ]
