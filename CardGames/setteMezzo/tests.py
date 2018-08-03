from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, carta_dett, new_topic
from .models import Carta, seme

# Create your tests here.
class HomeTests(TestCase):

    def setUp(self):
        seme_carta = seme.objects.create(value=2, colore="Spade")
        self.carta = Carta.objects.create(value=1, tipo=seme_carta)
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_carta_dett(self):
        carta_dett_url = reverse('carta', kwargs={'pk': self.carta.pk})
        print(self.response)
        self.assertContains(self.response, 'href = "{0}"'.format(carta_dett_url))


class setteMezzoCarteTests(TestCase):

    def setUp(self):
        seme_carta = seme.objects.create(value=2, colore="Spade")
        Carta.objects.create(value=1, tipo=seme_carta)

    def test_carta_dett_view_success_status_code(self):
        url = reverse('carta', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_carta_dett_view_not_found_status_code(self):
        url = reverse('carta', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_carta_dett_url_resolves_carta_dett_view(self):
        view = resolve('/carta/1')
        self.assertEquals(view.func, carta_dett)

    def test_carta_dett_view_contains_link_back_to_homepage(self):
        carta_dett_url = reverse('carta', kwargs={'pk': 1})
        response = self.client.get(carta_dett_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))


class NewTopicTests(TestCase):
    def setUp(self):
        seme_carta = seme.objects.create(value=2, colore="Spade")
        Carta.objects.create(value=1, tipo=seme_carta)

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/carta/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_carta_dett_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        carta_dett_url = reverse('carta', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(carta_dett_url))

