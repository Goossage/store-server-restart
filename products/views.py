from django.shortcuts import render
from products.models import Product,ProductCategory, Basket
# Create your views here.

def index(request):
    context = {
        "title": "store",
        "user": request.user.username
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        "title": "store-каталог",
        "user": request.user.username,
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
        'basket': Basket.objects.all().filter(user__in=request.user)
    }
    return render(request, 'products/products.html', context)