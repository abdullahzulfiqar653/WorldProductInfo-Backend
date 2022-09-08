from core.models import Product
from rest_framework import serializers
from gfksite.settings import ETILIZE_CONTENT
from .productsku_serializer import ProductSkusSerializer
from .productelement_serializer import ProductElementsSerializer
from .productdescription_serializer import ProductDescriptionsSerializer


class ProductListSerializer(serializers.ModelSerializer):

    """ Products Model serializer including child serializers of other models. 
    like product skus, product elements and product descriptions. these serializers
    providing related data of product"""

    # productSkus = ProductSkusSerializer(many=True)
    # productElements = ProductElementsSerializer(many=True)
    productDescription = ProductDescriptionsSerializer(
        many=True, read_only=True, source='type_description')
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        if ETILIZE_CONTENT:
            return "https://content.etilize.com/Main/{}.jpg?noimage=logo".format(obj.productid)
        else:
            return "media/2.jpg"

    class Meta:
        model = Product
        fields = [
            'productid',
            'image_url',
            'mfgpartno',
            # 'productSkus',
            # 'productElements',
            'productDescription',
        ]
