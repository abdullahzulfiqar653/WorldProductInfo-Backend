from rest_framework import serializers
from core.models import Productaccessories


class ProductAccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productaccessories
        fields = ['productid', ]
