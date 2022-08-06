from rest_framework import serializers
from core.models import SearchAttributeValues, SearchAttribute


class SearchAttributeValuesListSerializer(serializers.ModelSerializer):

    """ This serializer is using SearchAttributeValues model and including
    when extra attribute which contain count of products. """

    category_product_count = serializers.SerializerMethodField()

    def get_category_product_count(self, obj: SearchAttributeValues):
        return obj.product_count

    class Meta:
        model = SearchAttributeValues
        fields = [
            'value',
            'valueid',
            'category_product_count',
        ]
