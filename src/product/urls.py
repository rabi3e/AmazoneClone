from django.urls import path
from .views import ProductDetails, ProductList


app_name = 'product'

urlpatterns = [
    
    path('',ProductList.as_view(), name='product_list'),
    path('<slug:slug>', ProductDetails.as_view(), name='product_detail')
]
