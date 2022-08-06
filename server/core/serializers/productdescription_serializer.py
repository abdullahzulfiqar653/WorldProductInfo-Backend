from rest_framework import serializers
from core.models import Productdescriptions


class ProductDescriptionsSerializer(serializers.ModelSerializer):

    """ ProductDescription model serializer. """

    class Meta:
        model = Productdescriptions
        fields = [
            'type',
            'description',
        ]
