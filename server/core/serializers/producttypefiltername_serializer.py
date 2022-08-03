from rest_framework import serializers
from core.models import SearchAttributeValues


class SearchAttributeValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchAttributeValues
        fields = ['valueid', 'value', ]
