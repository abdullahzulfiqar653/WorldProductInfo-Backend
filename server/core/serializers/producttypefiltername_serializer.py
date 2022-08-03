from rest_framework import serializers
from core.models import SearchAttributeValues, SearchAttribute


class SearchAttributeValuesListSerializer(serializers.ModelSerializer):
    category_product_count = serializers.SerializerMethodField()

    def get_category_product_count(self, obj: SearchAttributeValues):
        return SearchAttribute.objects.filter(valueid=obj.valueid, attributeid=1100).count()

    class Meta:
        model = SearchAttributeValues
        fields = [
            'value',
            'valueid',
            'category_product_count',
        ]
