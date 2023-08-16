from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_your_view(self):
        url = reverse("home")  # Thay 'your-view-url' bằng URL của view bạn muốn test

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
