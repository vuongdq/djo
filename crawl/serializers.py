from rest_framework import serializers
from .models import Product2

class Product2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product2
        fields = '__all__'
