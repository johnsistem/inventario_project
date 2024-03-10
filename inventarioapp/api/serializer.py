from rest_framework import serializers
from inventarioapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
   class Meta:
      model = Product
      fields = '__all__'