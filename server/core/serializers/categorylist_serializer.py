from core.models import Category
from rest_framework import serializers


class CategoryListSerializer(serializers.ModelSerializer):
    category_label = serializers.CharField(
        read_only=True, source='categorylol.name')

    class Meta:
        model = Category
        fields = [
            'catlevel',
            'categoryid',
            'ordernumber',
            'category_label',
            'parentcategoryid',
        ]
