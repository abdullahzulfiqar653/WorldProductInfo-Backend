from django.db.models import Count
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from core.serializers import *
from core.models import *
from core.serializers.product_serializers import ProductSerializer, ManufacturerSerializer
from core.serializers.product_list_serializers import ProductListSerializer
from core.serializers.categories_serializers import CategoryListSerializer


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
        parent_cat_level = Category.objects.get(categoryid=1).catlevel
        cat_queryset = Category.objects.filter(parentcategoryid=1)

        cat_ids = list(cat_queryset.values_list('categoryid', flat=True))

        for i in range(parent_cat_level + 1, 4):
            queryset = cat_queryset.filter(catlevel=i).exclude(
                parentcategoryid__in=cat_ids)

        queryset = Category.objects.filter(
            parentcategoryid__in=queryset)

        return queryset


class ManufacturerFilter(ListAPIView):
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        cat_list = Product.objects.filter(categoryid=10025).values_list(
            'manufacturerid', flat=True).distinct()
        queryset = Manufacturer.objects.filter(manufacturerid__in=cat_list)
        return queryset
