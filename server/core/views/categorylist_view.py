from core.models import Category
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import CategoryListSerializer


class CategoryListView(ListAPIView):

    """This ListView for getting Category names, displayorder, 
    category_level and parentcategoryid.
    """

    serializer_class = CategoryListSerializer
    permission_classes = [permissions.AllowAny]
    # using select_related to pre load categoryname table data
    queryset = Category.objects.exclude(
        parentcategoryid__isnull=True).select_related('categorylol')
