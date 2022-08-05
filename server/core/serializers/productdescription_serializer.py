from rest_framework import serializers
from core.models import Productdescriptions


class ProductDescriptionsSerializer(serializers.ModelSerializer):

    """ This serializer is using ProductDescription model. """

    class Meta:
        model = Productdescriptions
        fields = [
            'type',
            'description',
        ]
