from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    """ Класс формы создания нового продукта. """
    class Meta:
        model = Product
        fields = "name", "description", "price", "discount"
        

class OrderForm(forms.ModelForm):
    """ Класс формы создания нового заказа. """
    class Meta:
        model = Order
        fields = 'delivery_address', 'promocode', 'user', 'products'