from core.models import Product
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from core.serializers import ProductRetrieveSerializer


class ProductRetrieveView(RetrieveAPIView):

    """getting product detail in the Product detail by using product id."""

    permission_classes = (AllowAny,)
    # prefectch related is used for pre load data from productDescription, productSkus and productElements using related name.
    queryset = Product.objects.filter(
        isactive=True).prefetch_related(
        'productSkus',
        'productElements__productElementProperties',
        'productDescription',

    )
    serializer_class = ProductRetrieveSerializer
