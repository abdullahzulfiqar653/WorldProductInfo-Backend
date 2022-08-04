from django.db.models import Q

from rest_framework import permissions
from rest_framework.generics import ListAPIView

from core.models import Category, Product
from core.serializers import CategoryFilterNameListSerializer


class CategoryFilterNameView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoryFilterNameListSerializer

    def get_queryset(self):
        parent_category_id = self.request.query_params.get(
            'parentcategoryid', None)
        category_ids = Category.objects.filter(
            parentcategoryid=parent_category_id).values('categoryid')

        products_category_ids = Product.objects.exclude(
            ~Q(categoryid__in=category_ids)).values('categoryid')

        queryset = Category.objects.filter(
            categoryid__in=products_category_ids).select_related('categorylol')

        return queryset
