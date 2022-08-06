from django.db.models import Count
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.utils import categories_with_all_childs
from core.serializers import SearchAttributeValuesListSerializer
from core.models import Product, SearchAttribute, SearchAttributeValues, Category


class ProductTypeFilterNames(ListAPIView):

    """Listing product filter names for left dsiplayed filters on product 
    listing page by using CategoryId from the SearchAttributeValues table."""

    permission_classes = [permissions.AllowAny]
    serializer_class = SearchAttributeValuesListSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        # getting all child categoryIds by using CategoryId from the category table.
        all_categories = categories_with_all_childs(category_id)
        # getting productIds from product table by using filtered categoryIds
        product_ids = Product.objects.filter(
            categoryid__in=all_categories).values('productid').distinct()
        # getting valueIds from searchAttributeTable by using filtered productIds
        values_ids = SearchAttribute.objects.filter(
            productid__in=product_ids, attributeid__name='Product Type').values('valueid')
        # getting valueNames from  searchAttributeValues table by using filtered value_ids
        # annotate to get the count of products for each value and prefetch_related to pre load products using related name.
        queryset = SearchAttributeValues.objects.filter(
            valueid__in=values_ids).annotate(
                product_count=Count('searchAttributeValue__productid')).prefetch_related('searchAttributeValue')
        return queryset
