from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=120, null=False, blank=True)
    age = models.IntegerField(blank=True, null=False, default=0)
    delivery_address = models.TextField(max_length=50, null=True, blank=False)
    
    