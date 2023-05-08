from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .models import Product, Order


@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)
    
    
class OrderInline(admin.TabularInline):
    model = Product.orders.through
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "price", "sale", "create_time", "archived",
    list_display_links = "pk", "name",
    search_fields = "pk", "name",
    ordering = "name", "pk",
    inlines = [
        OrderInline
    ]
    fieldsets = [
        (None, {
            "fields": ("name", "description"),
            "description": "Common fields",
        }),
        ("Price options", {
            "fields": ("price", "sale"),
            "classes": ("wide",),
            "description": "All about money",
        }),
        ("Additional options", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Be careful here"
        })
    ]
    actions = [
        mark_archived,
        mark_unarchived,
    ]


class ProductInline(admin.TabularInline):
    model = Order.products.through
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "pk", "user_verbose", "delivery_address", "promocode", "create_time",
    list_display_links = "pk",
    search_fields = "pk", "delivery_address", "user",
    ordering = "pk",
    inlines = [
        ProductInline
    ]
    
    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")
    
    @staticmethod
    def user_verbose(object: Order) -> str:
        return object.user.first_name or object.user.username
    