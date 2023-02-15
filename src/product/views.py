from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView, DetailView
from .forms import ProductReviewForm



class ProductList(ListView):
    model = Product
    
    
    
class ProductDetails(DetailView):
    model = Product

def add_review(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.product = product
            myform.save()
    return redirect(f'/products/{product.slug}')        
    