from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):

    """
        get -> list queryset
        get -> retrieve a instance details
        post -> create new instance
        put -> update
        patch -> partial update
        delete -> destroy
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
    ):

    """
        get -> list queryset
        get -> retrieve a instance details
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

product_list_view = ProductGenericViewSet.as_view({"get": "list"})

product_detail_view = ProductGenericViewSet.as_view({"get": "retrieve"})