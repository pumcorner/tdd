from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page

# Create your tests here.

class MineralTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):

        result = resolve('/')
        self.assertEqual(result.func, home_page)

    def test_home_page_view_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    
