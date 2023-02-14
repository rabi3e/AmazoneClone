from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView


class ProductList(ListView):
    model = Product
    
    
    
class ProductDetails(DetailView):
    model = Product