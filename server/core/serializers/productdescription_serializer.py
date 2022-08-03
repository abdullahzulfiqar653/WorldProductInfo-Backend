from rest_framework import serializers
from core.models import Productdescriptions


class ProductDescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productdescriptions
        fields = ['type',  'description', ]
