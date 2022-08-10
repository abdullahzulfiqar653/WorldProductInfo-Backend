from core.models import Product
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from core.serializers import ProductGallerySerializer


class ProductGalleryView(RetrieveAPIView):
    """getting  gallery Tab data in the Product detail by using product id."""

    permission_classes = (AllowAny,)
    # to pre load data from product element table and their child table .
    queryset = Product.objects.filter(
        isactive=True).prefetch_related(
            'productElements__productElementProperties')
    serializer_class = ProductGallerySerializer
