from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView, DetailView
from .forms import ProductReviewForm



class ProductList(ListView):
    model = Product
    
class ProductDetails(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context["related_product"] = Product.objects.filter(brand=product.brand)
        return context
    
    

def add_review(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.product = product
            myform.save()
            product.nbr_reviewe += 1
            product.save()
    return redirect(f'/products/{product.slug}')        
    