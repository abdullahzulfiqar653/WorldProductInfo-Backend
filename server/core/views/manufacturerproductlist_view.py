from core.models import Product
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import ProductListSerializer


class ProductManufacterFilterListView(ListAPIView):

    """send manufacturer id as query param to get product list
    and category id as query param to get product list """

    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.request.query_params.get('categoryid', None)
        manufacturer_id = self.request.query_params.get('manufacturerid', None)
        mfg_id = Product.objects.filter(
            manufacturerid=manufacturer_id).values('productid')
        queryset = Product.objects.filter(productid__in=mfg_id,
                                          categoryid=category_id
                                          ).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset
