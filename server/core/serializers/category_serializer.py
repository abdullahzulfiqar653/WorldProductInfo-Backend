from rest_framework import serializers
from core.models import Category
from core.serializers import CategoryDisplayAttributesSerializer
from core.serializers import CategoryHeaderSerializer


class CategorySerializer(serializers.ModelSerializer):
    categoryDisplayAttributeValue = CategoryDisplayAttributesSerializer(
        many=True)
    categoryHeader = CategoryHeaderSerializer(many=True)

    class Meta:
        model = Category
        fields = ['categoryHeader', 'categoryDisplayAttributeValue']
