from rest_framework import serializers
from core.models import Productlocales


class ProductLocalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productlocales
        fields = ['status', ]
