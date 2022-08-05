from django.db.models import Q
from core.utils import all_categories_have_no_childs
from rest_framework import permissions
from core.models import Category, Product
from rest_framework.generics import ListAPIView
from core.serializers import CategoryFilterNameListSerializer


class CategoryFilterNameView(ListAPIView):

    """Listing category filter names for left dsiplayed filters on product 
    listing page by using CategoryId from the category table."""

    permission_classes = [permissions.AllowAny]
    serializer_class = CategoryFilterNameListSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get(
            'categoryid', None)
        # getting all child categoryIds who dont have childs by using CategoryId
        all_categories = all_categories_have_no_childs(category_id)

        # excluding those categories who dont have any product available
        products_category_ids = Product.objects.exclude(
            ~Q(categoryid__in=all_categories)).values('categoryid')

        # getting categories also these categories have no childs.
        # using select_related to pre load categoryname table data
        queryset = Category.objects.filter(
            categoryid__in=products_category_ids).select_related('categorylol')

        return queryset
