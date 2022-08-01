from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from core.serializers import *
from core.models import *
from core.serializers.product_serializers import ProductSerializer
from core.serializers.product_list_serializers import ProductListSerializer


class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.filter(
        isactive=True).select_related('manufacturerid', ).prefetch_related('productSkus', 'productElements__productElementProperties', 'productAttribute__attributeid', 'productDescription', 'categoryid__categoryHeader__headerid')
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.filter(
        categoryid=5094).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
    )
    serializer_class = ProductListSerializer


class ProductSearchView(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product_ids = list(Productdescriptions.objects.filter(
            description__icontains='sony').values_list('productid', flat=True))

        queryset = Product.objects.filter(
            productid__in=product_ids).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        print(self.request.query_params.get('search', None))
        return queryset


class ProductManufacterFilter(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(
            manufacturerid=102764).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset


class ProductCategoryFilter(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(
            categoryid=4900).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset
