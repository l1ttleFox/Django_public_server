from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Product, Order


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999),
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


class ProductListView(ListView):
    """ Class-based view для отображения списка продуктов. """
    template_name = 'shopapp/products-list.html'
    queryset = Product.objects.filter(archived=False)
    context_object_name = "products"


class CreateProductView(CreateView):
    """ Class-based view для создания нового продукта. """
    model = Product
    fields = "name", "description", "price", "discount"
    success_url = reverse_lazy('shopapp:products_list')


class ProductDetailView(DetailView):
    """ Class-based view для просмотра деталей продукта. """
    template_name = 'shopapp/product_details.html'
    model = Product
    context_object_name = "object"
    

class ProductUpdateView(UpdateView):
    """ Class-based view для обновления деталей продукта. """
    model = Product
    fields = "name", "description", "price", "discount"
    template_name_suffix = "_update"
    
    def get_success_url(self):
        return reverse(
            "shopapp:product_details",
            kwargs={"pk": self.object.pk}
        )
    
    
class ProductDeleteView(DeleteView):
    """ Class-based view для архивирования продукта. """
    model = Product
    success_url = reverse_lazy('shopapp:products_list')
    
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
    

class CreateOrderView(CreateView):
    """ Class-based view для создания нового заказа. """
    model = Order
    fields = "delivery_address", "promocode", "user", "products"
    success_url = reverse_lazy("shopapp:orders_list")
    

class OrderListView(ListView):
    """ Class-based view для отображения списка продуктов. """
    template_name = 'shopapp/orders-list.html'
    model = Order
    context_object_name = "orders"


class OrderDetailView(DetailView):
    """ Class-based view для отображения деталей заказа. """
    template_name = 'shopapp/order_details.html'
    model = Order
    context_object_name = "object"
    

class OrderUpdateView(UpdateView):
    """ Class-based view для обновления деталей заказа. """
    model = Order
    fields = "delivery_address", "promocode", "user", "products"
    template_name_suffix = "_update"
    
    def get_success_url(self):
        return reverse(
            "shopapp:order_details",
            kwargs={"pk": self.object.pk}
        )
    

class OrderDeleteView(DeleteView):
    """ Class-based view для полного удаления заказа. """
    model = Order
    success_url = reverse_lazy('shopapp:orders_list')