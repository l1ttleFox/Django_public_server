from django.http import HttpRequest
from django.shortcuts import render
from shopapp.models import Order, Product


def shop_index(request: HttpRequest) -> object:
    context = {
    
    }
    return render(request, 'shopapp/shop-index.html', context=context)
    

def orders_list(request: HttpRequest) -> object:
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


def products_list(request: HttpRequest) -> object:
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)
