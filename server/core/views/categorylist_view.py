from core.models import Category
from django.db.models import Count
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import CategoryListSerializer


# class CategoryListView(ListAPIView):

#     """This ListView for getting Category names, displayorder,
#     category_level and parentcategoryid.
#     """

#     serializer_class = CategoryListSerializer
#     permission_classes = [permissions.AllowAny]
#     # using select_related to pre load categoryname table data
#     queryset = Category.objects.exclude(
#         parentcategoryid__isnull=True).select_related('categorylol')


class CategoryListView(ListAPIView):

    """This ListView for getting Category names, displayorder,
    category_level and parentcategoryid.
    """

    serializer_class = CategoryListSerializer
    permission_classes = [permissions.AllowAny]
    # using select_related to pre load categoryname table data
    queryset = Category.objects.exclude(
        parentcategoryid__isnull=True).annotate(
        product_count=Count('categoryproduct')).select_related(
        'categorylol').prefetch_related('categoryproduct').order_by("-product_count")[:11]
