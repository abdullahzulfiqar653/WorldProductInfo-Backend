from core.models import Productskus
from rest_framework import serializers


class ProductSkusSerializer(serializers.ModelSerializer):

    """ Productskus model serializer """

    class Meta:
        model = Productskus
        fields = [
            'name',
            'sku'
        ]
