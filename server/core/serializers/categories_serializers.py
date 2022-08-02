from rest_framework import serializers
from core.models import *
from core.serializers.product_serializers import *


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorynames
        fields = ['name', ]


class CategoryListSerializer(serializers.ModelSerializer):
    categorylol = CategoryNameSerializer()

    class Meta:
        model = Category
        fields = ['categoryid', 'parentcategoryid', 'categorylol', ]
