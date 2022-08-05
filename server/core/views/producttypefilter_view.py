from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import SearchAttributeValuesListSerializer
from core.models import Product, SearchAttribute, SearchAttributeValues, Category


class ProductTypeFilterNames(ListAPIView):

    """
    This ListView getting ProductTypeNames for the left displayed
    product type filter, by using parentcategoryid.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = SearchAttributeValuesListSerializer

    def get_queryset(self):
        parent_category_id = self.request.query_params.get(
            'parentcategoryid', None)
        # getting categoryIds by using parentCategoryId from the category table.
        category_ids = Category.objects.filter(
            parentcategoryid=parent_category_id).values('categoryid')
        # getting productIds from product table by using filtered categoryIds
        product_ids = Product.objects.filter(
            categoryid__in=category_ids).values('productid')
        # getting valueIds from searchAttributeTable by using filtered product ids
        values_ids = SearchAttribute.objects.filter(
            productid__in=product_ids, attributeid__name='Product Type').values('valueid')
        # getting valueNames from  searchAttributeValues table by using filtered value_ids
        queryset = SearchAttributeValues.objects.filter(valueid__in=values_ids)
        return queryset
