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
        # Getting manufacturer queryset on the basis of filtered manufacturerIds
        queryset = Manufacturer.objects.filter(
            manufacturerid__in=manufacturer_ids)
        return queryset

    def get_serializer_context(self):
        return {'categoryids': self.all_categories}
