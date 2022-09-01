from core.models import Product
from rest_framework import serializers
from gfksite.settings import etilze_content
from .productsku_serializer import ProductSkusSerializer
from .productelement_serializer import ProductElementsSerializer
from .productdescription_serializer import ProductDescriptionsSerializer


class ProductListSerializer(serializers.ModelSerializer):

    """ Products Model serializer including child serializers of other models. 
    like product skus, product elements and product descriptions. these serializers
    providing related data of product"""

    productSkus = ProductSkusSerializer(many=True)
    productElements = ProductElementsSerializer(many=True)
    productDescription = ProductDescriptionsSerializer(
        many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        etilze_content = False
        if etilze_content:
            return "https://content.etilize.com/Main/{}.jpg?noimage=logo".format(obj.productid)
        else:
            return "http://127.0.0.1:8000/media/2.jpg"

    class Meta:
        model = Product
        fields = [
            'productid',
            'image_url',
            'mfgpartno',
            'productSkus',
            'productElements',
            'productDescription',
        ]
