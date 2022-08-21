from .categoryheader_serializer import CategoryHeaderSerializer
from rest_framework import serializers
from core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Category Model serializer including child serializers of other models."""
    categoryHeader = CategoryHeaderSerializer(many=True)
    
    class Meta:
        model = Category
        fields = ['categoryHeader']
