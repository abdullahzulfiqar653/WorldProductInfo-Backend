from core.models import Category, Product
from rest_framework import serializers


class CategoryFilterNameListSerializer(serializers.ModelSerializer):
    category_label = serializers.CharField(
        read_only=True, source='categorylol.name')
    category_product_count = serializers.SerializerMethodField()

    def get_category_product_count(self, category: Category):
        return Product.objects.filter(categoryid=category.categoryid).count()

    class Meta:
        model = Category
        exclude = [
            'isactive',
            'catlevel',
            'parentcategoryid',
        ]
