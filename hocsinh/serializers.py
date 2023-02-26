from rest_framework import serializers
from .models import HocSinh

class HocSinhSerializer(serializers.ModelSerializer):
    class Meta:
        model = HocSinh
        fields = '__all__'
