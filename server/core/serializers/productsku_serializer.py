from rest_framework import serializers
from core.models import Productskus


class ProductSkusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productskus
        fields = ['name', 'sku']
