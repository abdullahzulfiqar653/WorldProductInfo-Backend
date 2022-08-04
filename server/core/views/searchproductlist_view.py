from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import ProductListSerializer
from core.models import Product, Productdescriptions


class SearchProductListView(ListAPIView):

    """send search as query param to get product list """

    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        product_ids = Productdescriptions.objects.filter(
            description__icontains=search).values('productid')

        queryset = Product.objects.filter(
            productid__in=product_ids).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset
