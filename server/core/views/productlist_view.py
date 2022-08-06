from rest_framework import permissions
from core.utils import LimitOffsetPagination
from rest_framework.generics import ListAPIView
from core.utils import categories_with_all_childs
from core.serializers import ProductListSerializer
from core.models import Product, Productdescriptions, SearchAttribute


class ProductListView(ListAPIView):

    """This ListView for getting product list in  the Product list by using and CategoryId.
    """

    serializer_class = ProductListSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.AllowAny]

    def __init__(self, **kwargs) -> None:
        self.all_categories = None

    def get_queryset(self):
        flag = self.request.query_params.get('flag', None)
        category_id = self.request.query_params.get(
            'categoryid', None)
        search = self.request.query_params.get('search', None)
        value_id = self.request.query_params.get(
            'valueid', None)
        manufacturer_id = self.request.query_params.get('manufacturerid', None)

        if flag.lower() == 'manufacturer':
            # getting all child categories of the category ids
            self.all_categories = categories_with_all_childs(category_id)
            # Getting product id from the product table by using manufacturer id .
            product_ids = Product.objects.filter(
                manufacturerid=manufacturer_id).values('productid')
            # Getting the product query set by using the filtered product id.
            queryset = Product.objects.filter(productid__in=product_ids,
                                              categoryid__in=self.all_categories
                                              ).prefetch_related(
                'productDescription',
                'productSkus',
                'productElements__productElementProperties'
            )
            return queryset
        elif flag.lower() == 'category':

            # getting all child categories of the category ids
            self.all_categories = categories_with_all_childs(category_id)
            # prefectching the product description, product skus and product elements by using prefetch_related.
            queryset = Product.objects.filter(
                categoryid__in=self.all_categories).prefetch_related(
                'productDescription',
                'productSkus',
                'productElements__productElementProperties'
            )
            return queryset

        elif flag.lower() == 'search':

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

        elif flag.lower() == 'productType':

            # getting product id from the Search attribute  table by using valueid.
            product_ids = SearchAttribute.objects.filter(
                valueid=value_id).values('productid')
            # getting category and child categories of the category ids
            self.all_categories = categories_with_all_childs(category_id)
            # getting the product query set by using the filtered product id and category_id.
            # prefectching the product description, product skus and product elements by using prefetch_related.
            queryset = Product.objects.filter(productid__in=product_ids, categoryid__in=self.all_categories
                                              ).prefetch_related(
                'productDescription',
                'productSkus',
                'productElements__productElementProperties'
            )
            return queryset
        else:
            return Product.objects.none()
