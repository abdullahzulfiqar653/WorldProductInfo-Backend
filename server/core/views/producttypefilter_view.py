from django.db.models import Count, Q
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.utils import categories_with_all_childs
from core.serializers import SearchAttributeValuesListSerializer
from core.models import Product, SearchAttribute, SearchAttributeValues, Category


class ProductTypeFilterNames(ListAPIView):

    """Listing product filter names for left dsiplayed filters on product
    listing page from the SearchAttributeValues table."""

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

        """
        1: getting queryset of searchAttributeValues table by using filtered value_ids
        2: using Annotations to get the count of products for each category
        3: prefetch_related to pre load searchAttributeValue."""
        queryset = SearchAttributeValues.objects.annotate(
            product_count=Count('searchAttributeValue__productid',
                                filter=(Q(searchAttributeValue__productid__categoryid__in=all_categories,
                                          searchAttributeValue__productid__productDescription__type=2
                                          )))).filter(
            valueid__in=values_ids, product_count__gt=0).prefetch_related(
            'searchAttributeValue').order_by("-product_count")
        return queryset
