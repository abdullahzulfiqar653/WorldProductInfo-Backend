from rest_framework import permissions
from django.db.models import Prefetch, Q
from core.utils import LimitOffsetPagination
from rest_framework.generics import ListAPIView
from core.utils import categories_with_all_childs
from core.serializers import ProductListSerializer
from core.models import (
    Product,
    Productdescriptions,
    SearchAttribute,
    Productsimilar,
    Productaccessories
)


class ProductListView(ListAPIView):

    """This ListView for getting product list in  the Product list by using and CategoryId.
    """

    serializer_class = ProductListSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.AllowAny]

    def __init__(self, **kwargs) -> None:
        self.all_categories = None
        self.flags_list = ['manufacturer',
                           'category', 'producttype', 'similar']
        # prefectched productDescription, productSkus and productElements.
        self.initial_querset = Product.objects.prefetch_related(
            Prefetch('productDescription', queryset=Productdescriptions.objects.filter(
                type=2), to_attr='type_description'),
        ).filter(productDescription__type=2).order_by('-lastupdated')

    def get_queryset(self):
        flag = self.request.query_params.get('flag')
        category_id = self.request.query_params.get('categoryid')

        if flag in self.flags_list:
            # getting all child categories of the category ids
            self.all_categories = categories_with_all_childs(category_id)

        if flag == 'manufacturer':
            manufacturer_id = self.request.query_params.get('manufacturerid')
            # Getting the product query set by using the filtered product id.
            queryset = self.initial_querset.filter(manufacturerid=manufacturer_id,
                                                   categoryid__in=self.all_categories)
            return queryset.order_by('-modifieddate', '-creationdate')

        elif flag == 'producttype':
            value_id = self.request.query_params.get('valueid')
            # getting product id from the Search attribute table by using valueid.
            product_ids = SearchAttribute.objects.filter(
                valueid=value_id).values('productid')
            # getting the product query set by using the filtered product id and category_id.
            queryset = self.initial_querset.filter(productid__in=product_ids,
                                                   categoryid__in=self.all_categories)
            return queryset.order_by('-modifieddate', '-creationdate')

        elif flag == 'category':
            queryset = self.initial_querset.filter(
                categoryid__in=self.all_categories)
            return queryset.order_by('-modifieddate', '-creationdate')

        elif flag == 'search':
            search = self.request.query_params.get('search')

            queryset = self.initial_querset.filter(
                Q(mfgpartno__iexact=search) |
                Q(productDescription__description__icontains=search, ), productDescription__type=2
            ).distinct()

            return queryset.order_by('-modifieddate', '-creationdate')

        elif flag == 'similar':
            product_id = self.request.query_params.get('productid')
            # getting product id from the productsimilar table by using product id.
            product_ids = Productsimilar.objects.filter(
                similarproductid=product_id).values('productid')
            # getting the product query set by using the filtered product id.
            queryset = self.initial_querset.filter(productid__in=product_ids)
            return queryset.order_by('-modifieddate', '-creationdate')

        elif flag == 'accessories':
            product_id = self.request.query_params.get('productid')
            # getting product id from the productaccessories table by using product id.
            product_ids = Productaccessories.objects.filter(
                accessoryproductid=product_id).values('productid')
            # getting the product query set by using the filtered product id.
            queryset = self.initial_querset.filter(productid__in=product_ids)
            return queryset.order_by('-modifieddate', '-creationdate')

        elif flag == 'latest':
            queryset = self.initial_querset.all()
            return queryset

        elif flag == 'onlyManufacture':
            manufacturer_id = self.request.query_params.get('manufacturerid')
            queryset = self.initial_querset.filter(
                manufacturerid=manufacturer_id)
            return queryset
        return self.initial_querset.none()
