from core.models import Product
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import ProductListSerializer


class ProductAttributeListView(ListAPIView):

    """This ListView for getting product list in category page 
    and filter the Product list by using and CategoryId.
    """

    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        # prefectching the product description, product skus and product elements by using prefetch_related.
        queryset = Product.objects.filter(
            categoryid=category_id).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset
