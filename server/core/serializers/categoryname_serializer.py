from rest_framework import serializers
from core.models import Categorynames


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorynames
        fields = ['name', ]
