from django.urls import path
from .views import shop_index, orders_list, products_list

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("orders/", orders_list, name="orders_list"),
    path("products/", products_list, name="products_list"),
]