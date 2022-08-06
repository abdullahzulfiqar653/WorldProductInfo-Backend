from rest_framework import serializers
from core.models import Manufacturer, Product


class ManufacturerFilterNameSerializer(serializers.ModelSerializer):

    """ This serializer is using Manufacturer model and including
    when extra attribute which contain count of products. """

    manufacturer_product_count = serializers.SerializerMethodField()

    def get_manufacturer_product_count(self, obj: Manufacturer):
        return obj.product_count

    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'manufacturerid',
            'manufacturer_product_count',
        ]
