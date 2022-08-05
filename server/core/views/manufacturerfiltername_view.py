from rest_framework import permissions
from core.models import Manufacturer, Product
from rest_framework.generics import ListAPIView
from core.serializers import ManufacturerFilterNameSerializer


class ManufacturerFilter(ListAPIView):
    """This ListView for getting Manufacturer names, and product count.
        For the related manufacturer, get the product count in the selected category id.


    """

    permission_classes = [permissions.AllowAny]
    serializer_class = ManufacturerFilterNameSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('categoryid', None)
        # Getting manufacturer id from the product table and remove the duplicates.
        manufacturer_ids = Product.objects.filter(categoryid=category_id).values(
            'manufacturerid').distinct()
        # Getting the manufacturer query set by using the filtered manufacturer id.
        queryset = Manufacturer.objects.filter(
            manufacturerid__in=manufacturer_ids)
        return queryset

    def get_serializer_context(self):
        """This method is used to pass the category id to the serializer."""
        return {'categoryid': self.request.query_params.get(
            'categoryid', None)}
