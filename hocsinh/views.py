from rest_framework import generics
from .models import HocSinh
from .serializers import HocSinhSerializer

class HocSinhList(generics.ListCreateAPIView):
    queryset = HocSinh.objects.all()
    serializer_class = HocSinhSerializer

class HocSinhDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HocSinh.objects.all()
    serializer_class = HocSinhSerializer
