from django.db.models import Count, Q, When
from rest_framework import permissions
from core.models import Manufacturer, Product
from rest_framework.generics import ListAPIView
from core.utils import categories_with_all_childs
from core.serializers import ManufacturerFilterNameSerializer


class ManufacturerFilter(ListAPIView):
    """Listing Manufacturer filter names for left dsiplayed filters on product
    listing page by using CategoryId from the Manufacturer table."""

    permission_classes = [permissions.AllowAny]
    serializer_class = ManufacturerFilterNameSerializer

    def __init__(self, **kwargs) -> None:
        self.all_categories = None

    def get_queryset(self):
        category_id = self.request.query_params.get('categoryid', None)
        # getting all child categoryIds by using CategoryId from the category table.
        self.all_categories = categories_with_all_childs(category_id)

        # manufacturerids from the product table and remove the duplicates.
        manufacturer_ids = Product.objects.filter(categoryid__in=self.all_categories).values(
            'manufacturerid').distinct()

        # Getting manufacturer queryset on the basis of filte red manufacturerIds
        # using Annotations to get the count of products for each manufacturer and
        # prefetch_related to pre load products using related name.
        queryset = Manufacturer.objects.annotate(
            product_count=Count('manufacturerproduct',
                                filter=(Q(
                                        manufacturerproduct__categoryid__in=self.all_categories,
                                        manufacturerproduct__productDescription__type=2
                                        )))).prefetch_related('manufacturerproduct'
                                                              ).order_by("-product_count"
                                                                         ).filter(
            manufacturerid__in=manufacturer_ids,
            product_count__gt=0)
        return queryset
