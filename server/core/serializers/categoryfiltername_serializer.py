from rest_framework import serializers
from core.models import Category, Product


class CategoryFilterNameListSerializer(serializers.ModelSerializer):

    """ This serializer is using Category model and including
    when extra attribute which contain count of products and category name. """

    # category_label contain the categoryName getting from categoryName table by using related name.
    category_label = serializers.CharField(
        read_only=True, source='categorylol.name')
    category_product_count = serializers.SerializerMethodField()
    # Defination of the Method: get_category_product_count is used to count the products in each category.

    def get_category_product_count(self, category: Category):
        return category.product_count

    class Meta:
        model = Category
        exclude = [
            'isactive',
            'catlevel',
            'parentcategoryid',
        ]
