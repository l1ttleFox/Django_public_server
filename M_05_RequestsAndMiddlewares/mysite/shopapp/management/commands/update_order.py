from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    """ Adds products to order. """
    
    def handle(self, *args, **options):
        order = Order.objects.last()
        if not order:
            self.stdout.write("There is no orders.")
            return
        
        products = Product.objects.all()
        
        for i_product in products:
            order.products.add(i_product)
            
        order.save()
        
        self.stdout.write(self.style.SUCCESS(f"Added products ({order.products.all()})."))

