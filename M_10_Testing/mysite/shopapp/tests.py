from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse
from .models import Order


class OrderDetailViewTestCase(TestCase):
    """ Тест для просмотра деталей заказа. """
    
    fixtures = ["orders.json", "products.json", "users.json"]
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.credentials = dict(username="temp_user", password="q")
        cls.user = User.objects.create_user(**cls.credentials)
        content_type = ContentType.objects.get_for_model(Order)
        permission = Permission.objects.get(
            codename="view_order",
            content_type=content_type,
        )
        cls.user.user_permissions.add(permission)
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.user.delete()
        
    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.order = Order(
            delivery_address="Kremlin2test",
            promocode="TEST",
            user=self.user,
        )
        self.order.save()
        self.order.products.add(1)
        
    def tearDown(self) -> None:
        self.order.delete()
        
    def test_order_details(self):
        response = self.client.get(reverse("shopapp:order_details", kwargs={"pk": self.order.pk}))
        self.assertContains(response, "address")
        self.assertContains(response, "Promocode")
        self.assertEquals(self.order.pk, response.context["object"].pk)


class OrdersExportTestCase(TestCase):
    """ Тест для экспорта всех заказов. """
    
    @classmethod
    def setUpClass(cls):
        cls.credentials = dict(username="temp_user", password="q")
        cls.user = User.objects.create_user(**cls.credentials)
        content_type = ContentType.objects.get_for_model(Order)
        permission = Permission.objects.get(
            codename="view_order",
            content_type=content_type,
        )
        cls.user.user_permissions.add(permission)
    
    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
    
    def setUp(self) -> None:
        self.client.force_login(self.user)
    
    def test_orders_export(self):
        response = self.client.get(reverse("shopapp:export_orders"))
        self.assertEqual(response.status_code, 200)
        expected_data = [
            {
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user": order.user,
                "products": [i_product.name for i_product in order.products]
            }
            for order in Order.objects.order_by("pk").all()
        ]
        recived_data = response.json()
        self.assertEqual(recived_data["orders"], expected_data)
        
        
        