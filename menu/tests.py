from django.test import TestCase
from .models import Dish


class DishVisibilityTests(TestCase):
    def test_hidden_dish_stays_in_database_but_not_public_menu(self):
        dish = Dish.objects.create(
            name='Platillo temporal',
            description='No disponible hoy',
            price='25.00',
            available=False,
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, dish.name)
        self.assertTrue(Dish.objects.filter(pk=dish.pk).exists())

    def test_available_dish_is_public(self):
        dish = Dish.objects.create(
            name='Platillo disponible',
            description='Disponible hoy',
            price='30.00',
            available=True,
        )

        response = self.client.get('/')

        self.assertContains(response, dish.name)
