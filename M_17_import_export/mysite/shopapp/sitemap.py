from django.contrib.sitemaps import Sitemap
from .models import Product


class ShopSitemap(Sitemap):
    """ Карта приложения shopapp. """
    
    changefreg = "always"
    priority = 0.5
    
    def items(self):
        return Product.objects.filter(archived=False).order_by("created_at")
        
    def lastmod(self, object: Product):
        return Product.created_at
