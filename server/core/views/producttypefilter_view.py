from unicodedata import category
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import SearchAttributeValuesSerializer
from core.models import Product, SearchAttribute, SearchAttributeValues, Category


class ProductTypeFilterNames(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SearchAttributeValuesSerializer

    def get_queryset(self):
        parent_category_id = self.request.query_params.get(
            'parentcategoryid', None)

        parent_category_id = Category.objects.filter(
            parentcategoryid=parent_category_id).select_related('categoryid').values_list(
            'categoryid', flat=True)
        product_ids = Product.objects.filter(
            categoryid__in=parent_category_id).values_list('productid', flat=True).distinct()
        values_ids = SearchAttribute.objects.filter(
            productid__in=product_ids, attributeid=1100).values_list('valueid', flat=True).order_by('valueid')
        queryset = SearchAttributeValues.objects.filter(valueid__in=values_ids)

        return queryset
