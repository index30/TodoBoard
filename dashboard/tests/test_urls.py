from django.test import TestCase
from django.urls import reverse, resolve
from dashboard.views import index

class TestUrls(TestCase):
    def test_home_url(self):
        url = reverse('home_view')
        self.assertEqual(resolve(url).func, index)