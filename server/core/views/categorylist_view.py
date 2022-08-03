from core.models import Category
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import CategoryListSerializer


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.exclude(
        parentcategoryid__isnull=True).select_related('categorylol')
