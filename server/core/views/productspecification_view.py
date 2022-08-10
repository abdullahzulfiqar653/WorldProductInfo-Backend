from core.models import Product
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from core.serializers import ProductSpecificationSerializer


class ProductSpecificationView(RetrieveAPIView):

    """This view for getting  specification Tab data in the Product detail by using product id."""

    permission_classes = (AllowAny,)
    # prefetch related is used for pre load data from headername and attributenames and product attribute table by using related name.
    queryset = Product.objects.filter(
        isactive=True).prefetch_related(
            'categoryid__categoryHeader__headerid', 'productAttribute__attributeid')
    serializer_class = ProductSpecificationSerializer
