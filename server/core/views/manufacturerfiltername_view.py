from rest_framework import permissions
from core.models import Manufacturer, Product
from rest_framework.generics import ListAPIView
from core.serializers import ManufacturerFilterNameSerializer


class ManufacturerFilter(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ManufacturerFilterNameSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        manufacturer_ids = Product.objects.filter(categoryid=category_id).values_list(
            'manufacturerid', flat=True).distinct()
        queryset = Manufacturer.objects.filter(
            manufacturerid__in=manufacturer_ids)
        return queryset

    def get_serializer_context(self):
        return {'categoryid': self.request.query_params.get(
            'categoryid', None)}
