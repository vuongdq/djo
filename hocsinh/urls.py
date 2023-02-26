from django.urls import path
from .views import HocSinhList, HocSinhDetail

urlpatterns = [
    path('hocsinh/', HocSinhList.as_view(), name='hoc_sinh_list'),
    path('hocsinh/<str:pk>/', HocSinhDetail.as_view(), name='hoc_sinh_detail'),
]
