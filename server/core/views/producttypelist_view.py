from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.models import Product, SearchAttribute
from core.serializers import ProductListSerializer


class ProductTypeFilterListView(ListAPIView):

    """ send value id as query param to get product list 
    and category id as query param to get product list that have no chiled category """

    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        value_id = self.request.query_params.get(
            'valueid', None)
        product_ids = SearchAttribute.objects.filter(
            valueid=value_id).values('productid')
        queryset = Product.objects.filter(productid__in=product_ids, categoryid=category_id
                                          ).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset
