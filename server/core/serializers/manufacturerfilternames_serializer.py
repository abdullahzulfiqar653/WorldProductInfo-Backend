from rest_framework import serializers
from core.models import Manufacturer, Product


class ManufacturerFilterNameSerializer(serializers.ModelSerializer):
    manufacturer_product_count = serializers.SerializerMethodField()

    def get_manufacturer_product_count(self, obj: Manufacturer):
        category_id = self.context['categoryid']
        return Product.objects.filter(
            manufacturerid=obj.manufacturerid, categoryid=category_id).select_related('manufacturerid').count()

    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'manufacturerid',
            'manufacturer_product_count',
        ]
