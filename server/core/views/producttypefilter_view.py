from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import SearchAttributeValuesListSerializer
from core.models import Product, SearchAttribute, SearchAttributeValues, Category


class ProductTypeFilterNames(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SearchAttributeValuesListSerializer

    def get_queryset(self):
        parent_category_id = self.request.query_params.get(
            'parentcategoryid', None)

        parent_category_id = Category.objects.filter(
            parentcategoryid=parent_category_id).values('categoryid')

        product_ids = Product.objects.filter(
            categoryid__in=parent_category_id).values('productid')

        values_ids = SearchAttribute.objects.filter(
            productid__in=product_ids, attributeid=1100).values('valueid')

        queryset = SearchAttributeValues.objects.filter(valueid__in=values_ids)
        return queryset
