from django.urls import path

from .views import (
    shop_index,
    groups_list,
    ProductListView,
    CreateProductView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    CreateOrderView,
    OrderListView,
    OrderDetailView,
    OrderUpdateView,
    OrderDeleteView
)

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/create/", CreateProductView.as_view(), name="create_product"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="update_product"),
    path("products/<int:pk>/archive/", ProductDeleteView.as_view(), name="delete_product"),
    path("orders/", OrderListView.as_view(), name="orders_list"),
    path("orders/create/", CreateOrderView.as_view(), name="create_order"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_details"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="update_order"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="delete_order")
]
