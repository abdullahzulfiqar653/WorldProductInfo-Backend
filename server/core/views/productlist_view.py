from core.models import Product
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.utils import categories_with_all_childs
from core.serializers import ProductListSerializer


class ProductListView(ListAPIView):

    """This ListView for getting product list in  the Product list by using and CategoryId.
    """

    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def __init__(self, **kwargs) -> None:
        self.all_categories = None

    def get_queryset(self):
        # flag = self.request.query_params.get('flag')
        # if not flag:
        #     return Product.objects.none()
        category_id = self.request.query_params.get(
            'categoryid', None)
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
