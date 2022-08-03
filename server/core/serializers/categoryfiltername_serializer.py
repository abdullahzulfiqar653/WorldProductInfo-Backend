from core.models import Category
from rest_framework import serializers


class CategoryFilterNameSerializer(serializers.ModelSerializer):
    category_label = serializers.CharField(
        read_only=True, source='categorylol.name')

    class Meta:
        model = Category
        fields = [
            'categoryid',
            'ordernumber',
            'category_label',
        ]
