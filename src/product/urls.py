from django.urls import path
from .views import ProductDetails, ProductList, add_review


app_name = 'product'

urlpatterns = [
    
    path('',ProductList.as_view(), name='product_list'),
    path('<slug:slug>', ProductDetails.as_view(), name='product_detail'),
    path('<slug:slug>/addreview', add_review, name='add_review'),
]
