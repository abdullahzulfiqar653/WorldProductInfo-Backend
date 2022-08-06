from core.models import Category
from rest_framework import serializers


class CategoryListSerializer(serializers.ModelSerializer):

    """ This serializer is using Category model and including
    when extra attribute which contain category name. """
    
    #category_label contain the categoryName getting from categoryName table by using related name.
    category_label = serializers.CharField(
        read_only=True, source='categorylol.name')

    class Meta:
        model = Category
        fields = [
            'catlevel',
            'categoryid',
            'ordernumber',
            'category_label',
            'parentcategoryid'
        ]
