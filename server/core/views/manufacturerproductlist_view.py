from core.models import Product
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.utils import categories_with_all_childs
from core.serializers import ProductListSerializer


class ProductManufacterFilterListView(ListAPIView):

    """This ListView is used for product list in category page 
    and filter the Product list by manufacturer by using manufacturer
    id and category id.
    """
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def __init__(self, **kwargs) -> None:
        self.all_categories = None

    def get_queryset(self):
        category_id = self.request.query_params.get('categoryid', None)
        manufacturer_id = self.request.query_params.get('manufacturerid', None)
        #getting all child categories of the category ids
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
