from ..models import ShoppingCard, Product, ShoppingItem
from .serializers import ShoppingCardSerializer, ProductSerializer
from rest_framework import generics

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
