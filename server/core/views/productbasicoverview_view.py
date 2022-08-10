from core.models import Product
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from core.serializers import ProductBasicOverViewSerializer


class ProductBasicOverView(RetrieveAPIView):

    """getting product basic overview tab Data for Product detail."""

    permission_classes = (AllowAny,)
    # to pre load data from product attribute and attributename table.
    queryset = Product.objects.filter(
        isactive=True).prefetch_related('productAttribute__attributeid',)
    serializer_class = ProductBasicOverViewSerializer
