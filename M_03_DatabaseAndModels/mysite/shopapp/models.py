from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20, null=False, blank=True)
    description = models.TextField(max_length=200, null=False, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=11)
    sale = models.PositiveSmallIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    

class Order(models.Model):
    delivery_address = models.TextField(max_length=100, null=False, blank=True)
    promocode = models.CharField(max_length=8, null=False, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")