from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import ProductListSerializer
from core.models import Product, Productdescriptions


class SearchProductListView(ListAPIView):

    """This ListView for getting product list in category page by using search keyword."""

    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        # getting product id from the product table by using search keyword.
        product_ids = Productdescriptions.objects.filter(
            description__icontains=search).values('productid')
        # getting the product query set by using the filtered product id.
        # prefectching the product description, product skus and product elements by using prefetch_related.
        queryset = Product.objects.filter(
            productid__in=product_ids).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset
