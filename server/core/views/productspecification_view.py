from core.models import Product
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from core.serializers import ProductSpecificationSerializer


class ProductSpecificationView(RetrieveAPIView):

    """getting specification Tab data for Product detail by using product id."""

    permission_classes = (AllowAny,)
    # prefetch data from headername and attributenames and productattribute table
    queryset = Product.objects.filter(
        isactive=True).prefetch_related(
            'categoryid__categoryHeader__headerid', 'productAttribute__attributeid')
    serializer_class = ProductSpecificationSerializer
