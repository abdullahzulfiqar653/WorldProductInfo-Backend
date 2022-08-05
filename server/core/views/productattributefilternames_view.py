from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import ProductAttributeSerializer
from core.models import Productattribute, SearchAttribute, Product
from core.models import Attributenames
from core.models import SearchAttributeValues


class ProductAttribuiteFilterNames(ListAPIView):

    """ This ListView is used to get attribute names and value from the search attribute table. """

    permission_classes = [permissions.AllowAny]
    serializer_class = ProductAttributeSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        product_ids = Product.objects.filter(
            categoryid=category_id).values('productid')
        queryset = SearchAttribute.objects.filter(
            productid__in=product_ids).prefetch_related('attributeid', 'valueid')
        # queryset_a = Attributenames.objects.filter(
        #     attributeid__in=attribute_ids).values('name')
        # queryset_b = SearchAttributeValues.objects.filter(
        #     valueid__in=value_ids).values('value')

        return queryset
