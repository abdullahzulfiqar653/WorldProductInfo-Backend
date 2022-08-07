from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from core.utils import categories_with_all_childs

from core.serializers import ProductAttributeSerializer, AttributeSerializer
from core.models import SearchAttribute, Product, Attributenames


class ProductAttribuiteFilterNames(APIView):

    """ This ListView is used to get attribute names and value from the search attribute table. """

    permission_classes = (permissions.AllowAny, )
    serializer_class = (ProductAttributeSerializer, AttributeSerializer)

    def __init__(self, **kwargs) -> None:
        self.all_categories = None

    def get(self, request, format=None):
        category_id = self.request.query_params.get(
            'categoryid', None)
        self.all_categories = categories_with_all_childs(category_id)
        queryset_attribute = SearchAttribute.objects.filter(
            productid__categoryid__in=self.all_categories).values_list('attributeid', flat=True).distinct()
        queryset_value = Attributenames.objects.filter(
            attributeid__in=queryset_attribute).distinct()
        queryset = SearchAttribute.objects.filter(
            productid__categoryid__in=self.all_categories
        ).prefetch_related('valueid')
        serializer = ProductAttributeSerializer(queryset, many=True)
        serializer_2 = AttributeSerializer(queryset_value, many=True)
        # return a.data
        return Response({"Values": serializer.data, "Names": serializer_2.data}, status=200)
