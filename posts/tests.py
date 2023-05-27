from django.test import TestCase, Client
from django.urls import reverse

class Contacts(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contacts(self):
        response = self.client.get(reverse("view-get_method"))
        data = "Это страница contacts"
        self.assertEqual(response.content.decode(), data)

    def test_about(self):
        response = self.client.get(reverse("view-get_about"))
        data = "Это страница about"
        self.assertEqual(response.content.decode(), data)

    def test_hello(self):
        response = self.client.get(reverse("view-hello"))
        data = {"name": "Alex"}
        self.assertEqual(response.headers.get("name"), "Alex") 