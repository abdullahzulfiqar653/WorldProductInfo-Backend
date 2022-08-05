from django.db.models import Q
from rest_framework import permissions
from core.models import Category, Product
from rest_framework.generics import ListAPIView
from core.serializers import CategoryFilterNameListSerializer


class CategoryFilterNameView(ListAPIView):

    """ This ListView for getting category filter names 
        by using ParentCategoryId from the category table.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = CategoryFilterNameListSerializer

    def get_queryset(self):
        parent_category_id = self.request.query_params.get(
            'parentcategoryid', None)
        # getting category Id by using parent category id from the category table.
        category_ids = Category.objects.filter(
            parentcategoryid=parent_category_id).values('categoryid')
        """
        getting CategoryIds by using category Ids from the product table.
        And exclude all category Ids That have no products In the given list of categories.
        """
        products_category_ids = Product.objects.exclude(
            ~Q(categoryid__in=category_ids)).values('categoryid')
        # getting categories name and ids by using Filtered category ids that have no category child.
        # select_related is used for getting category name and id from the category table by using revese relations.
        queryset = Category.objects.filter(
            categoryid__in=products_category_ids).select_related('categorylol')

        return queryset
