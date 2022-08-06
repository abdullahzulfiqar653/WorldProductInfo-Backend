from rest_framework import serializers
from core.models import Category, Product


class CategoryFilterNameListSerializer(serializers.ModelSerializer):

    """ This serializer is using Category model and also 2 non-model fields
    category_product_count and category_label."""

    # category_label contain the categoryName from categoryName table.
    category_label = serializers.CharField(
        read_only=True, source='categorylol.name')
    # category_product_count contain product_count which manually added using annotate in view.
    category_product_count = serializers.IntegerField(
        read_only=True, source='product_count')

    class Meta:
        model = Category
        exclude = [
            'isactive',
            'catlevel',
            'parentcategoryid',
        ]
