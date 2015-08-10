from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1, 2)

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        #self.assertTrue(response.content.startswith('<html>'))
        #self.assertIn('<title>To-Do lists</title>', response.content)
        #self.assertTrue(response.content.strip().endswith('</html>'))

    def test_home_page_can_save_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A New List Item'
        response = home_page(request)
        self.assertIn('A New List Item', response.content.decode())
        expected_html = render_to_string(
                'home.html',
                {'new_item_text': 'A New List Item'}
                )
        self.assertEqual(response.content.decode(), expected_html)


