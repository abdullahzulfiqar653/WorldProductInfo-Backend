from core.models import Product
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import ProductListSerializer


class ProductManufacterFilterListView(ListAPIView):

    """This ListView is used for product list in category page 
    and filter the Product list by manufacturer by using manufacturer
    id and category id.
    """
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.request.query_params.get('categoryid', None)
        manufacturer_id = self.request.query_params.get('manufacturerid', None)
        # Getting product id from the product table by using manufacturer id .
        mfg_id = Product.objects.filter(
            manufacturerid=manufacturer_id).values('productid')
        # Getting the product query set by using the filtered product id.
        queryset = Product.objects.filter(productid__in=mfg_id,
                                          categoryid=category_id
                                          ).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset
