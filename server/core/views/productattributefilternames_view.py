from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import ProductAttributeSerializer
from core.models import Productattribute, SearchAttribute, Product


class ProductAttribuiteFilterNames(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductAttributeSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        product_ids = Product.objects.filter(
            categoryid=category_id).values_list('productid', flat=True).distinct().prefetch_related('productid')
        attribute_ids = SearchAttribute.objects.filter(
            productid__in=product_ids).values_list(
                'attributeid', flat=True).distinct().prefetch_related('attributeid')
        queryset = SearchAttribute.objects.filter(
            productid=product_ids, productid__categoryid=category_id).prefetch_related(
            'attributeid',).select_related('attributeid').distinct()

        return queryset
