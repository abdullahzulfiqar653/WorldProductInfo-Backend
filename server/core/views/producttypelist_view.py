from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.models import Product, SearchAttribute
from core.utils import categories_with_all_childs
from core.serializers import ProductListSerializer


class ProductTypeFilterListView(ListAPIView):
    """This ListView for getting product List by using product type filter in the selected category page.
    Note: The category id could be posted in params that have no child category.
   """

    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def __init__(self, **kwargs) -> None:
        self.all_categories = None

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        value_id = self.request.query_params.get(
            'valueid', None)
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
