from django.db.models import Count
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from core.serializers import *
from core.models import *
from core.serializers.product_serializers import *
from core.serializers.product_list_serializers import *
from core.serializers.categories_serializers import *


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
        mfg_id = Product.objects.filter(
            manufacturerid=1020186).values_list('productid', flat=True)
        queryset = Product.objects.filter(productid__in=mfg_id, categoryid=4800).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        print(len(queryset))
        return queryset


class ProductCategoryFilter(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(
            categoryid=10273).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset


class ProductTypeFilter(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product_ids = list(SearchAttribute.objects.filter(
            valueid=2369529).values_list('productid', flat=True))
        print(product_ids)
        queryset = Product.objects.filter(productid__in=product_ids, categoryid=10206
                                          ).prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )
        return queryset


class CategoryNameFilter(ListAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):

        cat_queryset = Category.objects.filter(parentcategoryid=10041)

        cat_ids = list(cat_queryset.values_list('categoryid', flat=True))

        queryset = Category.objects.filter(
            categoryid__in=cat_ids)

        return queryset


class ManufacturerFilter(ListAPIView):
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        cat_list = Product.objects.filter(categoryid=10025).values_list(
            'manufacturerid', flat=True).distinct()
        queryset = Manufacturer.objects.filter(manufacturerid__in=cat_list)
        return queryset


class ProductTypeFilterNames(ListAPIView):
    serializer_class = SearchAttributeValuesSerializer

    def get_queryset(self):
        product_ids = Product.objects.filter(
            categoryid=10925).values_list('productid', flat=True).distinct()
        print(product_ids)
        v_ids = SearchAttribute.objects.filter(
            productid__in=product_ids).values_list('valueid', flat=True).order_by('valueid')
        queryset = SearchAttributeValues.objects.filter(valueid__in=v_ids)

        return queryset


class ProductAttribuiteFilterNames(ListAPIView):
    serializer_class = ProductAttributeSerializer

    def get_queryset(self):
        product_ids = Product.objects.filter(
            categoryid=10925).values_list('productid', flat=True).distinct().prefetch_related('productid')
        v_ids = SearchAttribute.objects.filter(
            productid__in=product_ids).values_list('attributeid', flat=True).distinct().prefetch_related('attributeid')
        queryset = Productattribute.objects.filter(attributeid__in=v_ids, productid__categoryid=10925).prefetch_related(
            'attributeid').select_related('attributeid')

        return queryset
