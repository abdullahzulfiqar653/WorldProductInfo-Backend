from core.models import Category, Product
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import CategoryFilterNameSerializer
from django.db.models import Q


class CategoryFilterNameView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoryFilterNameSerializer

    def get_queryset(self):
        cat_queryset = Category.objects.filter(
            parentcategoryid=10041).select_related('categoryid')
        cat_ids = cat_queryset.values_list(
            'categoryid', flat=True)
        c_id = Product.objects.exclude(
            ~ Q(categoryid__in=cat_ids)).values_list('categoryid',
                                                     flat=True).prefetch_related('categoryid')
        queryset = Category.objects.filter(
            categoryid__in=c_id).select_related('categorylol')

        return queryset
