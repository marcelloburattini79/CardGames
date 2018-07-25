from django.test import TestCase
from django.urls import reverse, resolve
from .views import home
from .models import Carta, seme

# Create your tests here.
class HomeTests(TestCase):

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/home')
        self.assertEquals(view.func, home)


class setteMezzoCarteTests(TestCase):

    def setUp(self):
        seme1 = seme.objects.create(value=2, colore="Spade")
        Carta.objects.create(value=1, tipo=seme1)

    def test_board_topics_view_success_status_code(self):
        url = reverse('carta', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

