from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_your_view(self):
        url = reverse("home")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
