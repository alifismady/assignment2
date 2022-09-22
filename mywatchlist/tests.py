from django.test import TestCase, Client
from django.urls import reverse

class MyWatchListTest(TestCase):
    def test(self):
        html_response = Client().get(reverse('mywatchlist:show_watchlist_html'))
        xml_response = Client().get(reverse('mywatchlist:show_xml'))
        json_response = Client().get(reverse('mywatchlist:show_json'))
        self.assertEqual(html_response.status_code, 200)
        self.assertEqual(xml_response.status_code, 200)
        self.assertEqual(json_response.status_code, 200)

#
