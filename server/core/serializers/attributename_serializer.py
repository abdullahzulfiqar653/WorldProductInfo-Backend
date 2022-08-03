from rest_framework import serializers
from core.models import Attributenames


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributenames
        fields = ['name', ]