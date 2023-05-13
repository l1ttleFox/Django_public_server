from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order


class Command(BaseCommand):
    """ Creates example order. """
    
    def handle(self, *args, **options):
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="Kremlin, d 1",
            promocode="111",
            user=user,
        )
        self.stdout.write(self.style.SUCCESS("New order created."))
