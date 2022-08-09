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
        self.flags_list = ['manufacturer', 'category', 'producttype']
        # prefectched productDescription, productSkus and productElements.
        self.initial_querset = Product.objects.prefetch_related(
            'productDescription',
            'productSkus',
            'productElements__productElementProperties'
        )

    def get_queryset(self):
        flag = self.request.query_params.get('flag')
        category_id = self.request.query_params.get('categoryid')

        if flag in self.flags_list:
            # getting all child categories of the category ids
            self.all_categories = categories_with_all_childs(category_id)

        if flag == 'manufacturer':
            manufacturer_id = self.request.query_params.get('manufacturerid')
            # Getting product id from the product table by using manufacturer id .
            product_ids = Product.objects.filter(
                manufacturerid=manufacturer_id).values('productid')
            # Getting the product query set by using the filtered product id.
            queryset = self.initial_querset.filter(productid__in=product_ids,
                                                   categoryid__in=self.all_categories
                                                   )
            return queryset

        elif flag == 'producttype':
            value_id = self.request.query_params.get('valueid')
            # getting product id from the Search attribute table by using valueid.
            product_ids = SearchAttribute.objects.filter(
                valueid=value_id).values('productid')
            # getting the product query set by using the filtered product id and category_id.
            queryset = self.initial_querset.filter(productid__in=product_ids,
                                                   categoryid__in=self.all_categories)
            return queryset

        elif flag == 'category':
            queryset = self.initial_querset.filter(
                categoryid__in=self.all_categories)
            return queryset

        elif flag == 'search':
            search = self.request.query_params.get('search')

            # getting product id from the product table by using search keyword.
            product_ids = Productdescriptions.objects.filter(
                description__icontains=search).values('productid')

            # getting the product query set by using the filtered product id.
            queryset = self.initial_querset.filter(productid__in=product_ids)
            return queryset
        else:
            return Product.objects.none()
