from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('new/', product_new, name='product_new'),
    path('<int:pk>/edit/', product_edit, name='product_edit'),
    path('<int:pk>/delete/', product_delete, name='product_delete'),
]
