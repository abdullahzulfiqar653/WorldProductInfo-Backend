from rest_framework import serializers
from core.models import *
from core.serializers import AttributeNameSerializer


class ProductAttributeSerializer(serializers.ModelSerializer):
    attributeid = AttributeNameSerializer(read_only=True)

    class Meta:
        model = Productattribute
        fields = ['attributeid',
                  'displayvalue', 'type', 'isabsolute', 'setnumber']
