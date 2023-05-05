from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    """ Creates products. """
    
    def handle(self, *args, **options):
        
        products = [
            ("Watermelon", 300),
            ("Mango", 222),
            ("Strawberry", 777),
        ]
        
        for i_product_name, i_product_price in products:
            print(i_product_price, i_product_name)
            product, created = Product.objects.get_or_create(name=i_product_name, price=i_product_price)
            self.stdout.write(self.style.SUCCESS(f"Created product {product.name}"))
            