from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from core.serializers import *
from core.models import *
from core.serializers.product_serializers import ProductSerializer


class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.filter(
        isactive=True).select_related('manufacturerid', ).prefetch_related('productElements__productElementProperties', 'productAttribute__attributeid', 'productDescription', 'categoryid__categoryHeader__headerid')
    serializer_class = ProductSerializer
