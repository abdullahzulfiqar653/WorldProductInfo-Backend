from rest_framework import serializers
from core.models import Productattribute, SearchAttribute
from core.models import Attributenames


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributenames
        fields = ('attributeid', 'name')


class ProductAttributeSerializer(serializers.ModelSerializer):
    """ This serializer is used to get attributeid and productid from the search attribute table.
    attribute_name_label is used to get attribute name from the attributenames table. using related_name.
    value_label is used to get value from the search attribute values table. using related_name. """

    value = serializers.CharField(read_only=True, source='valueid.value')

    class Meta:
        model = SearchAttribute
        fields = [

            'attributeid',
            'value',
            'valueid',
        ]
