from rest_framework import serializers
from core.models import Productattribute, SearchAttribute


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute_name_label = serializers.CharField(
        read_only=True, source='attributeid.name')
    value = serializers.CharField(read_only=True, source='valueid.value')
    # attribute = serializers.SerializerMethodField()

    # def get_attribute(self, obj: SearchAttribute):
    #     return SearchAttribute.objects.filter(attributeid=obj.attributeid).prefetch_related('attributeid').values('attributeid').distinct().count()

    class Meta:
        model = SearchAttribute
        fields = [
            'productid',
            'attributeid',
            'value',
            # 'attribute',
            'attribute_name_label'
        ]
