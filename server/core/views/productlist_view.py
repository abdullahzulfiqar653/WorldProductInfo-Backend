from core.models import Product
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import ProductListSerializer


class ProductListView(ListAPIView):
    """send categorid as query param to get product list 
    this api is used for product list in category page and category filter """
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        queryset = Product.objects.filter(
            categoryid=category_id).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset
