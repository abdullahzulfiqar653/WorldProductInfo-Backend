from core.models import Category, Product
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import CategoryFilterNameSerializer
from django.db.models import Q


class CategoryFilterNameView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoryFilterNameSerializer

    def get_queryset(self):
        parent_category_id = self.request.query_params.get(
                                                'parentcategoryid', None)
        category_queryset = Category.objects.filter(
            parentcategoryid=parent_category_id).select_related('categoryid')
        category_ids = category_queryset.values_list(
            'categoryid', flat=True)
        products_category_ids = Product.objects.exclude(~ Q(categoryid__in=category_ids)
                                                        ).values_list('categoryid', flat=True
                                                                      ).prefetch_related('categoryid')
        queryset = Category.objects.filter(
            categoryid__in=products_category_ids).select_related('categorylol')

        return queryset
