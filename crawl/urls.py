from django.urls import path
from .views import Product2List, Product2Detail

urlpatterns = [
    path('products2/', Product2List.as_view(), name='product2-list'),
    path('products2/<int:pk>/', Product2Detail.as_view(), name='product2-detail'),
]
