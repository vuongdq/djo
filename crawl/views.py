from rest_framework import generics
from .models import Product2
from .serializers import Product2Serializer

class Product2List(generics.ListCreateAPIView):
    queryset = Product2.objects.all()
    serializer_class = Product2Serializer

class Product2Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product2.objects.all()
    serializer_class = Product2Serializer
