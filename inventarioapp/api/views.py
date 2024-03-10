
from rest_framework import viewsets 

from inventarioapp.api.serializer import ProductSerializer
from inventarioapp.models import Product

class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer