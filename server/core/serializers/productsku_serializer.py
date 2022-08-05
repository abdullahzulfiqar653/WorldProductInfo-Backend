from core.models import Productskus
from rest_framework import serializers


class ProductSkusSerializer(serializers.ModelSerializer):

    """ This serializer is using Productskus model. """

    class Meta:
        model = Productskus
        fields = [
            'name',
            'sku'
        ]
