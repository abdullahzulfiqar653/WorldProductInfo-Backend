from rest_framework import serializers
from core.models import Productattribute, SearchAttribute


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute_name_label = serializers.CharField(
        read_only=True, source='attributeid.name')
    display_value = serializers.CharField(
        read_only=True, source='attributeid__productAttributeName__displayvalue')

    class Meta:
        model = SearchAttribute
        fields = [
            'attributeid',
            'display_value',
            'attribute_name_label'
        ]
