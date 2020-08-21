from django.test import TestCase
from django.urls import resolve
from .views import home_page

# Create your tests here.

class MineralTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):

        result = resolve('/')
        self.assertEqual(result.func, home_page)

    
