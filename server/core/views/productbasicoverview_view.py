from core.models import Product
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from core.serializers import ProductBasicOverViewSerializer


class ProductBasicOverView(RetrieveAPIView):

    """This view for getting product basic overview tab Data in the Product detail by using product id."""

    permission_classes = (AllowAny,)
    # prefatch related is used for pre load data from product attribute table and attributename table using related name.
    queryset = Product.objects.filter(
        isactive=True).prefetch_related('productAttribute__attributeid',)
    serializer_class = ProductBasicOverViewSerializer
